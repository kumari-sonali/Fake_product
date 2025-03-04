# 🛒 Fake Product Review Detector  

🚀 **An AI-powered solution to detect fake product reviews using a fine-tuned RoBERTa model.**  

## 📌 Overview  

The **Fake Product Review Detector** is an **NLP-based machine learning model** that classifies **genuine vs. fake** product reviews. The project leverages **Hugging Face Transformers, OpenAI API, and deep learning techniques** to analyze textual patterns, helping businesses and consumers identify deceptive reviews.  

---

## 👨‍💻 Author  

**Pranjal**  
📍 Developed as part of the **National Institute of Technology Agartala**.  

---

## 🎯 Problem Statement  

### **Project 14: Fake Product Review Detector**  

### **Objective**  
- Train a **RoBERTa-based model** to classify **fake vs. genuine** product reviews.  
- Build a **user-friendly Streamlit UI** for review analysis.  
- Develop a **FastAPI-based backend** to deploy the ML model.  

### **Tech Stack Used**  
✅ **Programming Languages:** Python  
✅ **Libraries:** Transformers (Hugging Face), TensorFlow/PyTorch, spaCy, NLTK, LangChain  
✅ **Frameworks:** Streamlit, FastAPI  
✅ **Datasets:** Kaggle, Hugging Face Hub, UCI ML Repository  

---

## 🔍 **Proposed Solution**  

The project consists of **three major components**:  
1. **Streamlit UI** for user input and result display (`main.py`).  
2. **Fine-tuning the Fake Review Detector RoBERTa model** (`fake_review_detector.ipynb`).  
3. **FastAPI for backend API to serve the model predictions** (`api.py`).  

### **How It Works**  
1. **User enters a review** in the Streamlit UI.  
2. **The API processes the review** using the pretrained RoBERTa model.  
3. **Model predicts** if the review is **genuine or fake**, along with a confidence score.  
4. **Results are displayed** in the UI.  

---

## 🏗️ **Model Training & Fine-Tuning**  

### **Dataset Used**  
📥 **[Fake Reviews Dataset](https://www.kaggle.com/datasets/mexwell/fake-reviews-dataset)** (Kaggle)  

### **Preprocessing Steps**  
- **Dropped missing values** for cleaner data.  
- **Extracted relevant columns** (category, rating, review text).  
- **Converted labels to binary format** (0 = Genuine, 1 = Fake).  
- **Tokenization using RobertaTokenizer** (for input preparation).  

### **Training Details**  
- Loaded **pretrained RoBERTa base model** from Hugging Face.  
- Used **Trainer API** for fine-tuning.  
- Model trained for **3 epochs** with evaluation metrics.  
- **Final Model Saved** for deployment.  

📊 **Accuracy Metrics:**  

| Epoch | Accuracy | Loss  |
|-------|----------|-------|
| 1     | 84.2%    | 0.32  |
| 2     | 86.8%    | 0.29  |
| 3     | 89.1%    | 0.25  |

---

## 🛠️ **Installation & Setup**  

### **Prerequisites**  
📌 **Python 3.8+**  
📌 **Git installed on the system**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-username/fake-review-detector.git
cd fake-review-detector
```
### **Step 2: Install Required Dependencies**  
```bash
pip install fastapi pydantic torch transformers streamlit requests
```
### **Step 3: Download Dataset**
```bash
Place the dataset file in the root directory.
```
## 🚀 Usage Instructions  

### **1️⃣ Train the Model (Optional)**  
If you want to fine-tune the model again, open the Jupyter Notebook (`fake_review_detector.ipynb`) and execute the cells.  

### **2️⃣ Run the FastAPI Backend**  
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```
The API runs at http://127.0.0.1:8000.

### **3️⃣ Start the Streamlit UI**
```bash
streamlit run main.py
```
Open the provided URL in your browser.
Enter a product review and click "Check Review" to analyze it.

## 🎯 Use Cases
### **✅ E-commerce Platforms** 
   – Detect fraudulent reviews on Amazon, Flipkart, etc.
### **✅ Business Intelligence**
   – Remove spam or misleading feedback.
### **✅ Consumer Awareness**
   – Help buyers make informed decisions.
## 🤝 Contributing
### **👥 Contributions are welcome! To contribute:**

1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature-branch
```
3. Commit your changes and push the branch:
```bash
git push origin feature-branch
```
4. Open a Pull Request.

## 📜 License
### **📄 This project is licensed under the MIT License – feel free to modify and distribute!**

## 🌟 Acknowledgments
📍Hugging Face for transformers & datasets.
📍OpenAI for GPT-based NLP tools.