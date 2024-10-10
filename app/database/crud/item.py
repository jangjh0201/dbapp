from sqlalchemy.orm import Session
from models.models import Item


def create_item(db: Session, name: str, storage: bool):
    item = Item(name=name, storage=True)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def read_item_by_id(db: Session, item_id: float):
    return db.query(Item).filter(Item.id == item_id).first()


def read_all_items(db: Session):
    return db.query(Item).all()


def update_item(
    db: Session,
    item_id: float,
    name: str = None,
    storage: bool = None,
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        return None

    if name is not None:
        item.name = name
    if storage is not None:
        item.price = storage

    db.commit()
    db.refresh(item)
    return item


def delete_item_by_id(db: Session, item_id: float):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item


def delete_all_items(db: Session):
    items = db.query(Item).all()
    for item in items:
        db.delete(item)
    db.commit()
    return items
