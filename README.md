# 📦 SmartCollect: AI-Driven Debt Recovery System

> **"Optimizing Debt Recovery with Machine Learning & Intelligent Allocation"**

## 📖 Overview
**SmartCollect** is an intelligent operational tool designed to solve the inefficiency in debt collection. Instead of manually calling every debtor, SmartCollect uses **Machine Learning (XGBoost)** to predict the probability of repayment and automatically segments customers into cost-effective tiers.

### 💡 The Problem
* **High Costs:** Agents waste time calling low-risk customers who would pay anyway.
* **Low Efficiency:** High-risk, high-value debts are often missed due to random allocation.
* **Resource Drain:** Expensive legal teams are assigned to small debts.

### 🚀 The Solution
SmartCollect analyzes financial history (Credit Score, Past Defaults, Payment History) to categorize cases:
1.  🔴 **Tier 1 (High Risk):** Assigned to Premium Legal Teams (For High Value Debts).
2.  🟠 **Tier 2 (Medium Risk):** Assigned to Standard Collection Agencies.
3.  🟢 **Tier 3 (Low Risk):** Assigned to "Digital Nudge" Bots (Zero Cost SMS/Email).

## 🛠️ Features
* **Single Case Prediction:** Interactive dashboard for agents to check individual customer status.
* **Bulk Batch Processing:** Upload a CSV with 10,000+ records and get an instant downloadable report with Agency Allocations.
* **Privacy First:** No data is stored permanently; processing happens in-memory.

## 🏗️ System Architecture
`User (CSV Upload)` → `Flask Backend` → `Preprocessing Pipeline` → `XGBoost Model` → `Agency Allocation Logic` → `Downloadable Report`

## 💻 Tech Stack
* **Frontend:** HTML5, Bootstrap 5 (Responsive UI)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, XGBoost, Pandas, Joblib

## 📸 Screenshots

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/2aa71bba-3851-4b48-81b9-d30a23682e20" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/b64818ab-8759-4717-afd0-7e95f79b1658" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/2b1dedd1-ed0e-40b0-9824-fef67cf40028" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/021848ae-0ded-4074-aada-9084864d7eac" />


## 📸 Video Demo
Link to video : https://drive.google.com/file/d/1pjGy0dgOQL9RBYy3xTtBQpo2trtw3yFK/view?usp=drive_link

##Time stamps :
#  0:0-0:10  -  Intro
#  0:11-0:40 -  SinglePrediction
#  0:41-1:05 -  BatchPrediction
#  1:06-1:27 -  CostImpact

## ⚙️ Installation & Usage
1.  **Clone the repository**
    ```bash
    git clone https://github.com/VishwaVikas20/Debt_collector.git
    cd Debt_collector
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    
3.  **Run the Application**
    ```bash
    python app.py
    ```

4.  **Access the Dashboard**
    Open your browser and go to: `http://127.0.0.1:5000`

## ⚖️ Disclaimer
This project is a prototype developed for the **FedEx SMART Hackathon**. It is for educational and demonstration purposes only and is not commercially affiliated with FedEx Corporation. The dataset used is synthetic.
