# customer_service.py

from app.schemes.customer_scheme import (
    CustomerCreate,
    CustomerPublic,
    CustomerUpdate,
)


# 1. 고객 등록
def customer_create(customer: CustomerCreate) -> CustomerPublic | None:
    # Database에 고객 정보 입력
    return CustomerPublic(
        id=customer.id,
        name=customer.name,
        age=customer.age,
    )


# 2. 고객 전체 조회
def customer_select_all() -> list[CustomerPublic]:
    # Database에서 전체 고객 조회
    return [
        CustomerPublic(
            id="id01",
            name="홍길동",
            age=30,
        ),
        CustomerPublic(
            id="id02",
            name="김철수",
            age=25,
        ),
        CustomerPublic(
            id="id03",
            name="김영희",
            age=20,
        ),
        CustomerPublic(
            id="id04",
            name="문수지",
            age=27,
        ),
        CustomerPublic(
            id="id05",
            name="박민수",
            age=32,
        ),
    ]


# 3. 고객 한 명 조회
def customer_select(customer_id: str) -> CustomerPublic | None:
    # Database에서 고객 한 명 조회
    return CustomerPublic(
        id=customer_id,
        name="홍길동",
        age=30,
    )


# 4. 고객 정보 수정
def customer_update(
    customer_id: str,
    customer: CustomerUpdate,
) -> CustomerPublic | None:
    # Database에서 customer_id에 해당하는 고객 정보 수정
    return CustomerPublic(
        id=customer_id,
        name=customer.name,
        age=customer.age,
    )


# 5. 고객 삭제
def customer_delete(customer_id: str) -> bool:
    # Database에서 customer_id에 해당하는 고객 삭제
    return True