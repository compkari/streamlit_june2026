# 1st
# import streamlit as st

# with st.chat_message("user"):
#    st.write("Hello 👋")

# 2nd
# import streamlit as st
# import numpy as np

# with st.chat_message("assistant"):
#    st.write("Hello human")
#    st.bar_chart(np.random.randn(30, 3))

# 3rd
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
