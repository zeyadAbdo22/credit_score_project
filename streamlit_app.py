# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Credit Score Calculator")
st.title("Credit Score Calculator")

user_id = st.number_input(" Enter user ID ", min_value=1, step=1)

if st.button("summit"):
    try:
        response = requests.get(f"http://localhost:8000/calculate_score/{user_id}")
        if response.status_code == 200:
            result = response.json()
            st.success(f"Final Score: {result['final_score']}")
            st.write(result)
        else:
            st.error(f"Erorr: {response.text}")
    except Exception as e:
        st.error(f"HTTPException: {e}")