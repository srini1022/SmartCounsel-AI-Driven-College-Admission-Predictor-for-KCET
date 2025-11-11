from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import re
import os
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import time

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(APP_DIR, "data", "File.csv")   # dataset path
EXPORT_DIR = os.path.join(APP_DIR, "exports")
FRONTEND_DIR = os.path.join(APP_DIR, "..", "frontend")

os.makedirs(EXPORT_DIR, exist_ok=True)

app = Flask(__name__)
CORS(app)  # allow local frontend

def load_and_clean_df(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at: {path}")

    df = pd.read_csv(path, encoding="latin1")
    if df.shape[1] < 3:
        raise ValueError("CSV must have at least 3 columns (Institution, CourseName, cutoffs...)")

    df = df.replace("--", np.nan)
    df.rename(columns={df.columns[0]: "Institution", df.columns[1]: "CourseName"}, inplace=True)

    # clean Institution
    df["Institution"] = (
        df["Institution"].astype(str)
        .str.replace("Ã", "", regex=False)
        .str.replace("Â", "", regex=False)
        .str.strip()
        .apply(lambda x: re.sub(r"^E\\d+\\w*\\s*", "", x))
    )

    # numeric cutoffs
    for col in df.columns[2:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    numeric_cols = df.select_dtypes(include=["number"]).columns
    df["AvgCutoffRank"] = df[numeric_cols].mean(axis=1, skipna=True)
    df = df[df["AvgCutoffRank"] > 0].copy()

    # encode course names
    le = LabelEncoder()
    df["CourseName_enc"] = le.fit_transform(df["CourseName"].astype(str))

    # category columns are numeric except helper cols
    exclude = {"AvgCutoffRank", "CourseName_enc"}
    category_columns = [c for c in numeric_cols if c not in exclude]
    return df, le, category_columns

# ----------------- API ROUTES -----------------

@app.route("/inspect", methods=["GET"])
def inspect():
    try:
        df, _, categories = load_and_clean_df(DATASET_PATH)
        return jsonify({"categories": categories})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/process", methods=["POST"])
def process():
    try:
        category = request.form.get("category", "").strip()
        rank_raw = request.form.get("rank", "").strip()
        top_n = int(request.form.get("top_n", 50))

        if not category:
            return jsonify({"error": "Missing 'category'"}), 400
        if not rank_raw:
            return jsonify({"error": "Missing 'rank'"}), 400

        try:
            user_rank = float(rank_raw)
        except:
            return jsonify({"error": "Rank must be a number"}), 400

        df, le, categories = load_and_clean_df(DATASET_PATH)
        if category not in df.columns:
            return jsonify({"error": f"'{category}' is not a valid category. Available: {categories}"}), 400

        X = df[["CourseName_enc", category]].copy()
        if X[category].isna().all():
            return jsonify({"error": f"Selected category '{category}' has no numeric values."}), 400

        X[category] = X[category].fillna(X[category].median())
        y = df["AvgCutoffRank"].values

        model = RandomForestRegressor(n_estimators=200, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        # Evaluate model performance
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        print(f"Model Performance for category '{category}':")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE: {rmse:.2f}")

        df["Predicted_AvgCutoffRank"] = model.predict(X)

        # eligibility: higher cutoff number means worse rank (eligible if cutoff >= user's rank)
        eligible = df[df[category] >= user_rank].copy()
        if eligible.empty:
            return jsonify({"results": [], "download": None, "message": "No eligible colleges found."})

        eligible = eligible.sort_values(by=category, ascending=True).head(top_n)
        final = eligible[["Institution", "CourseName", category, "Predicted_AvgCutoffRank"]]

        # save for download
        ts = int(time.time())
        safe_cat = re.sub(r"[^A-Za-z0-9_]+", "_", category)
        filename = f"eligible_colleges_{safe_cat}_{int(user_rank)}_{ts}.csv"
        final.to_csv(os.path.join(EXPORT_DIR, filename), index=False, encoding="utf-8-sig")

        return jsonify({
            "results": final.to_dict(orient="records"),
            "download": f"/download/{filename}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download/<path:filename>", methods=["GET"])
def download(filename):
    return send_from_directory(EXPORT_DIR, filename, as_attachment=True)

# ----------------- FRONTEND ROUTES -----------------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
