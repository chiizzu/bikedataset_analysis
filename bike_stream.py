import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker

def create_df_working_casual(df):
    casual_df = df.groupby(by = 'workingday').agg({
        'casual_day' : 'sum'
    }).reset_index()

    return casual_df


def create_registered_df(df):
    registered_df = df.groupby(by= 'workingday').agg({
    'registered_day': 'sum'
    }).reset_index()

    return registered_df

def create_hour_df(df):
    hour_df = df.groupby('hr').agg({
    'cnt_hour': 'sum'
    }).reset_index()

    return hour_df

def create_month_df(df):
    month_df = df.groupby('mnth').agg({
    'cnt_day' : 'sum' 
    }).reset_index()
    
    return month_df

all_df = pd.read_csv('all_data.csv')


#membuat min_date dan max_date berdasarkan dteday
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    #mengambil start date dan end date
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]

    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

casual_day_df = create_df_working_casual(main_df)
registered_day_df = create_registered_df(main_df)
total_month_df = create_month_df(main_df)

#buat header
st.header('Bike Dataset Analysis')

st.subheader("Monthly Rent")

total_rent = main_df['cnt_day'].sum()
st.metric("Total Rent", value= total_rent)


fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    total_month_df["cnt_day"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
plt.xticks(ticks= range(1, 13, 1))
st.pyplot(fig)

st.subheader("Hourly Rent")
min_hr = all_df['hr'].min()
max_hr = all_df['hr'].max()


start_hour, end_hour = st.slider(
    "Pilih Rentang Jam", 
    min_value = min_hr, 
    max_value= max_hr, 
    value=[min_hr, max_hr]
)

hour_df_rent = all_df[(all_df['hr'] >= start_hour) & (all_df['hr'] <= end_hour)]
total_hour_df = create_hour_df(hour_df_rent)
total_hour_df['hour_label'] = total_hour_df['hr'].apply(lambda x: pd.to_datetime(x, format='%H').strftime('%I %p'))
total_rent_hour = hour_df_rent['cnt_hour'].sum()
st.metric("Total Rent by hour", value= total_rent_hour)

fig2, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    total_hour_df['hour_label'],
    total_hour_df['cnt_hour'],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.grid(True)
st.pyplot(fig2)

st.subheader("Total of Registered and Casual Customer")

#membuat grafik untuk pengguna casual dan registered
fig3, ax = plt.subplots(nrows= 1, ncols= 2, figsize= (20,5))

ax[0].yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax[1].yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

casual_day_df.plot(kind= 'bar', ax= ax[0], color= 'orange')
ax[0].set_title("Jumlah Pelanggan Casual di Hari Libur dan Hari Kerja")

registered_day_df.plot(kind= 'bar', ax= ax[1], color= 'skyblue')
ax[1].set_title("Jumlah Pelanggan Registered di Hari Libur dan Hari Kerja")

plt.tight_layout()
st.pyplot(fig3)

