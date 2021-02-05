from flask import Flask, render_template, request
import pandas as pd
import joblib
import json

app = Flask(__name__)

@app.route('/')
def upload():
   return render_template('index.html')

def make_prediction(file):
    dummpy_df = pd.read_pickle("dummy.pkl")
    clf = joblib.load('model.pkl')
    
    # Opening JSON file 
    f = open(file) 

    # returns JSON object as  
    # a dictionary 
    data = json.load(f)

    data_final = {"Age":[int(data['Age'])],
              "Embarked": [data["Embarked"]],
              "Sex":[data["Sex"]]
              
              }
    q_df = pd.DataFrame(data_final)
    query = pd.get_dummies(q_df)
    final_q = query.combine_first(dummpy_df)
    prediction = clf.predict(final_q)
    return prediction[0]


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

    
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        try:
            prediction = make_prediction(f.filename)
            return render_template('index.html',prediction = "The Prediction is {}".format(prediction))
        except:
            render_template('index.html',prediction = "Something Went Wrong Mate!!!!!!)
    
    
if __name__ == '__main__':
     app.run(host = "0.0.0.0", port=8080)