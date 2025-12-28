import pandas as pd
from flask import Flask, render_template, request, redirect, send_file
from io import BytesIO
import joblib

app = Flask(__name__)

try:
    model_pipeline = joblib.load('debt_pred_pipeline.pkl')
    print("Model pipeline loaded")
except:
    model_pipeline = None
    print("Model pipeline not found")

def best_agency(prob,amount):
    #Let,
    #Tier 1 : Legal and Recovery Agency
    #Tier 2 : Phone Call Agency
    #Tier 3 : Atomated Email and SMS Agency

    if prob < 0.4 :
        if amount > 5000:
            return "Tier 1 : Legal and Recovery Agency"
        else:#We don't want to spend much money on small debts
            return "Tier 3 : Atomated Email and SMS Agency"
    elif prob<0.7:
        if amount > 2000:
            return "Tier 2 : Phone Call Agency"
        else:#For small amount let this be this way, If duration increases then we will go to tier 2 treatment
            return "Tier 3 : Atomated Email and SMS Agency"
    else:#For prob>0.7 atomated agency is enough
        return "Tier 3 : Atomated Email and SMS Agency"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_one_person', methods=['POST'])
def predict_one_person():
    if request.method == 'POST':
        input_data = {
            'Amount_Due' : float(request.form['amount']),
            'Days_Overdue':float(request.form['days']),
            'Credit_Score':float(request.form['credit']),
            'Past_Defaults':int(request.form['defaults']),
            'Calls_Made':int(request.form['calls'])
        }
        input_df = pd.DataFrame([input_data])
        prob=model_pipeline.predict_proba(input_df)[0][1]
        agency=best_agency(prob,input_data['Amount_Due'])
        return render_template('index.html', single_result=f"{round(prob*100,2)}%", recommendation=agency)
    
@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    try:
        file=request.files['file']
        if not file:
            return "Please upload a file"
        df=pd.read_csv(file)
        features=['Amount_Due','Days_Overdue','Credit_Score','Past_Defaults','Calls_Made']
        df['Recovery_Probability']=model_pipeline.predict_proba(df[features])[:,1]
        df['Recommended_Agency']=df.apply(lambda row: best_agency(row['Recovery_Probability'], row['Amount_Due']), axis=1)

        #Export as Downloadable CSV file
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return send_file(output, mimetype='text/csv', as_attachment=True, download_name="Predictions.csv")
    except Exception as e:
        return f"An error occurred : {str(e)}"
    
if __name__ == '__main__':
    app.run(debug=True)
#Finally, End of code