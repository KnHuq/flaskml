from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def upload():
   return render_template('index.html')

def make_prediction(file):
    
    return 0.09


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

    
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        prediction = make_prediction(f.filename)
        return render_template('index.html',prediction = "The Prediction is {}".format(prediction))
    
    
    
if __name__ == '__main__':
     app.run(host = "0.0.0.0", port=8080)