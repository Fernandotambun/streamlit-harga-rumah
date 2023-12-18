import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav','rb'))

st.title('Estimasi Harga Rumah')

LB = st.number_input('Input Luas Bangunan (m2)')
LT = st.number_input('Input Luas Tanah (m2)')
KT = st.number_input('Input Jumlah Kamar Tidur')
KM = st.number_input('Input Jumlah Kamar Mandi')
GRS = st.number_input('Input Jumlah Garasi')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[LB,LT,KT,KM,GRS]])
    # st.write('Estimasi Harga Rumah adalah  {}'.format(predict[0]))
    st.write('Estimasi Harga Rumah adalah : ', predict)