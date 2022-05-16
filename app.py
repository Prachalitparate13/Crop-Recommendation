from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Crop_Knn.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("crop_html.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Nitrogen
        N = int( request.form["Nitrogen"])
      

        #Phosphorus
        P =int(request.form["Phosphorus"])

        # potassium
        K = int(request.form["Potassium"])
      
        # temperature
        temperature = request.form["Temperature"]
            
       # humidity
        humidity = request.form["Humidity"]
       
        
        # ph
        ph = request.form["ph"]
      
        #rainfall
        rainfall = request.form["rainfall"]


        prediction=model.predict([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        output=prediction

        return render_template('crop_html.html',prediction_text="{} is recommended for your soil ".format(output))


    return render_template("crop_html.html")




if __name__ == "__main__":
    app.run(debug=True)
