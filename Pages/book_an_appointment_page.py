# from Scripts.constants import *
import Scripts.constants as constants
import Scripts.Utilities as Utils
from datetime import datetime, timedelta

from Scripts.doctor import get_docs_availiable_at, book

from Scripts.data_loader import get_users_data


def show_doc_table(st, data):
    import pandas as pd
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
        fit_columns_on_grid_load=True,
        theme='streamlit', #Add theme color to the table
        enable_enterprise_modules=True,
        height=350, 
        width='100%',
        reload_data=True
    )

    # data = grid_response['data']
    selected_doc = grid_response['selected_rows']
    
    return selected_doc[0] if selected_doc else None


def show_booking_form(st):
    if constants.CURR_USER == None:
        st.warning("Please login to continue")
        return None

    date_and_time = convert_to_datetime(
        st.date_input("Select A Date of Appointment", value=datetime.now()),
        st.time_input("Select A Time of Appointment", value=datetime.now() + timedelta(minutes=2))
    )

    specialization = st.selectbox("Select a specialization", ["Cardiology", "Neurology", "Orthopedics", "Gynaecology", "Dermatology"])

    info_box = st.empty()

    if not is_future_date(date_and_time):
        info_box.warning("You have entered an Invalid Date or Time")
        return None

    
    selected_docs = get_docs_availiable_at(
        date_and_time = date_and_time,
        criteria="specialization",
        value=specialization
    )

    doctors = {k: v for k, v in selected_docs}

    for doc in doctors.values():
        del doc["password"]

    if doctors:
        selected_doc = show_doc_table(st, doctors.values())
    else:
        info_box.warning("No doctor available at the moment")
        return None

    if selected_doc != None:
        # TODO :- https://towardsdatascience.com/visualization-in-python-finding-routes-between-points-2d97d4881996
        
        # TODO :- Remove this eval
        # Utils.add_folium_map(
        #     None, 
        #     [eval(selected_doc["location"])], [selected_doc["name"]],
        # )

        Utils.add_folium_map_route(
            None,
            location_1 = eval(selected_doc["location"]),
            doc_1 = selected_doc["name"],
            location_2 = get_users_data()[constants.CURR_USER]["location"],
            doc_2 = constants.CURR_USER,
            label=None
        )

        # selected_doc_id = None
        selected_doc['location'] = eval(selected_doc['location'])

        for k, v in doctors.items():
            if v == selected_doc:
                selected_doc_id = k
                break

        placeholder = st.empty()

        if Utils.center_button(st, "Book My Appointment"): # TODO :- Center button on webpage
            try:
                book(
                    date_and_time=date_and_time,
                    doc_id=selected_doc_id,
                    patient_id=constants.CURR_USER
                )
                placeholder.success("Your booking has been made")
                st.balloons()
            except Exception as e:
                raise e



def convert_to_datetime(date, time):
    return datetime(
        date.year, date.month, date.day, time.hour, time.minute, time.second
    )

def is_future_date(date_and_time):    
    return datetime.now() <= date_and_time 


def show_book_an_appointment_page(st):
    Utils.website_heading(
        st,
        content="Book an appointment",
        symbol="🤝",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)

    if constants.CURR_USER_IS_DOC:
        st.warning("The Booking Feature is only present for users and not doctors.")
    elif constants.CURR_USER == None:
        st.warning("Please login to continue with this feature")
    else:
        show_booking_form(st)