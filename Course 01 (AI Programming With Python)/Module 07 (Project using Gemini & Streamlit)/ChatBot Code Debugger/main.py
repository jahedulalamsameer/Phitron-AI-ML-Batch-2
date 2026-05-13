import streamlit as st
from PIL import Image
from app_backend import generate_response

st.header("AI Code Debugger")
st.divider()

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("image"):
            col = st.columns(len(message["image"]))
            for i,img in enumerate(message["image"]):
                with col[i]:
                    st.image(img)
        


if queries := st.chat_input("Share your problem with Gemma",accept_file="multiple",file_type=["jpg","jpeg","png"]):

    pil_images = [Image.open(img) for img in queries.files] if queries.files else []
    st.session_state["message_history"].append({"role":"User","content":queries.text,"image":pil_images})
    prompt = [img for img in pil_images] if pil_images else []
    


    with st.chat_message("User"):
        if pil_images:
            st.image(pil_images)
        if queries.text:
            st.markdown(queries.text)
            prompt.append(queries.text)
        

    if prompt:
        col1, col2 = st.columns(2, gap="xxsmall")
        st.text("Choose an option")
        with col1:
            button1 = st.button("Hint")
        with col2:
            button2 = st.button("Solution")
            
        
    with st.chat_message("Assistant"):
        with st.spinner("Working..."):
            if button1:
                prompt.append("provide hints only")
                response = generate_response(prompt)
                st.session_state["message_history"].append({"role":"Assistant","content":response.text})
                st.markdown(response.text)

            elif button2:
                prompt.append("provide solution to the problem")
                response = generate_response(prompt)
                st.session_state["message_history"].append({"role":"Assistant","content":response.text})
                st.markdown(response.text)
