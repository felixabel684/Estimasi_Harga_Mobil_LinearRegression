# import library pickle dan streamlit
import pickle
import streamlit as st

# load model yang sudah di training
model = pickle.load(open('estimasi_harga_mobil.sav', 'rb'))

# membuat judul dan inputan untuk estimasi harga mobil
st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil (km)')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi Bahan Bakar Mobil (mpg)')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

# identifikasi untuk model prediksi
predict = ''

# membuat kondisi button untuk estimasi harga mobil
if st.button('Estimasi Harga Mobil'):
    # yang mau di prediksi adalah model dan yang akan di prediksi atribut numerik (features)
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi Harga Mobil Bekas(Juta): ' , predict*16500)