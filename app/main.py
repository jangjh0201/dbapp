
from database.database import SessionLocal
from controller.auth_controller import router as auth_router
from controller.manager_controller import router as manager_router
from controller.user_controller import router as user_router
import sys
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

# 프로젝트 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = FastAPI()

# 정적 파일 설정
app.mount("/static", StaticFiles(directory="app/resource/static"), name="static")

# 유저, 매니저 및 인증 라우터 등록
app.include_router(user_router)
app.include_router(manager_router)
app.include_router(auth_router)

# 데이터베이스 세션
db = SessionLocal()


# 테스트용 데이터 추가
def add_test_data(db: Session):
    return None


# 테스트 데이터 추가
add_test_data(db)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
