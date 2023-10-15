import streamlit as st
import time
from pathlib import Path

st.title("Auto-Consultant")

# TEMP
def agent(prompt):
    time.sleep(1)
    return "Hi."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    assistant_response_first = "Hi, I'm your Auto-Consultant. I can help you understand your data and make business decisions. What would you like me to do?"
    st.session_state.messages.append({"role": "assistant", "content": assistant_response_first})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("How can I help?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    # TODO: call agent using user input
    response = agent(prompt)


    continue_string = "Continue"
    if response != continue_string:
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        # ?? how to continue ??
        pass


