# customer_scheme.py

from pydantic import BaseModel

# 고객 등록
class CustomerCreate(BaseModel):
    id: str
    pwd: str
    name: str
    age: int

# 고객 수정
class CustomerUpdate(BaseModel):
    pwd: str
    name: str
    age: int

# 고객 정보 응답
class CustomerPublic(BaseModel):
    id: str
    name: str
    age: int