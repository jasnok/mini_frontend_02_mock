# customer_client.py
# customer CRUD

from core.api_client import request


# 1. 고객 등록
def customer_create(customer: dict):
    return request("POST", "/customers", json=customer)


# 2. 고객 삭제
def customer_delete(customer_id: str):
    return request("DELETE", f"/customers/{customer_id}")


# 3. 고객 수정
def customer_update(customer_id: str, customer: dict):
    return request(
        "PUT",
        f"/customers/{customer_id}",
        json=customer,
    )


# 4. 고객 전체 조회
def customer_select_all():
    return request("GET", "/customers")


# 5. 고객 한 명 조회
def customer_select(customer_id: str):
    return request("GET", f"/customers/{customer_id}")