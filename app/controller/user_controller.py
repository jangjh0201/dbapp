from fastapi import APIRouter, Request, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from database.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/resource/templates")


@router.get("/")
def show_home(request: Request):
    """
    홈 페이지 반환 API
    Args:
        request: Request 객체
    Returns:
        홈 페이지 반환 (HTML)
    """
    return templates.TemplateResponse("index.html", {"request": request})
