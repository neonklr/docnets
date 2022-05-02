import Scripts.Utilities as Utils
from Scripts.doctor import filter_docs
from Scripts.constants import *
import json

def show_map(container, data):
    all_docs = filter_docs("specialization", data, reload=True)

    with open(DOCTORS_FILE_PATH, 'r') as file:
        doc_database = json.load(file)

    locations, doc_names = [], []

    for doc in all_docs:
        locations.append(doc_database[doc]["location"])
        doc_names.append(doc_database[doc]["name"])

    Utils.add_folium_map(
        container=container,
        locations=locations,
        doc_names=doc_names,
        width = 1200,
        zoom_start=2
    )



def show_info(st, datas):
    index = 0
    for data in datas.keys():
        
        columns = st.columns(2)

        if index % 2 == 0:
            left, right = columns
        else:
            right, left = columns

        Utils.add_space(right)

        Utils.website_heading(
            right,
            content=data,
            symbol=".",
            font_size=40,
            color="goldenrod",
            text_align="center"
        )

        Utils.add_space(left)

        left.markdown(f"""
        <img src="{datas[data]["image_url"]}" alt="image" style="width:75%; margin-left: 12.5%; border-radius: 5%;">
        """, unsafe_allow_html=True)

        Utils.add_space(left)


        right.markdown(f"""
        <br><p style=""> {datas[data]["content"]} </p><br><br>
        """, unsafe_allow_html=True)

        show_map(None, data)

        index += 1

def get_data():

    # TODO :- get data in real-time
    
    return {
        "General Medicine" : {
            "image_url": "https://wp02-media.cdn.ihealthspot.com/wp-content/uploads/sites/494/2019/10/26213210/Doctor-Specialty-Spotlight.jpg",
            "content": "General Physicians are highly trained specialists who provide a range of non-surgical health care to adult patients. They care for difficult, serious or unusual medical problems and continue to see the patient until these problems have resolved or stabilised."
        },

        "ENT": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJZCrGQqV32LdG2iT8wYFWUredoyv-AGdFUA&usqp=CAU",
            "content": "ENT specialists are not only medical doctors who can treat your sinus headache, your child’s swimmer’s ear, or your dad’s sleep apnea. They are also surgeons who can perform extremely delicate operations to restore hearing of the middle ear, open blocked airways, remove head, neck, and throat cancers, and rebuild these essential structures."
        },

        "Gynaecology": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFhU7JFRByxjAl1WViQ-H21oW4YOEXIXKKoQ&usqp=CAU",
            "content": "A gynaecologist is a doctor that heads or is a part of the gynaecology department and cures diseases of reproductive organs of women and provides cures for them."
        },

        "Pediatrics": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXQPo5BAD-Hmqj4-tAbdKfUY9JJifkNlh1hQ&usqp=CAU",
            "content": "Our paediatric division also diagnoses and treats cardiac issues in new-borns and foetuses alike. The Department has an ensemble of top cardiologists in India with advanced technology and the best practices in Non-invasive cardiology, Interventional Cardiology, Electrophysiology and Paediatric Cardiology."
        },

        "Dermatology": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsrDdceOLH7mEWPzjp7Lw2xt-01Lou8QYjpg&usqp=CAU",
            "content": "Dermatologists are medical practitioners who specialize in treating conditions of the skin, most commonly acne, sunburn, and skin cancer. Dermatological duties include taking consultations, providing screening tests, and undertaking non-invasive surgical procedures."
        },

        "Orthopedics": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuq1N17XMKUQJdDvrwgm3yL6WEhIauPP607g&usqp=CAU",
            "content": "The Orthopaedic and Joint Replacement department specialises in arthroscopy, dealing with trauma recovery, spinal injuries and complicated joint replacement, are performed here to make sure that you derive maximum bone and joint health under our care. With an efficient line-up of leading orthopaedic doctors from around the country, we offer dedicated treatments in all minor and major osteoarthritic issues. One of our leading treatment modules includes platelet-rich plasma transfusion for patient with osteoarthritis. Our treatments involve minimally invasive surgeries for trauma recovery or even bone restructuring. Our team of anaesthesiologists, rheumatologists and rehabilitation experts are here to make your recovery smooth and rapid. Treatments Offered: ACL reconstruction, Ankle-brachial index, Arthoscopy, Cortisone shots, Diskectomy"
        },

        "Cardiology": {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgyt_JHdJmizyzjYriNMPxOG-WzyOufEwq4A&usqp=CAU",
            "content": "The Cardiology Department provides the best of services in terms of accurate diagnosis and professional treatment. The experienced team of doctors specialises in cardiac by-pass surgery, minimally invasive surgery, interventional cardiology, and non-invasive cardiology. We also provide ambulatory systems for emergencies along with non-invasive image processing, echocardiography, stress tests, cardiovascular CT’s and thallium heart mapping among many others."
        },

        "Gastroenterologists": {
            "image_url": "https://images.medicinenet.com/images/article/main_image/gastroenterologist.jpg",
            "content": "we provide comprehensive Gastroenterology and Hepatology services. This is backed by excellent endoscopy unit, radiology, histopathology services, surgical backup and ITU care. We believe in a team and multidisciplinary approach towards patient care. We have state-of-the-art endoscopic instruments (Olympus) and we perform diagnostic and therapeutic endoscopies including: Endoscopic treatment of GI bleeding, Difficult ERCP procedures, Dilatation of oesophageal stricture, Dilatation of achalasia"
        }
    }


def show_page_heading(st):
    Utils.website_heading(
        st,
        content="Know our services and corresponding doctors around the world",
        symbol="📍",
        font_size=60,
        color="blue",
        text_align="center"
    )

    Utils.add_space(st)


def show_city_map_page(st):
    data = get_data()
    show_page_heading(st)
    show_info(st, data)