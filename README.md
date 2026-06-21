# 🌱 Crop Disease Detection System

An AI-powered Crop Disease Detection System that helps farmers identify plant diseases from leaf images and provides treatment recommendations.

## 📌 Features

- Upload crop leaf images
- Detect plant diseases using Deep Learning
- Display prediction confidence score
- Provide disease information
- Suggest treatment and prevention methods
- User-friendly Streamlit interface

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- OpenCV
- NumPy
- Pandas
- SQLite Database

## 📂 Project Structure

```
crop-disease-detection/
│
├── app.py
├── train.py
├── advisory.py
├── database.py
├── farm.db
├── requirements.txt
│
├── models/
│   ├── crop_disease_model.h5
│   └── class_indices.json
│
├── dataset/
│
├── pages/
│   ├── Disease_Predictor.py
│   ├── Fertilizer_Recommender.py
│   ├── Weather_Crop_Tips.py
│   └── Chatbot.py
│
└── README.md
```

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Priyu49/Crop-Disease-Detection.git
cd Crop-Disease-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## 🧠 Model Information

- Model: MobileNetV2
- Framework: TensorFlow/Keras
- Dataset: Plant Disease Dataset (Kaggle)
- Image Classification based Disease Detection

## 📸 Screenshots

Add screenshots of:
- Home Page
- Disease Prediction Page
  https://github.com/Priyu49/Disease-Detection-for-Crops/commit/ae79a5ca7789b0e138dcf9be9aa753427ddd9f2f
- Fertilizer Recommendation Page
- Weather Tips Page

## 🎯 Future Enhancements

- Real-time Camera Detection
- Multi-language Support
- Voice Assistant for Farmers
- Mobile Application
- Weather-based Disease Prediction

## 👩‍💻 Author

**Priyanka Kanade**

- GitHub: https://github.com/Priyu49

## 📜 License

This project is developed for educational and research purposes.
