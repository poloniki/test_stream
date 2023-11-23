import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_key"])

st.title("Angry investor")

if prompt := st.chat_input("Your pitch idea"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        placeholder = st.empty()
        message = ""
        for response in client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are angry investor. Give me ironic reaspons why this pitch is bad. Be brief.",
                },
                {"role": "user", "content": prompt},
            ],
            model="gpt-4",
            stream=True,
        ):
            message += response.choices[0].delta.content or ""
            placeholder.markdown(message)
