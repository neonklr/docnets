from annotated_text import annotated_text
import Scripts.Utilities as Utils

def __show_single_announcement(st, announcement):
    st.markdown(f"""
    <div style="background-color: rgba(250, 202, 43, 0.2); color: "rgb(148, 124, 45)"; padding: 10px; border-radius: 10px; border: 1px solid rgba(250, 202, 43, 0.2)">
        <h1 style="text-align: center; font-weight: 600; color: rgb(148, 124, 45)"> {announcement["title"]} </h1>
        <h3 style="text-align: center; font-size: 15px; font-weight: 400; color: rgba(49, 51, 63, 0.6);"> Posted on : {announcement["date"]} </h3>
        <br>
        <h4 style="text-align: center; font-family: 'Source Code Pro', monospace"> {announcement["content"]} </h4>
    </div>
    """, unsafe_allow_html=True)
    
    Utils.add_space(st)

def show_single_announcement(st, announcement):
    Utils.website_heading(
        st,
        content=announcement["title"],
        symbol=".",
        font_size=40,
        color="orange",
        text_align="left"
    )

    st.caption("Posted on : " + announcement["date"])
    st.text(announcement["content"])

    Utils.add_space(st)
    


def show_announcements(st, announcements):
    for announcement in announcements.keys():
        show_single_announcement(st, announcements[announcement])


def get_announcements_data():
    return Utils.get_firebase_data("announcements")


def show_page_heading(st):
    Utils.website_heading(
        st,
        content="Announcements",
        symbol="📢",
        font_size=60,
        color="orange",
        text_align="center"
    )
    
    Utils.add_space(st)


def show_announcements_page(st):
    announcements = get_announcements_data()
    show_page_heading(st)
    show_announcements(st, announcements)