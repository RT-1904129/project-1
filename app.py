from urllib import request
from flask import Flask, render_template, request
import predict

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello():
    price_pred = 0
    if request.method == "POST":
        LandSlope = request.form['landSlope']
        OverallQual = request.form['overallQual']
        GarageCars = request.form['garageCars']
        OverallCond = request.form['overallCond']
        Fireplaces = request.form['fireplaces']
        price_pred =  predict.predict_price( LandSlope, OverallQual, GarageCars, OverallCond, Fireplaces )
    return render_template("index.html", my_pred = price_pred)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)