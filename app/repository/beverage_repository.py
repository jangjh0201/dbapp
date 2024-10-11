from sqlalchemy.orm import Session
from models.beverage import Beverage


class BeverageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_beverage(self, name: str, price: int, quantity: int):
        beverage = Beverage(name=name, price=price, quantity=quantity)
        self.db.add(beverage)
        self.db.commit()
        self.db.refresh(beverage)
        return beverage

    def read_beverage_by_id(self, beverage_id: int):
        return self.db.query(Beverage).filter(Beverage.id == beverage_id).first()

    def read_all_beverages(self):
        return self.db.query(Beverage).all()

    def update_beverage(
        self,
        beverage: Beverage,
        name: str = None,
        quantity: int = None,
    ):
        if name is not None:
            beverage.name = name
        if quantity is not None:
            beverage.quantity = quantity

        self.db.commit()
        self.db.refresh(beverage)
        return beverage

    def delete_beverage_by_id(self, beverage_id: int):
        beverage = self.db.query(Beverage).filter(
            Beverage.id == beverage_id).first()
        if beverage:
            self.db.delete(beverage)
            self.db.commit()
        return beverage

    def delete_all_beverages(self):
        beverages = self.db.query(Beverage).all()
        for beverage in beverages:
            self.db.delete(beverage)
        self.db.commit()
        return beverages
