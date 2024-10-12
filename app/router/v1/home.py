from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

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
    return templates.TemplateResponse("index.jinja2", {"request": request})
