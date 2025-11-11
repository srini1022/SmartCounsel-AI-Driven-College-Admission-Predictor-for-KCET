🎓 SmartCounsel – AI-Driven College Admission Predictor for KCET

🧠 Overview
SmartCounsel is an AI-powered web application that predicts suitable engineering colleges in Karnataka based on a student's KCET rank and reservation category.
It uses machine learning (Random Forest Regressor) trained on real KCET cutoff datasets to recommend colleges where a student is most likely to get admission.

🚀 Features
    🧩 AI Prediction Model – Uses Random Forest Regression to analyze cutoff trends.
    ⚙️ Dynamic Data Cleaning – Handles missing or invalid data automatically.
    💡 Smart Filtering – Predicts top N colleges based on user’s rank and category.
    📊 Downloadable Results – Generates a CSV file of predicted eligible colleges.
    🌐 Interactive Frontend – Built with HTML, CSS, and JavaScript.
    🔗 Flask REST API Backend – Provides endpoints for prediction and file download.

🏗️ Tech Stack
    Layer	Technology
    Frontend	HTML, CSS, JavaScript
    Backend	Python (Flask), Flask-CORS
    Machine Learning	Scikit-learn (RandomForestRegressor)
    Data Handling	Pandas, NumPy
    Dataset	KCET Cutoff Data (File.csv)

⚙️ Project Structure
SmartCounsel/
│
├── backend/
│   ├── app.py                         # Flask backend server (main logic)
│   ├── data/
│   │   └── File.csv                   # KCET cutoff dataset
│   └── exports/                       # Auto-generated prediction result CSVs
│
├── frontend/
│   ├── index.html                     # Web interface
│   ├── styles.css                     # UI styling
│   ├── app.js                         # Frontend logic (API integration)
│   └── img1.jpg                       # Background image
│
└── README.md                          # Project documentation


⚡ How It Works

    User selects their category (GM, 2AG, SCG, etc.).

    Enters their KCET rank and number of top colleges to display.

    The system:

    Loads and cleans the dataset.

    Encodes course names and fills missing cutoff values.

    Trains a Random Forest model on historical cutoff data.

    Predicts eligibility based on user input.

    Displays top predicted colleges and allows CSV download.

🧩 API Endpoints
    Endpoint	Method	Description
    /inspect	GET	Returns available cutoff categories
    /process	POST	Predicts colleges based on category and rank
    /download/<filename>	GET	Downloads prediction results

🔧 How to Run Locally

    1️⃣ Setup Backend
        cd backend
        pip install flask flask-cors pandas numpy scikit-learn
        python app.py

    2️⃣ Setup Frontend
        Place the frontend files (index.html, app.js, styles.css) in a folder like /frontend.

    3️⃣ Run the App
        Open your browser and go to:
        http://127.0.0.1:5000

🧮 Example Input
Category: GM
CET Rank: 25000
Top N: 10

✅ Example Output
    Institution	Course	Cutoff (GM)	Predicted Avg Cutoff
    PES University	CSE	27500	28050.12
    BMSCE	ISE	24000	24210.78
    RVCE	ECE	26000	26530.41
📈 Model Performance (Sample)
    Metric	Value
    R² Score	~0.85
    RMSE	~1500


🧑‍💻 Future Enhancements

    Add college location filters (city/district).
    Implement stream-wise predictions (CSE, ECE, ME, etc.).
    Integrate live KCET data updates.
    Deploy using Render / AWS / Heroku.

👨‍🎓 Author

    Project: SmartCounsel – AI Driven College Admission Predictor for KCET
    Developer: srinidhi M D
    Tech Stack: Flask + ML + Web Frontend
    Purpose: Academic/Portfolio Project demonstrating AI integration in educational guidance.
