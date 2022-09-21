import json
import pickle

__locations = None
__data_columms = None
__model = None

def get_location_names():
    None

def load_saved_artifacts():
    print("Load saved artifacts..")
    global __data_columms
    global __locations

    with open(r"C:\Users\admin\Desktop\RealEstatePricePredictionModel\server\artifacts\columns (1).json", 'r') as f:
        __data_columms = json.load(f)['data_columns']
        __locations = __data_columms[3:]

    with open(r"C:\Users\admin\Desktop\RealEstatePricePredictionModel\server\artifacts\banglore_home_prices_model (1).pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts is done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    
