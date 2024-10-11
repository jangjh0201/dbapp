from datetime import datetime
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from config.database import get_db
from service import item_service
from auth.auth import manager
import io
import base64

router = APIRouter()
templates = Jinja2Templates(directory="app/resource/templates")


@router.get("/stock", dependencies=[Depends(manager)])
def show_inventory(request: Request, db: Session = Depends(get_db)):
    """
    재고 조회 API
    Args:
        request: Request 객체
        db: 데이터베이스 세션
    Returns:
        모든 재고 정보 리스트 반환 (HTML)
    """
    item_service = item_service()
    ice_creams, toppings, consumables = item_service.get_all_inventories(db)
    return templates.TemplateResponse(
        "stock.html",
        {
            "request": request,
            "inventory_data": {
                "ice_cream": ice_creams,
                "topping": toppings,
                "consumable": consumables,
            },
        },
    )


@router.get("/item", dependencies=[Depends(manager)])
def show_item(request: Request, db: Session = Depends(get_db)):
    """
    아이템 조회 API
    Args:
        request: Request 객체
        db: 데이터베이스 세션
    Returns:
        모든 아이템 정보 리스트 반환 (HTML)
    """
    ice_creams, toppings, consumables = item_service.get_all_items(db)
    return templates.TemplateResponse(
        "item.html",
        {
            "request": request,
            "ice_creams": ice_creams,
            "toppings": toppings,
            "consumables": consumables,
        },
    )


@router.post("/item", dependencies=[Depends(manager)])
def add_item(
    request: Request,
    item_type: str = Form(...),
    item_name: str = Form(...),
    item_price: int = Form(...),
    item_quantity: int = Form(...),
    db: Session = Depends(get_db),
):
    """
    아이템 추가 API
    Args:
        item_type: 아이템 타입
        item_name: 아이템 이름
        item_price: 아이템 가격
        item_quantity: 아이템 수량
        db: 데이터베이스 세션
    Returns:
        모든 아이템 정보 리스트 반환 (JSON)
    """
    item_service.add_item(item_type, item_name, item_price, item_quantity, db)
    return item_service.get_all_items(db)


@router.delete("/item/{item_type}/{item_id}", dependencies=[Depends(manager)])
def remove_item(item_type: str, item_id: int, db: Session = Depends(get_db)):
    """
    아이템 삭제 API
    Args:
        item_type: 아이템 타입
        item_id: 아이템 ID
        db: 데이터베이스 세션
    Returns:
        아이템 삭제 성공 여부 (JSON)
    """
    if item_service.remove_item(item_type, item_id, db):
        return {"success": True}
    else:
        return {"success": False}
