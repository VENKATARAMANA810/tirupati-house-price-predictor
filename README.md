# 🏠 Tirupati House Price Predictor

This is a real-time **Machine Learning web application** built using **Python, Scikit-learn, Streamlit, and Flask** that predicts house prices in Tirupati based on user input features such as square footage, number of bedrooms, location, and amenities.

## 🔍 Problem Statement

Property prices vary drastically based on location and features. Buyers and real estate professionals need a quick and accurate way to estimate housing prices. This project solves that problem with an ML-powered web app.

---

## 🚀 Demo

🔗 **Live Application**: *Currently in local deployment*

🔗 **GitHub Repository**: [Tirupati House Price Predictor](https://github.com/VENKATARAMANA810/tirupati-house-price-predictor)

---

## 🛠️ Features

- User-friendly web interface built with **Streamlit**
- Model served using **Flask** API
- Trained using **Scikit-learn**
- Real-time prediction based on user inputs
- Displays predicted price instantly
- Organized codebase for model training, API, and UI

---

## ⚙️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python      | Programming language             |
| Pandas      | Data cleaning and manipulation   |
| Scikit-learn| Model building                   |
| Flask       | Backend API to serve predictions |
| Streamlit   | Web UI for user interaction      |
| GitHub      | Version control and portfolio    |

---

## 📊 Model Workflow

1. **Data Collection**: CSV dataset with house features
2. **EDA & Cleaning**: Removed outliers, handled missing data
3. **Feature Engineering**: One-hot encoding for location and categorical fields
4. **Modeling**: Linear Regression, Ridge Regression (tuned with GridSearchCV)
5. **Deployment**: 
    - Model exported with `joblib`
    - Backend created with Flask
    - Frontend created with Streamlit
    - Integrated using API calls

---

## 📂 Project Structure

tirupati-house-price-predictor/
├── app.py # Flask API
├── model.pkl # Trained ML model
├── requirements.txt # Project dependencies
├── streamlit_app.py # Streamlit UI
├── utils.py # Helper functions
├── README.md # Project documentation
└── data/
└── house_data.csv # Cleaned dataset


---

## 📸 Screenshots

![App Screenshot 1](https://github.com/VENKATARAMANA810/tirupati-house-price-predictor/assets/your_screenshot_1.png)
*Prediction Page UI*

---

## 🧪 How to Run Locally

1. Clone the repo:

 git clone https://github.com/VENKATARAMANA810/tirupati-house-price-predictor.git
cd tirupati-house-price-predictor

2. Install requirements:

pip install -r requirements.txt

3. Run Streamlit App:

streamlit run streamlit_app.py


4. Access the web app at:

http://localhost:8501


---

## ✍️ Author

**Sunkara Venkataramana**  
📧 vramana086@gmail.com  
🔗 [GitHub Portfolio](https://github.com/VENKATARAMANA810)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/your-profile)

---

## 📌 License

This project is open-source and free to use for learning or reference purposes.


