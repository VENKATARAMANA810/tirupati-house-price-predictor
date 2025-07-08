# 🏠 Tirupati House Price Predictor

A real-time web app built using **Python, Streamlit, and Machine Learning** that predicts house prices in Tirupati based on area, location, number of bedrooms, and furnishing status.

![App Preview](https://raw.githubusercontent.com/VENKATARAMANA810/tirupati-house-price-predictor/main/app_screenshot.png)


## 🚀 Live Demo
👉 [Click here to try the app](https://tirupati-house-price-predictor-9j7yv32x9pbzsjanmnuhtk.streamlit.app/)

## 📌 Features
- Real-time prediction of house prices in Tirupati.
- User-friendly Streamlit interface.
- Trained using **Random Forest Regressor** for high accuracy.
- Data cleaned and preprocessed using Pandas.
- Supports custom user input for predictions.

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Matplotlib & Seaborn
- Git & GitHub

## 📂 Project Structure

tirupati-house-price-predictor/
│
├── app.py # Flask backend (optional)
├── streamlit_app.py # Streamlit frontend app
├── model.pkl # Trained Random Forest model
├── columns.pkl # Feature columns used in model
├── train model.ipynb # Model training notebook
├── tirupati_large_cleaned_data.csv # Cleaned dataset


## 📈 Model Info
- Model Used: **Random Forest Regressor**
- Metrics: R² Score, MAE
- Dataset: Custom scraped and cleaned dataset with location, area, bedrooms, etc.

## 📊 Sample Prediction
Input:
- Location: AIR Bypass Road
- Area: 1200 sqft
- Bedrooms: 3 BHK
- Furnishing: Semi-Furnished

Output:
Predicted Price: ₹ 48.5 Lakhs


## 👨‍💻 Developer
**Sunkara Venkataramana**  
📫 [GitHub](https://github.com/VENKATARAMANA810)  
📧 vramana086@gmail.com

---

> ⭐ *Don't forget to star this repository if you find it useful!*
