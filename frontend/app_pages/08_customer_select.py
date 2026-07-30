# 08_customer_select.py

import streamlit as st

from clients.customer_client import (
    customer_delete,
    customer_select,
    customer_select_all,
    customer_update,
)


st.title("Customer 조회")

customers = customer_select_all()

st.subheader("고객 전체 목록")
st.dataframe(customers, use_container_width=True)

st.subheader("고객 한 명 조회")

customer_id = st.text_input("조회할 고객 ID")

if st.button("조회"):
    selected_customer = customer_select(customer_id)
    st.json(selected_customer)

st.subheader("고객 정보 수정")

update_customer_id = st.text_input("수정할 고객 ID")
update_name = st.text_input("수정할 이름")
update_age = st.number_input(
    "수정할 나이",
    min_value=0,
    step=1,
)

if st.button("수정"):
    customer = {
        "name": update_name,
        "age": int(update_age),
    }

    result = customer_update(update_customer_id, customer)

    st.success("고객 정보가 수정되었습니다.")
    st.json(result)

st.subheader("고객 삭제")

delete_customer_id = st.text_input("삭제할 고객 ID")

if st.button("삭제"):
    result = customer_delete(delete_customer_id)

    st.success("고객 정보가 삭제되었습니다.")
    st.json(result)