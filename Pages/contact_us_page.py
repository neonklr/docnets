import Scripts.Utilities as Utils


def show_contact_us_info(st):
    Utils.website_heading(
        st,
        content="Contact us",
        symbol="📞",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)

    columns = st.columns([1, 2, 2, 1])

    left, right = columns[1], columns[2]

    left.markdown(f"""
    <h3 style="text-align: center;"> <b> Phone </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via Email </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via LinkedIn </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via Github </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via Twitter </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via Slack </b> </h3>
    <h3 style="text-align: center;"> <b> Reach us via Discord </b> </h3>
    """, unsafe_allow_html=True)

    right.markdown(f"""
    <h3 style="text-align: center; font-weight: 200;"> +91-9888888888 </h3>
    <h3 style="text-align: center; font-weight: 200;"> name@email.com </h3>
    <h3 style="text-align: center; font-weight: 200;"> linkedin </h3>
    <h3 style="text-align: center; font-weight: 200;"> github </h3>
    <h3 style="text-align: center; font-weight: 200;"> twitter </h3>
    <h3 style="text-align: center; font-weight: 200;"> slack </h3>
    <h3 style="text-align: center; font-weight: 200;"> discord </h3>
    """, unsafe_allow_html=True)

    Utils.add_space(st)



def add_developer_details(container, name, content, color, text_align):
    for i in range(2):
        Utils.add_space(container)

    container.markdown(f"""
    <p style="font-size: 40px; border-bottom: 3px solid {color}; font-family: Euclid Circular B,Arial,Helvetica,sans-serif; font-weight: 600; text-align: {text_align}">{name}<span style="color: {color};"></span></p>
    """, unsafe_allow_html=True)

    container.markdown(f"""
    <p style="text-align: center;"> {content} </p>
    """, unsafe_allow_html=True)


def know_the_developer(st):

    left, right = st.columns([2, 1])
    right.image(Utils.image_url("19FCg1hIFRMO7mJ8789NzKJMNZpXMOId6"))
    add_developer_details(
        left, 
        "Rishaab Kalra", 
        """Student at Deenbandhu Chhotu Ram University of Science and Technology, Murthal. <br> Currently Pursing Computer Science and Engineering, CSE Honos. <br> <br> Reachout to me via the above contact us medium""",
        color="red",
        text_align="center"
    )
    
    left, right = st.columns([1, 2])
    left.image(Utils.image_url("19XLFm7jEb_fJZKbhFBZgTJH-5ZJqmill"))
    add_developer_details(
        right,
        "Jatin",
        """Student at Deenbandhu Chhotu Ram University of Science and Technology, Murthal. <br> Currently Pursing Computer Science and Engineering, CSE Honos. <br> <br> Reachout to me via the above contact us medium""",
        color="blue",
        text_align="center"
    )
    
    left, right = st.columns([2, 1])
    right.image(Utils.image_url("1IzGXU8WU4M8X2rWFcnQjqkUivN3OJJkr"))
    add_developer_details(
        left,
        "Romil",
        """Student at Deenbandhu Chhotu Ram University of Science and Technology, Murthal. <br> Currently Pursing Computer Science and Engineering, CSE Honos. <br> <br> Reachout to me via the above contact us medium""",
        color="green",
        text_align="center"
    )



def _know_the_developer(st):
    Utils.website_heading(
        st,
        content="Know the developers",
        symbol="...",
        font_size=60,
        color="goldenrod",
        text_align="center"
    )

    Utils.add_space(st)

    left, middle, right = st.columns(3)

    left.markdown(f"""
    <img src={Utils.image_url("1O8pWNFISycQZr5cKr-EdklFdlTQeQgol")} alt="team_image" style="width:100%; height: 400px; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Jatin </h2>
    """, unsafe_allow_html=True)

    middle.markdown(f"""
    <img src={Utils.image_url("1ZXvmnRHGyz9icsaeWO220EcQ-JO3Yrko")} alt="team_image" style="width:100%; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Rishaab Kalra </h2>
    """, unsafe_allow_html=True)

    right.markdown(f"""
    <img src={Utils.image_url("1a1VCeiw_QiIU-fawXaXJDRh3lsvMdt4t")} alt="team_image" style="width:100%; height: 400px; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Romil </h2>
    """, unsafe_allow_html=True)





def show_contact_us_page(st):
    show_contact_us_info(st)
    know_the_developer(st)