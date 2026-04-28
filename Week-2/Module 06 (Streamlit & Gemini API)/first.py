import streamlit as st

# Text or form input
with st.form("Fill the form", enter_to_submit=False):
    name = st.text_input("Name",placeholder="Type your name")
    age = st.number_input("Age",value=None,placeholder="Type your age")
    profession = st.selectbox("Profession",["Student","Employee","Businessman","Service Holder","Freelancer"],index=None,placeholder="Choose your profession")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and age and profession:
            st.success("Form submitted successfully")
            st.markdown(f"Name-{name.strip().lower().title()}, Age-{age:.0f}, & Profession-{profession}")
        else:
            st.warning("Fill all the sections")
    else:
        st.error("Fill the form and submit properly")

# Image input
images = st.file_uploader("Enter images",accept_multiple_files=True,type=("jpg","jpeg","png"))

if len(images) == 3:
    cols = st.columns(len(images))
    for i, img in enumerate(images):
        cols[i].image(img,width="stretch")
elif len(images) > 3:
    st.error("Too many images")
else:
    st.warning("Input at least three images")

# Text
text = st.text_input("Enter a text")

if text:
    st.title(text,anchor=False)
    st.divider()
    st.header(text,anchor=False)
    st.divider()
    st.subheader(text,anchor=False)
    st.divider()
    st.text(text)