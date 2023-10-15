import streamlit as st
import time
from pathlib import Path

st.title("Auto-Consultant")

path = (Path(__file__).parent.parent.parent / "./logs_1/agent_log/main_log").resolve()
if path.exists():
    content = path.read_text()

    # split on \n "Step #:" where # is a number
    split_seq = "\nStep "
    split = content.split(split_seq)

    # prepend split_seq to each element except the first
    split = [split[0]] + [split_seq + s for s in split[1:]]

    # for s in split:
    #     st.write(s, unsafe_allow_html=True)

    st.session_state.messages = []
    for s in split:
        st.session_state.messages.append({"role": "assistant", "content": s})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
else:
    st.write("No log found.")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

#     st.session_state.messages.append({"role": "assistant", "content": assistant_response_first})

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
