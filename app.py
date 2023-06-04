import streamlit as st
import pickle
import numpy as np
import pandas as pd

df=pd.read_csv('Laptop-data.csv')
forest = open('lap_price.pkl','rb')
model= pickle.load(forest)

st.title(':blue[LAPTOP PRICE PREDICTION APP]')
company={'Apple': 1.0, 'HP': 7.0, 'Acer': 0.0, 'Asus': 2.0, 'Dell': 4.0, 'Lenovo': 10.0, 'Chuwi': 3.0, 'MSI': 11.0, 'Microsoft': 13.0, 'Toshiba': 16.0, 'Huawei': 8.0, 'Xiaomi': 18.0, 'Vero': 17.0, 'Razer': 14.0, 'Mediacom': 12.0, 'Samsung': 15.0, 'Google': 6.0, 'Fujitsu': 5.0, 'LG': 9.0}
typename={'Ultrabook':4.0,'Notebook':3.0,'Netbook':2.0,'Gaming': 1.0,'2 in 1 Convertible':0.0,'Workstation':5.0}
cpu_brand={'Intel Core i5':2.0,'Intel Core i7':3.0,'AMD Processor':0.0,'Intel Core i3':1.0,'Other Intel Processor':4.0}
gpu_brand={'Intel':1.0,'AMD':0.0,'Nvidia':2.0}
os_brand={'Mac':0.0,'Others/No OS/Linux':1.0,'Windows':2.0}

col1,col2,col3=st.columns(3)
with col1:
    # Company
    comp=st.selectbox(':violet[Select Company]',df['Company'].unique())
    if comp in company:
        Company=company[comp]
        #st.write(Company)

    # TypeName
    tipe=st.selectbox(':violet[Select Type]',df['TypeName'].unique())
    if tipe in typename:
        TypeName=typename[tipe]
        #st.write(TypeName)

    # RAM
    Ram=st.selectbox(':violet[Select RAM (in GB)]',[2,4,6,8,12,16,24,32,64])

    # weight
    Weight =st.selectbox(':violet[Select Weight]',df['Weight'].unique())
    
    # screensize
    screen_size=st.selectbox(':violet[Select Screen Size]',df['Inches'].unique())

with col2:
    # Touchscreen
    touchscreen = st.selectbox(':violet[Touchscreen]', ['No', 'Yes'])
    if touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0
    #st.write(Touchscreen)

    # Ips
    ips = st.selectbox(':violet[Select IPS]', ['No', 'Yes'])
    if ips == 'Yes':
        Ips = 1
    else:
        Ips = 0
    #st.write(Ips)

    # resolution
    resolution = st.selectbox(':violet[Screen Resolution]',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    
    # Cpu brand
    cpu = st.selectbox(':violet[Select CPU]',df['Cpu brand'].unique())
    if cpu in cpu_brand:
        Cpu_brand = cpu_brand[cpu]
    st.text(" ")
    st.text(" ")
    # predict button
    predict=st.button('PREDICT PRICE')

with col3:
    # HDD
    HDD = st.selectbox(':violet[Select HDD (in GB)]',[0,32,128,256,500,512,1000,1024,2000,2048])

    #SSD
    SSD = st.selectbox(':violet[Select SSD(in GB)]',[0,8,16,32,64,128,180,240,256,512,768,1000,1024])

    #Gpu Brand
    brand = st.selectbox(':violet[Select Gpu Brand]',df['Gpu brand'].unique())
    if brand in gpu_brand:
        Gpu_brand = gpu_brand[brand]
        #st.write(Gpu_brand)

    # OS
    osb = st.selectbox(':violet[Select OS]',df['os'].unique())
    if osb in os_brand:
        os=os_brand[osb]
        #st.write(os)

if predict:
    y = np.array([[Company, TypeName, Ram, Weight, Touchscreen, Ips, ppi,Cpu_brand, HDD, SSD, Gpu_brand, os]])
    new = model.predict(y)
    st.write("### :green[The predicted price of this configuration is]"+" "+str(int(np.exp(new[0]))))







