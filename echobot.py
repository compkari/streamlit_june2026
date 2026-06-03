# 1st iteration - create chat msg box
# import streamlit as st

# with st.chat_message("user"):
#    st.write("Hello 👋")

# 2nd iteration - print msg
# import streamlit as st
# import numpy as np

# with st.chat_message("assistant"):
#    st.write("Hello human")
#    st.bar_chart(np.random.randn(30, 3))

# 3rd iteration - input and capture msg
# import streamlit as st

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")

#4 iteration - integrate both user prompt and response echo  
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input - echo users input message
if prompt := st.chat_input("Dude, tell me something!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

