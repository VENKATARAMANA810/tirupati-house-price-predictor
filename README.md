# 🏡 Tirupati House Price Predictor

A real-time machine learning web application that predicts house prices in **Tirupati** based on area (sqft), number of BHKs, location, and property type. The model is trained on data scraped from MagicBricks.

---

## 📌 Features

- 🔍 Predicts prices for properties in Tirupati
- 📊 Trained using Random Forest Regressor
- 🖥️ Frontend built using Streamlit
- ⚙️ Backend API built using Flask
- 📁 Data scraped from MagicBricks and cleaned

---

## 💻 Tech Stack

- Python (Pandas, NumPy)
- Scikit-learn
- XGBoost
- Streamlit
- Flask
- Joblib

---

## 📈 Model Performance

- **Model**: Random Forest Regressor
- **R² Score**: 0.735
- **MAE**: ₹15.2 Lakhs

---

## 🚀 How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/tirupati-house-price-predictor.git
   cd tirupati-house-price-predictor
   
2.**Install Dependencies**
   pip install -r requirements.txt
   
3.**Start the Flask API**
   python app.py
   
4.**Run Streamlit App in a New Terminal**
   streamlit run streamlit_app.py
   
##🗃️ Project Structure
  tirupati-house-price-predictor/
├── app.py                     # Flask backend (API)
├── streamlit_app.py           # Streamlit UI
├── model.pkl                  # Trained ML model
├── tirupati_large_cleaned_data.csv  # Dataset
├── requirements.txt           # Python dependencies
├── screenshot.png             # UI Screenshot
└── README.md                  # Project description
##🖼️ Screenshot
![Screenshot 2025-07-06 210207](https://github.com/user-attachments/assets/965c56b8-5d4b-4665-91be-8dfe6fa9127c)




