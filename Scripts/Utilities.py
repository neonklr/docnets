import os
import Scripts.constants as constants
import streamlit as st


def remove_streamlit_marks(st):
    st.markdown(
        '''
            <style>
                footer { visibility: hidden; }
                /* #MainMenu { visibility: hidden; } */
                /* [data-testid=stHeader] { backdrop-filter: blur(1px); background: none; } */
            </style>
        '''
    , unsafe_allow_html=True)


def website_heading(container, content, symbol, font_size=60, color="blue", text_align="left"):
    container.markdown(f"""
    <p style="font-size: {font_size}px; font-family: Euclid Circular B,Arial,Helvetica,sans-serif; font-weight: 600; text-align: {text_align}">{content}<span style="color: {color};">{symbol}</span></p>
    """, unsafe_allow_html=True)

def add_space(container):
    container.markdown("""
    <br><br>
    """, unsafe_allow_html=True)


def get_column_mean(data, column_index):
    if len(data) == 0:
        return 0

    sum = 0
    for row in data:
        sum += row[column_index]

    return sum/len(data)


def add_folium_map_route(container, location_1, location_2, doc_1, doc_2, label, width=1200, zoom_start=8):
    
    if container == None:
        __add_folium_map_route(location_1, location_2, doc_1, doc_2, label, width, zoom_start)
    else:
        with container:
            __add_folium_map_route(location_1, location_2, doc_1, doc_2, label, width, zoom_start)


def __add_folium_map_route(location_1, location_2, doc_1, doc_2, label, width, zoom_start):

    from streamlit_folium import folium_static
    import folium

    # center on doctors location
    lon = get_column_mean([location_1, location_2], column_index=0)
    lat = get_column_mean([location_1, location_2], column_index=1)

    m = folium.Map(location=[lon, lat], zoom_start=zoom_start)
    
    folium.Marker(
        location_1,
        popup=doc_1,
        tooltip=doc_1,
    ).add_to(m)

    folium.Marker(
        location_2,
        popup=doc_2,
        tooltip=doc_2,
    ).add_to(m)

    f1=folium.FeatureGroup(label)

    # Adding lines to the different feature groups
    line_1=folium.vector_layers.PolyLine((location_1, location_2),popup=f'<b>{label}</b>',tooltip=label,color='red',weight=10).add_to(f1)

    f1.add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m, width=width)



def add_folium_map(container, locations, doc_names, width=1200, zoom_start=8):
    
    if container == None:
        __add_folium_map(locations, doc_names, width, zoom_start)
    else:
        with container:
            __add_folium_map(locations, doc_names, width, zoom_start)




def __add_folium_map(locations, doc_names, width, zoom_start):

    from streamlit_folium import folium_static
    import folium

    # center on doctors location
    lon = get_column_mean(locations, column_index=0)
    lat = get_column_mean(locations, column_index=1)

    m = folium.Map(location=[lon, lat], zoom_start=zoom_start)
    
    # add marker for a doctor
    for location, doc_name in zip(locations, doc_names):
        folium.Marker(
            location,
            popup=doc_name,
            tooltip=doc_name,
            #icon=folium.Icon(color='blue', icon='circle-h', prefix='fa')
        ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m, width=width)


def load_lottie_url(url):
    import requests

    r = requests.get(url)
    
    if r.status_code != 200:
        return None
    
    return r.json()


def show_lottie_animation(container, url):
    from streamlit_lottie import st_lottie
    
    with container:
        try:
            st_lottie(load_lottie_url(url))
        except Exception:
            pass



def image_url(image_url_id):
        return f"https://drive.google.com/uc?export=view&id={image_url_id}"


def center_button(st, text):
    st.text("")
    columns = st.columns([3, 1, 3])
    return columns[1].button(text)



def set_env_variables():
    # Set environment variables
    try:
        all_variables = open(".env", 'r', encoding='utf-8').read().strip().split("\n")

        for variable in all_variables:
            var, val = variable.split("=>")
            os.environ[var] = val
    except:
        pass



from cryptography.fernet import Fernet
import json

def get_credentials():
    credentials_encrypted = os.environ["FIREBASE_API"]
    crypto_key = os.environ["CRYPTO_KEY"]

    fernet = Fernet(crypto_key)
    credentials = fernet.decrypt(credentials_encrypted.encode()).decode()

    return json.loads(credentials)



@st.experimental_memo(ttl=constants.DATABASE_CACHE_TTL, show_spinner=False)
def get_firebase_data(outer, inner=None):
    if inner != None:
        doc_ref = constants.FIREBASE_DATABASE.collection(outer).document(inner)
        return doc_ref.get().to_dict()
    else:
        doc_ref = constants.FIREBASE_DATABASE.collection(outer)
        return {doc.id : doc.to_dict() for doc in doc_ref.stream()}


def set_firebase_data(outer, inner, data):
    doc_ref = constants.FIREBASE_DATABASE.collection(outer).document(inner)
    doc_ref.set(data)