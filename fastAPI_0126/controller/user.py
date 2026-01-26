from fastapi import APIRouter
from config.db import getconn
import mariadb

router = APIRouter(prefix="/user" ,tags=["사용자"])

print(getconn())
@router.get(path="")
# def user():
#     try:
#         conn = getconn()
#         cur = conn.cursor()
#         sql = "select * from edu.test"
#         cur.execute(sql)
#         columns = [desc[0] for desc in cur.description]
#         rows = cur.fetchall()
#         result = [dict(zip(columns, row)) for row in rows]
#         cur.close()
#         conn.close()
#         return {"status": True, "result":result}
#     except mariadb.Error as e:
#         print(f'sql오류 : {e}')
#         return {"status": False}

def user():
    try:
        conn = getconn()  # 내 db연결 정보를 conn에 넣겠다
        cur = conn.cursor() # conn으로 접속해서 
        sql = "select * from edu.test"
        cur.execute(sql)

        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        result = [dict(zip(columns,row)) for row in rows]
        cur.close()
        conn.close()
        return {"status": True, "result": result}
    except mariadb.Error as e:
        print(f"sql 오류 : {e}")
        return {"status": False}


@router.post(path="")
def user():
    return {"Hello": "World"}

@router.put(path="")
def user():
    return {"Hello": "World"}

@router.delete(path="")
def user():
    return {"Hello": "World"}


