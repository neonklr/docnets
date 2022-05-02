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
    return {
        "Announcement 1": {
            "title": "Announcement 1",
            "content": "This is the first announcement",
            "date": "2020-01-01",
            "color": "yellow"
        },
        "Announcement 2": {
            "title": "Announcement 2",
            "content": "This is the Second announcement",
            "date": "2020-02-01",
            "color": "blue"
        },
        "Announcement 3": {
            "title": "Announcement 3",
            "content": "This is the Third announcement",
            "date": "2020-03-01",
            "color": "green"
        },
        "Announcement 4": {
            "title": "Announcement 4",
            "content": "This is the fourth announcement",
            "date": "2020-04-01",
            "color": "black"
        },
    }


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