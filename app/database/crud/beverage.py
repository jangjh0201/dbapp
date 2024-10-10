from sqlalchemy.orm import Session
from models.models import Beverage


def create_beverage(db: Session, name: str, price: int, quantity: int):
    beverage = Beverage(name=name, price=price, quantity=quantity)
    db.add(beverage)
    db.commit()
    db.refresh(beverage)
    return beverage


def read_beverage_by_id(db: Session, beverage_id: float):
    return db.query(Beverage).filter(Beverage.id == beverage_id).first()


def read_all_beverages(db: Session):
    return db.query(Beverage).all()


def update_beverage(
    db: Session,
    beverage_id: float,
    name: str = None,
    price: int = None,
    quantity: int = None,
):
    beverage = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if beverage is None:
        return None

    if name is not None:
        beverage.name = name
    if price is not None:
        beverage.price = price
    if quantity is not None:
        beverage.quantity = quantity

    db.commit()
    db.refresh(beverage)
    return beverage


def delete_beverage_by_id(db: Session, beverage_id: float):
    beverage = db.query(Beverage).filter(Beverage.id == beverage_id).first()
    if beverage:
        db.delete(beverage)
        db.commit()
    return beverage


def delete_all_beverages(db: Session):
    beverages = db.query(Beverage).all()
    for beverage in beverages:
        db.delete(beverage)
    db.commit()
    return beverages
