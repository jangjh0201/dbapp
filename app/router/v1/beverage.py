from fastapi import APIRouter, Form, Request, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from app.service.beverage_service import BeverageService
from config.database import get_db
from auth.auth import manager

router = APIRouter()
templates = Jinja2Templates(directory="app/resource/templates")


@router.get("/beverage", dependencies=[Depends(manager)])
def show_all_beverages(request: Request, db: Session = Depends(get_db)):
    """
    음료 조회 API
    Args:
        request: Request 객체
        db: 데이터베이스 세션
    Returns:
        모든 음료 정보 리스트 반환 (HTML)
    """
    beverage_service = BeverageService(db)
    return templates.TemplateResponse(
        "beverage.html",
        {
            "request": request,
            "beverage_data": beverage_service.get_all(),
        },
    )


@router.post("/beverage", dependencies=[Depends(manager)])
def set_new_beverage(
    request: Request,
    name: str = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db),
):
    """
    음료 추가 API
    Args:
        name: 음료 이름
        quantity: 음료 수량
        db: 데이터베이스 세션
    Returns:
        모든 음료 정보 리스트 반환 (HTML)
    """
    beverage_service = BeverageService(db)
    beverage_service.add(name, quantity)
    return show_all_beverages(request, db)


@router.delete("/beverage/{beverage_id}", dependencies=[Depends(manager)])
def extract_beverage(beverage_id: int, db: Session = Depends(get_db)):
    """
    음료 제거 API
    Args:
        beverage_id: 음료 ID
        db: 데이터베이스 세션
    Returns:
        음료 삭제 성공 여부 (JSON)
    """
    beverage_service = BeverageService(db)
    if beverage_service.remove(beverage_id):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/beverage/{beverage_id}", dependencies=[Depends(manager)])
def refill_beverage(beverage_id: int, db: Session = Depends(get_db)):
    """
    음료 보충 API
    Args:
        beverage_id: 음료 ID
        db: 데이터베이스 세션
    Returns:
        음료 보충 성공 여부 (JSON)
    """
    beverage_service = BeverageService(db)
    if beverage_service.refill(beverage_id):
        return {"success": True}
    else:
        return {"success": False}


@router.post("/beverage/order/{beverage_id}", dependencies=[Depends(manager)])
def order_beverage(beverage_id: int, db: Session = Depends(get_db)):
    """
    음료 주문 API
    Args:
        beverage_id: 음료 ID
        db: 데이터베이스 세션
    Returns:
        음료 주문 성공 여부 (JSON)
    """
    beverage_service = BeverageService(db)
    if beverage_service.order(beverage_id):
        return {"success": True}
    else:
        return {"success": False}
