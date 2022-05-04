import Scripts.Utilities as Utils
from Scripts.data_loader import get_doctors_data, get_users_data

def top_header(st):
    left, right = st.empty().columns(2)

    # first header
    Utils.website_heading(
        left,
        content="Doctor is a designation where passion and profession co-exist",
        symbol=".",
        font_size=55,
        color="blue"
    )
    
    right.image("https://soffront.com/wp-content/uploads/2020/11/healthcare1.png", use_column_width=True)


def second_header_util(container, icon, heading, content):
    container.markdown(f"""
    <div id="symbol"><i class="material-icons" style="font-size: 60px;">{icon}</i></div>
    <h3 class="lg:mt-2 lg:mb-3" style="color: goldenrod;">{heading}</h3>
    <p><b>{content}<b><p>
    """, unsafe_allow_html=True)
    
    
    # container.markdown(f"""
    # <div id="symbol">{icon}</div>
    # <h3 class="lg:mt-2 lg:mb-3" style="color: goldenrod;">{heading}</h3>
    # <p><b>{content}<b><p>
    # """, unsafe_allow_html=True)


def second_header(st):
    Utils.website_heading(
        st,
        content="DocNets, An easy-to-use appointment scheduling app for a patient with a doctor",
        symbol=".",
        font_size=60,
        color="green",
        text_align="center"
    )

    Utils.add_space(st)

    st.markdown("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    """, unsafe_allow_html=True)

    left, middle, right = st.empty().columns(3)

    second_header_util(left, icon="free_cancellation", heading="Easy and Quick Appointment Scheduling", content="Book a non-clashing appointment with a doctor of your choice, in just a few simple steps. Visit out 'Book An Appointment' page to know more")
    second_header_util(middle, icon="pin_drop", heading="Availability of Doctor based on Location", content="You can find the doctors based on their location, and make yourself comfortable with whichever location suits you best")
    second_header_util(right, icon="sort",heading="Sort the Doctors based on your needs", content="Not just locations, we provide a variety of variables for you to select whichever factor you need the most, wether it be fees or experience, we value your choice")

    Utils.add_space(st)

    left, middle, right = st.empty().columns(3)

    second_header_util(left, icon="pending_actions", heading="Enjoy seemless Real Time Scheduling", content="Enjoy seemless easy-to-use real time booking of your appointment. No need to worry about other ends, we take care of it")
    second_header_util(middle, icon="contact_support", heading="Have any Problem? worry not we have FAQs Section", content="If you feel stuck or have any problem, just visit our FAQs section for answers to some of our most common questions... Still Stuck? Visit our contact us page and reach out to us")
    second_header_util(right, icon="travel_explore", heading="Use our easy to view Maps for location understandings", content="We also provide an easy-to-view instant maps for all our location services. This helps you as a user to have a quick view of the surrounding terrains of your appointment destination")



def third_header(st):
    Utils.website_heading(
        st,
        content="Supporting connection between Doctors and Patients from all over the world",
        symbol=".",
        font_size=60,
        color="red",
        text_align="center"
    )

    Utils.add_space(st)

    # import pandas as pd
    # import numpy as np

    # df = pd.DataFrame(
    #     np.random.randint(-90, 90, (200, 2)),
    #     columns=['lat', 'lon']
    # )

    # st.map(df)

    locations, names = [], []
    doc_data = get_doctors_data()
    user_data = get_users_data()

    for doc in doc_data.values():
        locations.append(doc["location"])
        names.append("{} @Doctor".format(doc["name"]))

    for user in user_data.values():
        locations.append(user["location"])
        names.append("{} @User".format(user["name"]))

    Utils.add_folium_map(
        None,
        locations=locations,
        doc_names=names,
        width=1200,
        zoom_start=2
    )


def fourth_header(st):
    Utils.website_heading(
        st,
        content="What do we provide",
        symbol="?",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)



    left, right = st.empty().columns(2)

    Utils.show_lottie_animation(left, url="https://assets4.lottiefiles.com/packages/lf20_ibbakwps.json")
    for i in range(2):
        Utils.add_space(right)
    Utils.website_heading(
        right,
        content="Easy and Quick Appointment Scheduling",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    right.markdown("""
    <p> An Easy to Use and Fast Responding Appointment Scheduling System.  Books conflicts free appointments and gives user-friendly error messages if something is wrong.</p>
    """, unsafe_allow_html=True)



    left, right = st.empty().columns(2)

    Utils.show_lottie_animation(right, url="https://assets10.lottiefiles.com/packages/lf20_go0wc4l3.json")
    Utils.add_space(left)
    Utils.website_heading(
        left,
        content="Enjoy Seemless Real Time Scheduling",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    left.markdown("""
    <p>Multiple Users can interact with booking system at the same time !   No Conflicts can occur in scheduling.</p>
    """, unsafe_allow_html=True)



    left, right = st.empty().columns(2)

    Utils.show_lottie_animation(left, url="https://assets5.lottiefiles.com/packages/lf20_vPnn3K.json")
    for i in range(4):
        Utils.add_space(right)
    Utils.website_heading(
        right,
        content="Sort the Doctors based on your needs",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    right.markdown("""
    <p>Too many doctors to choose from? Sort them out based on their Experience, Fees or any other criteria you want  !  Easy to work with as you just have to click on desired column</p>
    """, unsafe_allow_html=True)




def show_home_page(st):

    top_header(st)
    Utils.add_space(st)

    second_header(st)
    Utils.add_space(st)

    third_header(st)
    Utils.add_space(st)

    fourth_header(st)
    Utils.add_space(st)