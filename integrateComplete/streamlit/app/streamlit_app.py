# streamlit_app.py

import streamlit as st
import pymongo
import pandas as pd
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb://tesarally:contestor@mongodb:27018")

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client['waterDay2']
    items = db.waterdataday2.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

df = pd.DataFrame.from_dict(items)
st.dataframe(df)


#background colo
# Use st.markdown to set the background color
st.markdown(
    """
    <style>
        body {
            background-color:#CCF2F4; /* สีอ่อน */
        }
    </style>
    """,
    unsafe_allow_html=True
)

#create matrix visualize use col1.matrix
# col1, col2, col3 = st.columns(3)
# col1.metric("Date", "", "1.2 °F")
# col2.metric("", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")



waterfront = df['WaterDataFront'].to_list()
waterback = df['WaterDataBack'].to_list()
waterDrinRate = df['WaterDrainRate'].to_list()
year = df['Year'].to_list()



selected = st.selectbox('Select Data', ['WaterDataFront', 'WaterDataBack', 'WaterDrainRate'])
selectedyear = st.selectbox('Select Year', df['Year'].unique())
dfyear = df[df['Year'] == selectedyear]

st.write("## Data Metrics")
st.write("### Data Describe")
st.write(df.describe())


col1, col2, col3, col4= st.columns(4)
col1.metric("ปี", "year")
col2.metric("น้ำหน้าเขื่่อนสูงสุด", max(waterfront))
col3.metric("น้ำหลังเขื่่อนสูงสุด", max(waterback))
col4.metric("อัตราการระบายน้ำสูงสุด", max(waterDrinRate))

st.write("### Chart")
if selected == 'WaterDataFront':
    chart_data = dfyear[['Date', 'WaterDataFront']]
    chart = alt.Chart(chart_data).mark_bar(color='green').encode(x='Date', y=alt.Y('WaterDataFront', title='WaterDataFront (cm)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDataBack':
    chart_data = dfyear[['Date', 'WaterDataBack']]
    chart = alt.Chart(chart_data).mark_bar(color='yellow').encode(x='Date', y=alt.Y('WaterDataBack', title='WaterDataBack (cm)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDrainRate':
    chart_data = dfyear[['Date', 'WaterDrainRate']]
    chart = alt.Chart(chart_data).mark_bar(color='blue').encode(x='Date', y=alt.Y('WaterDrainRate', title='WaterDrainRate (cm)'))
    st.altair_chart(chart, use_container_width=True)

else:
    st.write("Select Data")
    
st.write("### graph line")

if selected == 'WaterDataFront':
    chart_data = dfyear[['Date', 'WaterDataFront']]
    chart = alt.Chart(chart_data).mark_line(color='green').encode(x='Date', y=alt.Y('WaterDataFront', title='WaterDataFront (m)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDataBack':
    chart_data = dfyear[['Date', 'WaterDataBack']]
    chart = alt.Chart(chart_data).mark_line(color='yellow').encode(x='Date', y=alt.Y('WaterDataBack', title='WaterDataBack (m)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDrainRate':
    chart_data = dfyear[['Date', 'WaterDrainRate']]
    chart = alt.Chart(chart_data).mark_line(color='blue').encode(x='Date', y=alt.Y('WaterDrainRate', title='WaterDrainRate (m)'))
    st.altair_chart(chart, use_container_width=True)

else:
    st.write("Select Data")



st.write("### plot graph")

if selected == 'WaterDataFront':
    chart_data = dfyear[['Date', 'WaterDataFront']]
    chart = alt.Chart(chart_data).mark_point(color='green').encode(x='Date', y=alt.Y('WaterDataFront', title='WaterDataFront (m)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDataBack':
    chart_data = dfyear[['Date', 'WaterDataBack']]
    chart = alt.Chart(chart_data).mark_point(color='yellow').encode(x='Date', y=alt.Y('WaterDataBack', title='WaterDataBack (m)'))
    st.altair_chart(chart, use_container_width=True)

elif selected == 'WaterDrainRate':
    chart_data = dfyear[['Date', 'WaterDrainRate']]
    chart = alt.Chart(chart_data).mark_point(color='blue').encode(x='Date', y=alt.Y('WaterDrainRate', title='WaterDrainRate (m)'))
    st.altair_chart(chart, use_container_width=True)

else:
    st.write("Select Data")
# year_selected = st.sidebar.selectbox("Select Year", df['Year'].unique())

# # กรองข้อมูลตามปีที่เลือก
# filtered_df = df[df['Year'] == year_selected]

# # สร้างกราฟ

# st.sidebar.header("Please Filter Here:")

# city = st.sidebar.selectbox("Select year:",
#                             options=df["Year"].unique(),
#                             index=0
# )

# areaLocality = st.sidebar.multiselect("Select month:",
#                 options=df.query("City == @city")["Area_Locality"].unique(),
#                 default=df.query("City == @city")["Area_Locality"].unique()[0],
# )

# areaType = st.sidebar.selectbox("Select the Area Type:",
#                 options=df["Year"].unique(),
#                 index=0
# )

# furnishing = st.sidebar.selectbox("Select the Furnishing Status:",
#                 options=df["Year"].unique(),
#                 index=0
# )

# st.title(":bar_chart: House Rent Dashboard")
# st.markdown("##")
# # average_rent = round(df_selection["Rent"].mean(),1)
# # average_size = round(df_selection["Size"].mean(), 2)
# left_column, right_column = st.columns(2)
# with left_column:
#         st.subheader("Average Rentalt:")
#         st.subheader(f"US $ {average_rent:,}")
# with right_column:
#         st.subheader("Average Size Room:")
#         st.subheader(f"M {average_size}")
# st.markdown("""---""")


#creat chart form data in df
# import plotly.express as px
# fig = px.line(df, x="Date", y="WaterDataFront", title='Water Data Front')
# st.plotly_chart(fig)

# #select year to show data barchart and show st.bar_chart year from select 
# year = st.selectbox('Select Year', df['Year'].unique())
# dfyear = df[df['Year']==year]
# # show st.bar_chart year from select dfyear

# st.line_chart(dfyear['WaterDataFront'])

# #select year to show data  and show st.bar_chart year from select 

    
