from Scripts.data_saver import add_new_person
from Scripts.login import login

def show_login_form(login_form):
    login_form.markdown("""
    <h1 style="text-align: center;">Please login...</h1>
    """, unsafe_allow_html=True)

    username = login_form.text_input("Please enter your username")
    password = login_form.text_input("Please enter your password", type="password")
    i_am_a = login_form.radio("Please define yourself", ["I am a user", "I am a doctor"])

    info_box = login_form.empty()

    if login_form.button("Login"):
        try:
            login(username, password, i_am_a == "I am a doctor")
            info_box.warning("Successfully logged in")
        except Exception as e:
            info_box.warning(str(e))


def show_register_form(register_form): 
    register_form.markdown("""
    <h1 style="text-align: center;">Please Register...</h1>
    """, unsafe_allow_html=True)
    
    username = register_form.text_input("Please enter your username")
    password = register_form.text_input("Please enter your password", type="password")
    i_am_a = register_form.radio("Please define yourself", ["I am a user", "I am a doctor"])

    if i_am_a == "I am a doctor":

        data = {
            "name": register_form.text_input("Please enter your name"),
            "email": register_form.text_input("Please enter your email"),
            "fees": register_form.number_input("Please enter your fees", value=100, step=100),
            "phone": register_form.number_input("Please enter your phone number", value=0, step=1, max_value=10**11-1),
            "location": list(map(float, register_form.text_input("Please enter your location coordinates (space seperated)").split())),
            "specialization": register_form.text_input("Please enter your specialization"),
            "experience": register_form.number_input("Please enter your experience", value=0.0, step=0.1),
        }
        
    elif i_am_a == "I am a user":
        data = {
            "name": register_form.text_input("Please enter your name")
        }
        
    info_box = register_form.empty()

    if register_form.button("Register"):
        if i_am_a == "I am a doctor":
            if not (username and password and all(data.values())):
                info_box.warning("Please fill all the fields")
            else:
                try:
                    add_new_person(username, password, data)
                    info_box.success("Successfully registered")

                except Exception as e:
                    info_box.warning("Username already exists")

        else:
            if not (username and password and data["name"]):
                info_box.warning("Please fill all the fields")
            else:
                try:
                    add_new_person(username, password, data)
                    info_box.success("Successfully registered")

                except Exception as e:
                    info_box.warning("Username already exists")



def show_my_account_page(st):
    container = st.columns([1, 2, 1])[1]
    value = container.selectbox("", ["Login", "Register"])

    if value == "Login":
        show_login_form(container)
        
    elif value == "Register":
        show_register_form(container)