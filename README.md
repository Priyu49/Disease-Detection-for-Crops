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
  
  <img width="959" height="439" alt="Screenshot 2026-06-21 233243" src="https://github.com/user-attachments/assets/9e9c0fbf-5840-4491-b304-717ea670457f" />

- Disease Prediction Page
 <img width="1835" height="836" alt="Screenshot 2026-04-09 124429" src="https://github.com/user-attachments/assets/55d8c35c-93e0-4e76-be23-1b834e9398dc" />

  <img width="1835" height="836" alt="Screenshot 2026-04-09 124429" src="https://github.com/user-attachments/assets/92b669c9-8d0f-48f2-bbab-106b088fa566" />

- Fertilizer Recommendation Page
  <img width="881" height="400" alt="Screenshot 2026-06-21 233341" src="https://github.com/user-attachments/assets/5a5f5436-3644-42bd-8565-65aadec51d3e" />

  <img width="882" height="407" alt="Screenshot 2026-06-21 233411" src="https://github.com/user-attachments/assets/82f400ff-7341-4c6e-aabd-3e6dd4bbcee8" />

- Weather Tips Page

<img width="876" height="399" alt="Screenshot 2026-06-21 233533" src="https://github.com/user-attachments/assets/c43a9e21-7bed-4008-8a71-2aa1fea24b6d" />

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
