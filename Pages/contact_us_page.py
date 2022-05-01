import Scripts.Utilities as Utils


def know_the_developer(st):
    Utils.website_heading(
        st,
        content="Know the developers",
        symbol="...",
        font_size=60,
        color="pink",
        text_align="center"
    )

    Utils.add_space(st)

    left, middle, right = st.columns(3)

    left.markdown(f"""
    <img src={Utils.image_url("1O8pWNFISycQZr5cKr-EdklFdlTQeQgol")} alt="jatins_image" style="width:100%; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Jatin </h2>
    """, unsafe_allow_html=True)

    middle.markdown(f"""
    <img src={Utils.image_url("1O8pWNFISycQZr5cKr-EdklFdlTQeQgol")} alt="jatins_image" style="width:100%; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Jatin </h2>
    """, unsafe_allow_html=True)

    right.markdown(f"""
    <img src={Utils.image_url("1O8pWNFISycQZr5cKr-EdklFdlTQeQgol")} alt="jatins_image" style="width:100%; border-radius: 25%;">
    <h2 style="text-align: center; margin-top: 20px; font-size: 35px"> Jatin </h2>
    """, unsafe_allow_html=True)





def show_contact_us_page(st):
    know_the_developer(st)