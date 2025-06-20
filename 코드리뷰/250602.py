# 1. 짝수 제곱 리스트 구하기
'''
[ 조건 ]
n은 1 이상 자연수,
리스트 컴프리헨션을 이용하여 작성,
return 형식: 짝수들의 제곱 리스트,
# 예시 입력
n = 10
# 예시 출력
[4, 16, 36, 64, 100]'''


def solution(n):
    return [i**2 for i in range(1, n+1) if i % 2 ==0]





# 2. 사용자 등록 API 만들기

'''
[ 조건 ]df
Pydantic의 BaseModel을 사용하여 사용자 입력을 검증,
POST 요청으로 사용자 데이터를 받으면, 다음과 같은 응답을 JSON으로 반환,'''
{"message": "홍길동님, 등록이 완료되었습니다."}

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = [
    {"name": "홍길동", "age": 25},
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]

@app.get("/users", response_model=List[User])
def get_users(min_age: int):
    filtered_users = [user for user in users if user["age"] >= min_age]
    return filtered_users






# 3. 나이로 사용자 필터링 API,
'''
[ 조건 ]
사용자 정보는 서버 내에서 고정된 리스트로 관리 (DB 없이 in-memory),
/users?min_age=30처럼 쿼리 파라미터로 나이 기준을 입력받기,
min_age 이상인 사용자들의 리스트를 반환'''



# 내부 사용자 데이터
[
    {"name": "홍길동", "age": 25},
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]

# GET /users?min_age=30
# Response:
[
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def register_user(user: User):
    return {"message": f"{user.name}님, 등록이 완료되었습니다."}