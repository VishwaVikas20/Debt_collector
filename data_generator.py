import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)

# Number of rows (customers)
num_customers = 1000

# Generate Dummy Data
data = {
    'Customer_ID': [f'CUST_{i:04d}' for i in range(num_customers)],
    
    # Amount they owe (₹1,000 to ₹5,00,000)
    'Amount_Due': np.random.randint(1000, 500000, num_customers),
    
    # How many days late (10 days to 365 days)
    'Days_Overdue': np.random.randint(10, 365, num_customers),
    
    # Customer Credit Score (300 to 850)
    'Credit_Score': np.random.randint(300, 850, num_customers),
    
    # Previous defaults (0 to 5 times)
    'Past_Defaults': np.random.choice([0, 1, 2, 3, 4, 5], num_customers, p=[0.6, 0.2, 0.1, 0.05, 0.03, 0.02]),
    
    # Interaction History (How many times we called them)
    'Calls_Made': np.random.randint(0, 20, num_customers),
    
    # Current Agency Assigned (None if new case)
    'Assigned_Agency': np.random.choice(['Alpha Collections', 'Beta Recovery', 'Gamma Legal', 'None'], num_customers),
}

df = pd.DataFrame(data)

# --- ADDING LOGIC FOR TARGET VARIABLE (Recovery_Probability) ---
# We simulate a "Recovery Score" based on rules so your model actually learns something.
# Rule: High credit score + Low Amount + Low Days Overdue = High Probability
def calculate_prob(row):
    score = 0.5 # Base probability
    
    # Credit Score Impact
    if row['Credit_Score'] > 750: score += 0.3
    elif row['Credit_Score'] < 500: score -= 0.3
    
    # Overdue Impact
    if row['Days_Overdue'] > 180: score -= 0.2
    
    # History Impact
    if row['Past_Defaults'] > 2: score -= 0.2
    
    return max(0.01, min(0.99, score)) # Keep between 0 and 1

df['Recovery_Probability'] = df.apply(calculate_prob, axis=1)

# Create a binary target "Paid_In_Full" (1 = Yes, 0 = No) based on probability
df['Target_Paid'] = (np.random.rand(len(df)) < df['Recovery_Probability']).astype(int)

# Save to CSV
df.to_csv('fedex_debt_data.csv', index=False)
print("Data Generated Successfully: fedex_debt_data.csv")
print(df.head())
