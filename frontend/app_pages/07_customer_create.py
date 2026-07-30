# 07_customer_create.py

import streamlit as st

from clients.customer_client import customer_create


st.title("Customer 입력")

customer_id = st.text_input("ID")
customer_pwd = st.text_input("PASSWORD", type="password")
customer_name = st.text_input("NAME")
customer_age = st.number_input(
    "AGE",
    min_value=0,
    step=1,
)

if st.button("등록"):
    customer = {
        "id": customer_id,
        "pwd": customer_pwd,
        "name": customer_name,
        "age": int(customer_age),
    }

    result = customer_create(customer)

    st.success("고객 등록이 완료되었습니다.")
    st.json(result)