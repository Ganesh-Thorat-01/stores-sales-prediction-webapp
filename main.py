from flask import Flask,render_template,request
from flask_cors import cross_origin
import requests
app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
   return render_template('home.html')


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
       Item_Weight=float(request.form["Item_Weight"])
       
       Item_Fat_Content=request.form["Item_Fat_Content"]

       Item_Visibility=float(request.form["Item_Visibility"])

       Item_Type=request.form["Item_Type"]
       
       Item_MRP=int(request.form["Item_MRP"])
       
       Outlet_Establishment_Year=int(request.form["Outlet_Establishment_Year"])
       
       Outlet_Size=request.form["Outlet_Size"]
       
       Outlet_Location_Type=request.form["Outlet_Location_Type"]
       
       Outlet_Type=request.form["Outlet_Type"]

       data={
            "Item_Weight": Item_Weight,
            "Item_Fat_Content": Item_Fat_Content,
            "Item_Visibility": Item_Visibility,
            "Item_Type": Item_Type,
            "Item_MRP": Item_MRP,
            "Outlet_Establishment_Year": Outlet_Establishment_Year,
            "Outlet_Size": Outlet_Size,
            "Outlet_Location_Type": Outlet_Location_Type,
            "Outlet_Type": Outlet_Type
            }
       
       response = requests.post('https://stores-sales-api.herokuapp.com/predict', json=data)
       result=response.text
       output=result.split(":",1)[1]
       output=output.replace("}","")
       return render_template('home.html',output=output)


    return render_template("home.html")

if __name__ == '__main__':
   app.run(debug = True)
   