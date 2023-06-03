import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
from xgboost import XGBRegressor

# import the model
pipe = pickle.load(open('lap_price.pkl','rb'))
df = pd.read_csv('Laptop-data.csv')

st.title(":violet[LAPTOP PRICE PREDICTOR]")
col1,col2,col3=st.columns(3)
with col1:
    st.subheader(':violet[COMAPANY]')
    company = st.selectbox('Brand',df['Company'].unique())

    st.subheader(':violet[TYPE]')
    type = st.selectbox('Type',df['TypeName'].unique())

    st.subheader(':violet[RAM]')
    ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

    # weight
    st.subheader(':violet[WEIGHT]')
    weight = st.number_input('Weight of the Laptop')
    
    # Touchscreen
    st.subheader(':violet[TOUCH SCREEN]')
    touchscreen = st.selectbox('Touchscreen',['No','Yes'])
with col2:
    # IPS
    st.subheader(':violet[IPS]')
    ips = st.selectbox('IPS',['No','Yes'])

    # screen size
    st.subheader(':violet[SCREEN SIZE]')
    screen_size = st.number_input('Screen Size')

    # resolution
    st.subheader(':violet[RESOLUTION]')
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

    #cpu
    st.subheader(':violet[CPU]')
    cpu = st.selectbox('CPU',df['Cpu brand'].unique())
    
    # hdd
    st.subheader(':violet[HDD]')
    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
with col3:
    # ssd
    st.subheader(':violet[SSD]')
    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
    
    # gpu
    st.subheader(':violet[GPU]')
    gpu = st.selectbox('GPU',df['Gpu brand'].unique())
    
    # os
    st.subheader(':violet[OS]')
    os = st.selectbox('OS',df['os'].unique())
    
    submit=st.button('Predict Price')
if submit:
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    new=pipe.predict(query)
    st.write(new[0])
    #st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

