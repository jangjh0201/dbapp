from sqlalchemy.orm import Session
from models.item import Item


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str):
        item = Item(name=name, storage=True)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def read_by_id(self, item_id: float):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def read_by_name(self, name: str):
        return self.db.query(Item).filter(Item.name == name).first()

    def read_all(self):
        return self.db.query(Item).all()

    def update(self, item: Item, name: str, storage: bool):
        if name is not None:
            item.name = name
        if storage is not None:
            item.storage = storage

        self.db.commit()
        self.db.refresh(item)
        return item

    def delete_by_id(self, item_id: float):
        item = self.db.query(Item).filter(Item.id == item_id).first()
        if item:
            self.db.delete(item)
            self.db.commit()
        return item

    def delete_all(self):
        items = self.db.query(Item).all()
        for item in items:
            self.db.delete(item)
        self.db.commit()
        return items
