
import sys
import os
from app.router.v1 import drawer
from utils.init_db import initialize_tables
from router.v1 import home, beverage, auth
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# 프로젝트 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    debug=True
)

# 정적 파일 설정
app.mount("/static", StaticFiles(directory="app/resource/static"), name="static")

# 라우터 등록
app.include_router(home.router)
app.include_router(beverage.router)
app.include_router(drawer.router)
app.include_router(auth.router)

# 테이블 및 데이터베이스 초기화
initialize_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
