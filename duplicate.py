import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Angry investor")

if prompt := st.chat_input("Pitch your idea"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        placeholder = st.empty()
        response_message = ""

        for response in client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are angry investor. Give me ironic reasons why pitch is bad. be breif!",
                },
                {"role": "user", "content": prompt},
            ],
            model="gpt-4",
            stream=True,
        ):
            response_message += response.choices[0].delta.content or ""
            placeholder.markdown(response_message)
