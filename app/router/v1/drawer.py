from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from config.database import get_db
from service.drawer_service import DrawerService
from auth.auth import manager

router = APIRouter()
templates = Jinja2Templates(directory="app/resource/templates")


@router.get("/drawer", dependencies=[Depends(manager)])
def show_all_items(request: Request, db: Session = Depends(get_db)):
    """
    물건 조회 API
    Args:
        request: Request 객체
        db: 데이터베이스 세션
    Returns:
        모든 물건 정보 리스트 반환 (HTML)
    """
    drawer_service = DrawerService(db)
    return templates.TemplateResponse(
        "drawer.html",
        {
            "request": request,
            "drawer_data": drawer_service.get_all(),
        },
    )


@router.post("/drawer", dependencies=[Depends(manager)])
def set_new_item(
    request: Request,
    name: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    물건 추가 API
    Args:
        name: 물건 이름
        db: 데이터베이스 세션
    Returns:
        모든 물건 정보 리스트 반환 (HTML)
    """
    drawer_service = DrawerService(db)
    drawer_service.add(name)
    return show_all_items(request, db)


@router.delete("/drawer/{item_id}", dependencies=[Depends(manager)])
def delete_item(
    request: Request,
    item_id: int,
    db: Session = Depends(get_db),
):
    """
    물건 삭제 API
    Args:
        item_id: 물건 ID
        db: 데이터베이스 세션
    Returns:
        모든 물건 정보 리스트 반환 (HTML)
    """
    drawer_service = DrawerService(db)
    drawer_service.delete(item_id)
    return show_all_items(request, db)


@router.put("/drawer/{item_id}", dependencies=[Depends(manager)])
def update_item(
    request: Request,
    item_id: int,
    name: str = Form(None),
    is_stored: bool = Form(None),
    db: Session = Depends(get_db),
):
    """
    물건 수정 API
    Args:
        item_id: 물건 ID
        name: 물건 이름
        is_stored: 물건 보유 여부
        db: 데이터베이스 세션
    Returns:
        모든 물건 정보 리스트 반환 (HTML)
    """
    drawer_service = DrawerService(db)
    if name:
        drawer_service.update_name(item_id, name)
    elif is_stored is not None:
        if is_stored:
            drawer_service.store(item_id)
        else:
            drawer_service.retrieve(item_id)
    return show_all_items(request, db)
