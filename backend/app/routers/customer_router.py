# customer_router.py

from fastapi import APIRouter

from app.schemes.customer_scheme import (
    CustomerCreate,
    CustomerPublic,
    CustomerUpdate,
)
from app.services.customer_service import (
    customer_create,
    customer_delete,
    customer_select,
    customer_select_all,
    customer_update,
)


customer_router = APIRouter(
    prefix="/customers",
    tags=["Customer"],
)


# 1. 고객 등록
@customer_router.post("", response_model=CustomerPublic)
def create_customer(customer: CustomerCreate):
    return customer_create(customer)


# 2. 고객 전체 조회
@customer_router.get("", response_model=list[CustomerPublic])
def select_all_customers():
    return customer_select_all()


# 3. 고객 한 명 조회
@customer_router.get("/{customer_id}", response_model=CustomerPublic)
def select_customer(customer_id: str):
    return customer_select(customer_id)


# 4. 고객 정보 수정
@customer_router.put("/{customer_id}", response_model=CustomerPublic)
def update_customer(
    customer_id: str,
    customer: CustomerUpdate
):
    return customer_update(customer_id, customer)


# 5. 고객 삭제
@customer_router.delete("/{customer_id}", response_model=bool)
def delete_customer(customer_id: str):
    return customer_delete(customer_id)