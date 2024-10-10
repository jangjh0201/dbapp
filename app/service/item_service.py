from sqlalchemy.orm import Session
from models.models import Item
from app.database.crud.item import create_item, read_all_items


def add_item(
    item_name: str, db: Session
):
    """
    아이템 추가 함수
    Args:
        item_name: 아이템 이름
        storage: 아이템 보관 여부
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    create_item(db, item_name, True)
    return True


def get_all_items(db: Session):
    """
    모든 아이템 정보 조회 함수
    Args:
        db: 데이터베이스 세션
    Returns:
        items: 모든 아이템 정보 리스트
    """
    items = read_all_items(db)
    return items


def remove_item(item_id: int, db: Session):
    """
    아이템 삭제 함수
    Args:
        item_id: 아이템 ID
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    db.query(Item).filter(Item.id == item_id).delete()
    db.commit()
    return True


def edit_item(item_id: int, db: Session):
    """
    아이템 수정 함수
    Args:
        item_id: 아이템 ID
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    db.query(Item).filter(Item.id == item_id).update({Item.storage: False})
    db.commit()
    return True
