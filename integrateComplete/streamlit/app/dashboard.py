import streamlit as st
import requests
import pymongo
import pandas as pd
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import time
import streamlit.components.v1 as components
# import option_menu
# from streamlit_option_menu
from pyecharts import options as opts
from pyecharts.charts import Line
from streamlit_echarts import st_echarts
from streamlit_extras.stylable_container import stylable_container
#change background color
# Use st.markdown to set the background color
st.set_page_config(
    page_title="Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)


    
@st.cache_resource
def init_connection():
    # Update the MongoDB connection URL
    return pymongo.MongoClient("mongodb://tesarally:contestor@mongodb:27018")

client = init_connection()
# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=10)
def get_data():
    db = client['waterdatatest']
    items = db.waterdatadetail.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

    # ทำสิ่งที่คุณต้องการด้วยข้อมูลที่ได้รับ
df = pd.DataFrame.from_dict(items)
# st.table(df)



def home():
    c1, c2, c3, c4, c5, c6,c7, c8= st.columns(8)
    with c4:
        with stylable_container(
            key="lv_image",
            css_styles="""
            img {   
                border-radius: 100%;
                margin-top: -30px;;
            }
            """,
        ):
            st.image("images.jfif", width=100)

    with c5:
        with stylable_container(
            key="KMITL_image",
            css_styles="""
            img {
                margin-top: -130px;
                margin-left: -80px;
                display: flex;
            }
            """,
        ):
            st.image("luvinas.svg", width=300)

    #creat title center page
    st.markdown("""
        <style>
            .center {
                margin-top: -100px;
                display: flex;
                justify-content: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # ใช้ div กล่องล้อมสำหรับ Title และใส่ class="center"
    st.markdown('<div class="center"><h1>ระบบแสดงผล และการจจัดการสภาวะน้ำท่วมและน้ำแล้ง</h1></div>', unsafe_allow_html=True)

    st.write("###")
    

    button_clicked = False

    c1, c2, _ = st.columns([1, 1, 2])

    with c1:
        with stylable_container(
            key="green_button",
            css_styles="""
                button {
                    background-color: #1E90FF;
                    color: white;
                    border-radius: 20px;
                }
                """,
        ):
            button_clicked = st.button("รับข้อมูลจาก T-SIM CAM")

    if button_clicked:
        with st.spinner("ร้องขอข้อมูลแล้ว กรุณารอสักครู่"):
            url = 'http://fastapi/mqtt/'

            try:
                r = requests.get(url)
                r.raise_for_status()
                response_data = r.json()
                # Process the response_data as needed
                st.success("ข้อมูลได้รับสำเร็จ")
            except requests.exceptions.RequestException as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")





    wTheight = df['w_height'].iloc[-1]  # Assuming 'w_height' is a numeric column
    wTdischarge = df['w_discharge'].iloc[-1]  # Assuming 'w_discharge' is a numeric column
    # Assuming df is your DataFrame and you want to get the previous row's values
    pre_wTheight = df['w_height'].iloc[-2]  # Assuming 'w_height' is a numeric column
    pre_wTdischarge = df['w_discharge'].iloc[-2]  # Assuming 'w_discharge' is a numeric column

    # create three columns
    kpi0, kpi1, kpi2 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="## ความสูง (ม.รทก)",
        value=(wTheight),
        delta=(wTheight) - (pre_wTheight),
    )

    kpi2.metric(
        label="## ปริมาณน้ำ (ลูกบาศก์เมตรต่อวินาที)",
        value=(wTdischarge),
        delta=(wTdischarge) - (pre_wTdischarge),
    )

    # wTheight=wTheight
    # wTdischarge=wTdischarge

    # Data
    categories = ["56", '57', '58', '59', '60']
    # y = [150, 230, 224, 218, 135, 147, 260]
    data = df['w_height'].iloc[-5:].tolist()

    # ECharts options
    echarts_options = {
        'xAxis': {'type': 'category', 'data': categories},
        'yAxis': {'type': 'value'},
        'series': [{'data': data, 'type': 'line'}]
    }


    st.write("###")
    # Streamlit app
    st.title('กราฟแสดงการเปลี่ยนแปลงระดับน้ำ')

    # Render ECharts
    chart = st_echarts(
        options=echarts_options,
        height=400,
        theme='light',
    )

    # Display the chart
    st.write(chart)


def page1():
    st.markdown("""
        <style>
            .center {
                display: flex;
                justify-content: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # ใช้ div กล่องล้อมสำหรับ Title และใส่ class="center"
    st.markdown('<div class="center"><h1>กราฟคาดการณ์ระดับน้ำในอนาคต</h1></div>', unsafe_allow_html=True)
    categories = ["61", '62', '63', '64', '65']
    # y = [150, 230, 224, 218, 135, 147, 260]
    data = df['w_height'].iloc[-5:].tolist()
    # data = df['w_height'].iloc[-5:].tolist()

    # ECharts options
    echarts_options = {
        'xAxis': {'type': 'category', 'data': categories},
        'yAxis': {'type': 'value'},
        'series': [{'data': data, 'type': 'line'}]
        # 'series': [{'data': data, 'type': 'line'}]
    }


    st.write("###")
    # Streamlit app
    st.title('กราฟแสดงการเปลี่ยนแปลงระดับน้ำ')

    # Render ECharts
    chart = st_echarts(
        options=echarts_options,
        height=400,
        theme='light',
    )

    # Display the chart
    st.write(chart)



menu = ["หน้าหลัก", "สถานีวัดน้ำ 1"]
choice = st.sidebar.selectbox("### เลือกหน้า", menu)
if choice == "หน้าหลัก":
    home()
elif choice == "สถานีวัดน้ำ 1":
    page1()


# while True:
#     items = get_data()
#     st.sleep(5)
# def ChangeButtonColour(wgt_txt, wch_hex_colour = '12px'):
#     htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
#                 for (i = 0; i < elements.length; ++i) 
#                     { if (elements[i].innerText == |wgt_txt|) 
#                         { elements[i].style.color ='""" + wch_hex_colour + """'; } }</script>  """

#     htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
#     components.html(f"{htmlstr}", height=0, width=0)

# cols = st.columns(4)
# cols[1].button('green', key='b2')
# cols[2].button('red', key='b3')

# ChangeButtonColour('green', '#4E9F3D') # button txt to find, colour to assign
# ChangeButtonColour('red', '#FF0000') # button txt to find, colour to assign
# # Data
# categories = ['61', '62', '63', '64', '65']
# data_gr = df['w_height'].iloc[-5:].tolist()

# # Create Pyecharts Line Chart
# line_chart = (
#     Line()
#     .add_xaxis(categories)
#     .set_global_opts(title_opts=opts.TitleOpts(title="Stacked Area Chart"))
# )

# # Add series to the chart
# for name, values in data_gr.items():
#     line_chart.add_yaxis(name, values, is_smooth=True, stack="total", area_style_opts=opts.AreaStyleOpts(opacity=0.7))

# # Render the chart
# st_pyecharts = st.pyecharts()
# st_pyecharts.chart(line_chart)

# # You can also save the chart as an HTML file if needed
# line_chart.render("stacked_area_chart.html")

# # You can also save the chart as an HTML file if needed
# line_chart.render("stacked_area_chart.html")
