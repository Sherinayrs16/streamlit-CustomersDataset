import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Model (customers_model.sav)
filename = 'CustomerDataset_model.sav'
model = pickle.load(open(filename, 'rb'))

# Convert model into a DataFrame
customers_df = pd.DataFrame(model)

# 2. Dashboard Layout

# Judul
st.title("Dashboard Pelanggan Berdasarkan Kategori Prioritas")
st.write("Dashboard ini menampilkan visualisasi pelanggan berdasarkan kategori prioritas: High, Medium, dan Low.")

# Sidebar for filtering data by State
st.sidebar.header("Filter Data")
state_options = customers_df['Customer_Group'].unique()
selected_state = st.sidebar.multiselect('Pilih Kategori Prioritas:', state_options, state_options)

# Filter data berdasarkan kategori yang dipilih
filtered_data = customers_df[customers_df['Customer_Group'].isin(selected_state)]

# 3. Display Data and Summary
st.header("Tabel Pelanggan")
st.write("Data pelanggan berdasarkan kategori prioritas yang dipilih:")
st.dataframe(filtered_data)

# Menampilkan summary data
st.header("Summary Data")
st.write(filtered_data.groupby('Customer_Group').agg({'customer_id': 'count'}))

# 4. Visualisasi

# Pie Chart untuk distribusi pelanggan berdasarkan Customer Group
st.subheader("Pie Chart: Distribusi Pelanggan Berdasarkan Kategori Prioritas")
fig, ax = plt.subplots(figsize=(8, 6))
filtered_data['Customer_Group'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Bar Chart untuk jumlah pelanggan per kategori prioritas
st.subheader("Bar Chart: Jumlah Pelanggan Berdasarkan Kategori Prioritas")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='Customer_Group', data=filtered_data, palette='viridis', ax=ax)
ax.set_xlabel('Kategori Prioritas')
ax.set_ylabel('Jumlah Pelanggan')
st.pyplot(fig)

# 5. Filtered Data for Further Analysis
st.subheader("Analisis Data Pelanggan")
st.write(f"Total Pelanggan berdasarkan Kategori Prioritas: {len(filtered_data)}")
st.write("Tabel berikut menunjukkan data pelanggan setelah difilter berdasarkan kategori prioritas yang dipilih:")
st.dataframe(filtered_data)

# Download filtered data as CSV
st.subheader("Unduh Data")
st.write("Klik tombol di bawah ini untuk mengunduh data pelanggan yang sudah difilter.")
csv = filtered_data.to_csv(index=False)
st.download_button(label="Unduh Data sebagai CSV", data=csv, file_name='filtered_customers.csv', mime='text/csv')

# Informasi Tambahan atau Interpretasi
st.write("""
* **High Priority**: Pelanggan dari provinsi dengan prioritas tinggi.
* **Medium Priority**: Pelanggan dari provinsi dengan prioritas menengah.
* **Low Priority**: Pelanggan dari provinsi dengan prioritas rendah.
""")
