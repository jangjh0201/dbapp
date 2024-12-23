from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from config.database import get_db
from service.item_service import ItemService
from security.auth import manager

router = APIRouter()
templates = Jinja2Templates(directory="app/resource/templates")


@router.get("/item", dependencies=[Depends(manager)])
def show_all_items(request: Request, db: Session = Depends(get_db)):
    """
    물품 조회 API
    Args:
        request: Request 객체
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환 (HTML)
    """
    item_service = ItemService(db)
    return templates.TemplateResponse(
        "item.jinja2", {"request": request, "item_data": item_service.get_all()}
    )


@router.post("/item", dependencies=[Depends(manager)])
def set_new_item(
    request: Request, name: str = Form(...), db: Session = Depends(get_db)
):
    """
    물품 추가 API
    Args:
        name: 물품 이름
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환 (HTML)
    """
    item_service = ItemService(db)
    item_service.add(name)
    return show_all_items(request, db)


@router.delete("/item/{item_id}", dependencies=[Depends(manager)])
def eliminate_item(item_id: int, db: Session = Depends(get_db)):
    """
    물품 삭제 API
    Args:
        item_id: 물품 ID
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    if item_service.remove(item_id):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/item/{item_id}/name", dependencies=[Depends(manager)])
def rename_item(item_id: int, name: str = Form(None), db: Session = Depends(get_db)):
    """
    물품 수정 API
    Args:
        item_id: 물품 ID
        name: 물품 이름
        is_stored: 물품 보유 여부
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    if item_service.rename(item_id, name):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/item/{item_id}/use", dependencies=[Depends(manager)])
def use_item(item_id: int, db: Session = Depends(get_db)):
    """
    물품 사용 API
    Args:
        item_id: 물품 ID
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    if item_service.use(item_id):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/item/{item_id}/keep", dependencies=[Depends(manager)])
def keep_item(item_id: int, db: Session = Depends(get_db)):
    """
    물품 보관 API
    Args:
        item_id: 물품 ID
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    if item_service.store(item_id):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/ai/{name}/use")
def ai_use_item(name: str, db: Session = Depends(get_db)):
    """
    물품 사용 AI API
    Args:
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    item_id = item_service.get_id(name)
    if item_service.use(item_id):
        return {"success": True}
    else:
        return {"success": False}


@router.put("/ai/{name}/keep")
def ai_keep_item(name: str, db: Session = Depends(get_db)):
    """
    물품 보관 AI API
    Args:
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    item_id = item_service.get_id(name)
    if item_service.store(item_id):
        return {"success": True}
    else:
        return {"success": False}


@router.post("/ai/all/use")
def ai_use_all_items(db: Session = Depends(get_db)):
    """
    모든 물품 사용 AI API
    Args:
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    for item in item_service.get_all():
        item_service.use(item["id"])
    return {"success": True}


@router.post("/ai/remain/keep")
def ai_keep_remain_items(db: Session = Depends(get_db)):
    """
    남은 물품 보관 AI API
    Args:
        db: 데이터베이스 세션
    Returns:
        모든 물품 정보 리스트 반환
    """
    item_service = ItemService(db)
    for item in item_service.get_all():
        if not item["storage"]:
            item_service.store(item["id"])
    return {"success": True}
