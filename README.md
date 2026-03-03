# 🧴 Skin Disease Detection using Deep Learning

A web-based application that detects different types of skin diseases using a Deep Learning model built with PyTorch and deployed using Flask.

---

## 🚀 Project Overview

This project allows users to upload an image of a skin condition and receive a predicted disease category using a trained Convolutional Neural Network (CNN).

The system consists of:
```
- 🔹 Frontend (HTML, CSS, JavaScript)
- 🔹 Backend (Flask + PyTorch)
- 🔹 Deep Learning Model
- 🔹 Image Classification Pipeline
```
---

## 🏗️ Project Structure
```
Skin-Disease-Detection/
│
├── backend/
│ ├── run.py
│ └── (model files if applicable)
│
├── frontend/
│ ├── templates/
│ │ └── index.html
│ └── static/
│ ├── style.css
│ ├── main.js
│ └── Images/
│
├── requirements.txt
├── .gitignore
└── README.md

```
---

## 🧠 Technologies Used
```
- Python  
- Flask  
- PyTorch  
- Torchvision  
- HTML5  
- CSS3  
- JavaScript  
```
---


---

## 📂 Dataset

This project uses the **Skin Disease Dataset** available on Kaggle.

Dataset Source:  
🔗 https://www.kaggle.com/datasets/pacificrm/skindiseasedataset

### 📌 How to Download
```
1. Create a Kaggle account (if you don’t have one).
2. Visit the dataset link above.
3. Click on the **Download** button.
4. Extract the dataset after downloading.
```
### 📁 Dataset Placement

After extracting:

- Place the dataset folder inside your project directory.
- Update the dataset path in your training script if required.

⚠ Note: The dataset is not included in this repository due to GitHub file size limitations.

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```
git clone https://github.com/roysamarpita19/Skin-Disease-Detection.git
cd Skin-Disease-Detection
```
2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the Application
```
cd backend
python run.py
The app will run at:

http://127.0.0.1:5000/
```
## 📷 How It Works
User uploads an image

Image is preprocessed

CNN model predicts disease type

Result is displayed on the webpage

## 📌 Features
✔ Upload skin image
✔ Deep learning-based prediction
✔ Clean project structure
✔ GitHub-ready repository
✔ Modular frontend & backend separation

## 🛠 Future Improvements
Add confidence percentage

Deploy to cloud (Render / Railway)

Improve UI animations

Add model performance metrics

## 👩‍💻 Author
Samarpita Roy

## 📜 License
This project is created for educational and academic purposes.
