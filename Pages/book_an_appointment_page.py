# from Scripts.constants import *
import Scripts.constants as constants
import Scripts.Utilities as Utils
from datetime import datetime

from Scripts.doctor import get_docs_availiable_at


def make_table(st, data):
    import pandas as pd 
    import numpy as np
    from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

    data= pd.DataFrame(data)
    
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=350, 
        width='100%',
        reload_data=True
    )

    data = grid_response['data']
    selected = grid_response['selected_rows'] 
    df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe d 

    return dict(df.iloc[0])



def show_booking_form(st):
    if constants.CURR_USER == None:
        st.warning("Please login to continue")
        return None

    appointment_date = st.date_input("Select A Date of Appointment", value=datetime.now())
    appointment_time = st.time_input("Select A Time of Appointment")

    specialization = st.selectbox("Select a specialization", ["Cardiology", "Neurology", "Orthopedics", "Gynaecology", "Dermatology"])

    selected_docs = get_docs_availiable_at(
        date_and_time = convert_to_datetime(appointment_date, appointment_time),
        criteria="specialization",
        value=specialization
    )

    selected_docs = list(selected_docs)

    for doc in selected_docs:
        del doc["password"]

    selected_doc = make_table(st, selected_docs)
    Utils.add_folium_map(st.columns(2)[0], eval(selected_doc["location"]), selected_doc["name"])



def convert_to_datetime(date, time):
    return datetime(
        date.year, date.month, date.day, time.hour, time.minute, time.second
    )


def show_book_an_appointment_page(st):
    Utils.website_heading(
        st,
        content="Book an appointment",
        symbol=".",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)

    constants.CURR_USER = "xyz" # TODO : remove this

    show_booking_form(st)