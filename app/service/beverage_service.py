from sqlalchemy.orm import Session
from models.models import Beverage
from app.database.crud.beverage import create_beverage, read_all_beverages


def add_beverage(
    beverage_name: str, beverage_quantity: int, db: Session
):
    """
    음료 추가 함수
    Args:
        beverage_name: 음료 이름
        beverage_quantity: 음료 수량
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    create_beverage(db, beverage_name, beverage_quantity)
    return True


def get_all_beverages(db: Session):
    """
    모든 음료 정보 조회 함수
    Args:
        db: 데이터베이스 세션
    Returns:
        beverages: 모든 음료 정보 리스트
    """
    beverages = read_all_beverages(db)
    return beverages


def get_all_inventories(db: Session):
    """
    모든 음료 수량 정보 조회 함수
    Args:
        db: 데이터베이스 세션
    Returns:
        beverages: 모든 음료 수량 정보 딕셔너리
    """
    beverages = {bv.name: bv.quantity for bv in read_all_beverages(db)}
    return beverages


def remove_beverage(beverage_id: int, db: Session):
    """
    음료 삭제 함수
    Args:
        beverage_id: 음료 ID
        db: 데이터베이스 세션
    Returns:
        성공 여부
    """
    db.query(Beverage).filter(Beverage.id == beverage_id).delete()
    db.commit()
    return True