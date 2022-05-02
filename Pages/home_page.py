import Scripts.Utilities as Utils


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
    <div id="symbol">{icon}</div>
    <h3 class="lg:mt-2 lg:mb-3">{heading}</h3>
    <p>{content}<p>   
    """, unsafe_allow_html=True)


def second_header(st):
    Utils.website_heading(
        st,
        content="An easy-to-use appointment scheduling app for doctors",
        symbol=".",
        font_size=60,
        color="green",
        text_align="center"
    )

    Utils.add_space(st)

    left, middle, right = st.empty().columns(3)

    second_header_util(left, icon="", heading="Create your custom Booking Page", content="Minimize the time it takes for patients to schedule an appointment. Enable easy online self-booking with your specialists.")
    second_header_util(middle, icon="", heading="Display availability for all staff", content="Add individual profiles for your practice’s doctors. Direct patients to the appropriate consultant and streamline booking.")
    second_header_util(right, icon="", heading="Minimize missed appointments", content="Automate text and email reminders for every booking. Patients can also reschedule directly from their confirmations.")

    left, middle, right = st.empty().columns(3)

    second_header_util(left, icon="", heading="View your schedule on-the-go", content="Stay updated when away from your clinic. Get instant notifications with the Setmore mobile app for iOS and Android devices.")
    second_header_util(middle, icon="", heading="Set up recurring follow-ups", content="Establish full treatment plans and book multiple appointments in advance with your doctor appointment software.")
    second_header_util(right, icon="", heading="Offer a modern medicine experience", content="Book and host video appointments to reach patients where they’re comfortable. Your Setmore app connects with Teleport and Zoom.")



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

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        np.random.randint(-90, 90, (200, 2)),
        columns=['lat', 'lon']
    )

    st.map(df)


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
        content="Provide secure virtual medical consultations",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    right.markdown("""
    <p>Meet with your patients online via telemedicine appointments. Discuss their concerns and establish treatment plans remotely, using Setmore’s Zoom or Teleport integrations. Your online doctor appointment booking system offers added privacy, enabling you to lock video calls when discussing sensitive patient data.</p>
    """, unsafe_allow_html=True)



    left, right = st.empty().columns(2)

    Utils.show_lottie_animation(right, url="https://assets10.lottiefiles.com/packages/lf20_go0wc4l3.json")
    Utils.add_space(left)
    Utils.website_heading(
        left,
        content="Store up-to-date patient information",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    left.markdown("""
    <p>A patient's Customer Profile automatically updates when they book an appointment. Centralize contact information and attach notes for fast access before appointments. Your online doctor scheduling app allows you to digitally back-up patient health records and treatment recommendations.</p>
    """, unsafe_allow_html=True)



    left, right = st.empty().columns(2)

    Utils.show_lottie_animation(left, url="https://assets5.lottiefiles.com/packages/lf20_vPnn3K.json")
    for i in range(4):
        Utils.add_space(right)
    Utils.website_heading(
        right,
        content="Accept medical fees online",
        symbol=".",
        font_size=40,
        color="blue",
        text_align="left"
    )
    right.markdown("""
    <p>Minimize invoicing time by integrating Setmore with Stripe , Square or PayPal. Your practice is able to accept secure online payments, directly from your Booking Page. Bill patients for consultations or treatments in advance with a convenient, contactless payment gateway.</p>
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