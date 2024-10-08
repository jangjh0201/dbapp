import sys
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database.database import initialize_tables, SessionLocal

# 프로젝트 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# 정적 파일 설정
app.mount("/static", StaticFiles(directory="app/resource/static"), name="static")

# 테이블 및 데이터베이스 설정
initialize_tables()

# 데이터베이스 세션
db = SessionLocal()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
