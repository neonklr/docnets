

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


def add_folium_map(container):
    from streamlit_folium import folium_static
    import folium

    with container:
        # center on Liberty Bell
        m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

        # add marker for Liberty Bell
        tooltip = "Liberty Bell"
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
        ).add_to(m)

        # call to render Folium map in Streamlit
        folium_static(m)


def load_lottie_url(url):
    import requests

    r = requests.get(url)
    
    if r.status_code != 200:
        return None
    
    return r.json()


def show_lottie_animation(container, url):
    from streamlit_lottie import st_lottie
    
    with container:
        st_lottie(load_lottie_url(url))



def image_url(image_url_id):
        return f"https://drive.google.com/uc?export=view&id={image_url_id}"