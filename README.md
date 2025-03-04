# AIDE505_assignment_1


## **Project Overview**  
This project demonstrates how to integrate a **Flask-based Sentiment Analysis API** with an **Express.js web server**. The Flask API uses **VADER Sentiment Analysis** to classify input text as **positive, negative, or neutral**. The Express.js application acts as an intermediary, forwarding user input to the Flask API and returning the result.  

This assignment showcases **machine learning API deployment** and **backend integration** using Python and JavaScript.

---

## **1. Project Structure**  

```
sentiment-analysis-api/
├── flask-api/            # Flask-based sentiment analysis API
│   ├── app.py            # Main Python script
│   ├── requirements.txt  # List of dependencies
│── express-server/       # Express.js application
│   ├── index.js          # Main Express.js server file
│   ├── package.json      # Node.js dependencies
│── README.md             # Project documentation (this file)
│── .gitignore            # Global Git ignore file
```

---

## **2. Flask API – Backend Service**  

The Flask API performs **sentiment analysis** using **VADER Sentiment Analysis**. It exposes a RESTful endpoint that receives text input and returns a sentiment classification.

### **Setup & Installation**  
1. **Navigate to the Flask API directory:**  
   ```sh
   cd flask-api
   ```
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Flask server:**  
   ```sh
   python app.py
   ```
4. **API Endpoint Details:**  
   - **Endpoint:** `http://127.0.0.1:5000/predict`
   - **Method:** `POST`
   - **Input Format (JSON):**  
     ```json
     { "text": "I love machine learning!" }
     ```
   - **Output Format:**  
     ```json
     { "sentiment": "positive" }
     ```

---

## **3. Express.js Server – API Integration**  

The Express.js application acts as a **middleware** that receives user input and forwards it to the Flask API for analysis.

### **Setup & Installation**  
1. **Navigate to the Express.js directory:**  
   ```sh
   cd express-server
   ```
2. **Install dependencies:**  
   ```sh
   npm install
   ```
3. **Run the Express server:**  
   ```sh
   node index.js
   ```
4. **API Endpoint Details:**  
   - **Endpoint:** `http://localhost:3000/analyze-sentiment`
   - **Method:** `POST`
   - **Input Format (JSON):**  
     ```json
     { "text": "AI is the future!" }
     ```
   - **Output Format:**  
     ```json
     { "sentiment": "neutral" }
     ```

---

## **4. GitHub Repository & Version Control**  

The project is managed using **GitHub** for version control. Below are key version control practices implemented:

### **GitHub Repository:**  
[GitHub Link](https://github.com/Mohammadawad1/AIDE505_assignment_1.git)  

### **Version Control Practices:**  
- `.gitignore` files are included to exclude unnecessary files ( `/node_modules`, `*/__pycache__`).
- The project follows **best practices** for structuring API-based applications.
- The code is pushed using:

  ```sh
  git init
  git add .
  git commit -m "Initial submission of sentiment analysis API"
  git branch -M main
  git remote add origin https://github.com/Mohammadawad1/AIDE505_assignment_1.git
  git push -u origin main
  ```
---

## **5. Conclusion**  

This project successfully demonstrates how to **integrate a machine learning API (Flask)** with a **web server (Express.js)** to provide sentiment analysis services. The implementation follows best practices for API development, version control, and deployment considerations.

---

Thank you for reviewing my submission! I look forward to your feedback. 😊  

---
