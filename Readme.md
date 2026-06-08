# 🎓 SmartCounsel – AI-Driven College Admission Predictor for KCET

## 🧠 Overview

SmartCounsel is an AI-powered web application that predicts suitable engineering colleges in Karnataka based on a student's KCET rank and reservation category.

The system uses a Machine Learning model (Random Forest Regressor) trained on historical KCET cutoff data to recommend colleges where a student is most likely to secure admission.

---

## 🚀 Features

- 🧩 AI-powered college admission prediction
- 📊 Random Forest Regression model
- ⚙️ Automated data cleaning and preprocessing
- 🎯 Personalized recommendations based on rank and category
- 📥 Downloadable CSV reports
- 🌐 Interactive web interface
- 🔗 Flask REST API backend
- 📈 Performance evaluation using R² Score and RMSE

---

## 🏗️ Tech Stack

| Layer | Technology |
|---------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask, Flask-CORS |
| Machine Learning | Scikit-Learn (RandomForestRegressor) |
| Data Processing | Pandas, NumPy |
| Dataset | KCET Historical Cutoff Data |

---

## ⚙️ Project Structure

```text
SmartCounsel/
│
├── backend/
│   ├── app.py
│   ├── data/
│   │   └── File.csv
│   └── exports/
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── img1.jpg
│
├── SmartCounsel AI-Driven College Admission Predictor for KCET.pdf
├── final certificate updated-302.pdf
│
└── README.md
```

---

## ⚡ How It Works

1. User selects a reservation category.
2. User enters their KCET rank.
3. User chooses the number of colleges to display.
4. The system:
   - Loads historical KCET cutoff data
   - Cleans and preprocesses the dataset
   - Encodes categorical features
   - Trains a Random Forest Regressor
   - Predicts eligible colleges
   - Displays recommendations
   - Allows CSV export of results

---

## 🧩 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/inspect` | GET | Returns available categories |
| `/process` | POST | Predicts colleges using rank and category |
| `/download/<filename>` | GET | Downloads prediction results |

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/SmartCounsel-AI-KCET-College-Predictor.git
cd SmartCounsel-AI-KCET-College-Predictor
```

### Install Dependencies

```bash
pip install flask flask-cors pandas numpy scikit-learn
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Example Input

```text
Category: GM
KCET Rank: 25000
Top N Colleges: 10
```

---

## 📈 Model Performance

| Metric | Value |
|---------|---------|
| R² Score | 0.85 – 0.98 |
| RMSE | 1500 – 9000 |

---

## 📄 Research Publication

### Conference Presentation

Presented at the **2nd International Conference on Optimization Techniques for Learning (ICOTL 2026)**

### Paper Title

**SmartCounsel: AI-Driven College Admission Predictor for KCET**

### Documents

- 📄 [Research Paper](./SmartCounsel%20AI-Driven%20College%20Admission%20Predictor%20for%20KCET.pdf)
- 🏆 [Conference Certificate](./final%20certificate%20updated-302.pdf)

---

## 🔮 Future Enhancements

- College location filtering
- Stream-wise recommendations
- Live KCET data integration
- Cloud deployment (AWS / Render)
- Analytics dashboard

---

## 👨‍💻 Author

**Srinidhi M D**

B.Tech – Computer Science and Engineering  
M S Ramaiah University of Applied Sciences

### Skills Demonstrated

- Machine Learning
- Random Forest Regression
- Flask Development
- Data Science
- Predictive Analytics
- Web Development
- REST API Development

---

⭐ If you found this project useful, consider giving it a star on GitHub.
