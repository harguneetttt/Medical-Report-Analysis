# Automated Medical Report Analysis and Recommendation System  
### Developed by: **Harguneet Kaur**  
### Guided by: **Mr. Mudrik Kaushik**  

---

## 📌 Overview  
Medical reports such as ECG summaries, lab results, or handwritten prescriptions are often difficult for patients to interpret and time-consuming for doctors to review.  
This project provides an **AI-powered medical report analyzer** capable of extracting text from scanned reports and producing structured summaries and recommendations.

The system integrates:
- **FastAPI** for backend processing  
- **EasyOCR** for text extraction from images  
- **Gemini 2.5 Flash** for medical summarization  
- **A clean, interactive frontend** for uploading, viewing summaries, and asking follow-up questions  
- A healthcare-themed UI branded as **HKPharma**

---

## 🚀 Features  
### **1. Image-based Medical Report Analysis**
Upload any medical report image (typed or handwritten).  
The system extracts text using EasyOCR and generates a clear summary.

### **2. AI-Generated Medical Insights**
Powered by Google Gemini:
- Summary of diagnosis  
- Abnormal findings  
- Detected medicines  
- Recommendations and general guidance  

### **3. Follow-up Chat System**
Users can ask contextual questions about the analyzed report.  
The chat retains history to give meaningful follow-up answers.

### **4. Modern Healthcare UI**
- Blue-white medical theme  
- HKPharma branding with logo  
- Easy upload interface  
- Summary panel + chat panel  
- Benefits section highlighting AI in healthcare  

---

## 🧠 System Architecture  
**The workflow includes:**  
1. Upload image →  
2. OCR text extraction (EasyOCR) →  
3. AI analysis (Gemini) →  
4. Summary generation →  
5. User follow-up chat →  
6. Display on frontend dashboard  

---

## 🏗️ Tech Stack  

### **Frontend**
- HTML  
- CSS (custom medical theme)  
- JavaScript (fetch API for communication)

### **Backend**
- **FastAPI** (Python)  
- **EasyOCR** (image text extraction)  
- **Pillow** (image handling)  
- **NumPy** (image preprocessing)  
- **Gemini AI API** (text analysis & summarization)

### **Additional Tools**
- dotenv  
- uvicorn (local server)  

---

## 📁 Project Structure  

```

├── main.py                # FastAPI backend
├── static/
│   ├── index.html         # Frontend UI
│   └── assets/...         # Icons, images (optional)
├── README.md
├── requirements.txt
└── .env                   # Gemini API key

````

---

## ⚙️ Installation & Setup  

### **1. Clone the repo**
```bash
git clone https://github.com/your-username/medical-report-analyzer.git
cd medical-report-analyzer
````

### **2. Create virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Add your Gemini API key**

Create a `.env` file:

```
GOOGLE_API_KEY=your_key_here
```

### **5. Run the server**

```bash
uvicorn main:app --reload
```

### **6. Open the web interface**

Visit:

```
http://127.0.0.1:8000
```

---

## 📊 Output Examples

The system returns:

### ✔ AI Summary

```
• Summary of medical report
• Abnormal findings
• Medicine details
• Recommendations
```

### ✔ Follow-up Q&A

Users can ask:

* What does the diagnosis mean?
* Should I be concerned?
* What lifestyle steps can I follow?

And get an AI-powered, context-aware explanation.

---

## 🧪 Testing

The model was tested on:

* Lab reports
* ECG summaries
* Typed prescriptions
* Handwritten prescriptions
* Scanned mobile photos

Focus areas:

* OCR accuracy
* Summarization clarity
* API response speed
* Frontend responsiveness

---

## 🎯 Applications

* **Doctors:** Quick pre-analysis for faster interpretation
* **Patients:** Understand complex medical reports
* **Educational:** Learn how AI interprets health data
* **Research:** Base for advanced medical AI models

---

## 🔮 Future Enhancements

* Support for X-ray, MRI, and CT scan analysis
* Deep learning–based medical diagnosis models
* Real-time monitoring via wearable sensors
* Multi-language report support
* More medically validated models

---

## 📜 License

This project is for educational and research use only.
Not intended for real medical diagnosis.
Prescriptions must be provided only by certified doctors.

---

