import pickle
import json
import numpy as np 
__locations =None
__model =None
__columns=None

def load_artifacts():
    print("loading artifacts...")
    global __columns
    global __locations
    global __model
    with open("back-end/artifacts/colsdata.json",'r') as f:
        __columns=json.load(f)['datacols']
        __locations = __columns[3:]
    with open("back-end/artifacts/real_estate_model.pkl",'rb') as f:
        __model = pickle.load(f)
    print("loading finished")
# get locations from the json file
def get_locations():
    return __locations

def get_prices(location,size,bhk,bath):
    try:
        loc_idx=__columns.index(location.lower())
    except:
        loc_idx=-1
    x=np.zeros(len(__columns))
    x[0]=size
    x[1]=bath
    x[2]=bhk
    if loc_idx >=0:
        x[loc_idx]=1

    price = round(__model.predict([x])[0],2)
    price = "$ "+str(price)
    return price
if __name__ == "__main__":
    load_artifacts()
    # print(get_locations())
    print(get_prices("1st Phase JP Nagar",1200,3,3))