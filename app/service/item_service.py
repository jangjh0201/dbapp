from sqlalchemy.orm import Session
from app.database.crud.item import create_item, read_all_items, read_item_by_id, delete_item_by_id, update_item
from sqlalchemy import update
from sqlalchemy import update


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
    delete_item_by_id(db, item_id)
    return True


def edit_item_name(item_id: int, name: str, db: Session):
    """
    아이템 수정 함수
    Args:
        item_id: 아이템 ID
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    update_item(db, item_id, name, None)
    return True


def change_item_storage(item_id: int, request: bool, db: Session):
    """
    아이템 보관 함수
    Args:
        item_id: 아이템 ID
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    if request == True:
        update(db, item_id, None, False)
    elif request == False:
        update(db, item_id, None, True)
    else:
        return False
