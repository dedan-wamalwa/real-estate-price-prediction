
from flask import Flask , request, jsonify
import utilities
app = Flask(__name__)
@app.route('/get_locations')
def get_locations():  
    response = jsonify({
        'locations' : utilities.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_price',methods = ['POST'])
def predict_price():
    location = request.form['location']
    size= float(request.form['sqft'])
    bhk= int(request.form['bhk'])
    baths = int(request.form['bath'])

    response=jsonify({
        'price ':utilities.get_prices(location,size,bhk,baths)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__ == "__main__":
    print ("Starting python flask server")
    app.run()

