import os
import sys

# 프로젝트 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.init_db import initialize_tables
from router.v1 import home, item, beverage, auth
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


class DBApp:
    def __init__(self):
        self.app = FastAPI(debug=True)
        self._initialize_app()

    def _initialize_app(self):
        # 정적 파일 설정
        self.app.mount(
            "/static", StaticFiles(directory="app/resource/static"), name="static"
        )

        # 라우터 등록
        self.app.include_router(home.router)
        self.app.include_router(beverage.router)
        self.app.include_router(item.router)
        self.app.include_router(auth.router)

        # 테이블 및 데이터베이스 초기화
        initialize_tables()

    def get_app(self) -> FastAPI:
        return self.app
