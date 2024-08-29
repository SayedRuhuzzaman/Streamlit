import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("./car_price.csv")

st.write(
    """
    # Cars24 Used Car Price Predictor
    """
)
st.dataframe(cars_df.head())
col1,col2 = st.columns(2)

fuel_type = col1.selectbox("Select the Fuel Type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col1.slider("Set the Engine Power", 500,5000, step=100)
transmission_type = col2.selectbox("Select the Transmission Type", ["Manual", "Automatic"])
seats = col2.selectbox("Enter Number of Seats", [2,4,5,6,7,8,9,11])
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3 },
    "transmission_type": {'Manual': 1, 'Automatic':2}
}

def model_pred(fuel_type,engine,transmission_type,seats):

    ##Loading a Model
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[2018.0,1,4000,fuel_type,transmission_type,19.70,engine,86.30,seats]]

        
        return reg_model.predict(input_features)

if(st.button("Predict Price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, engine, transmission_type, seats)

    st.text(f"The Price of Car is {price[0].round(2)} Lakhs Rupees")