from sqlalchemy.orm import Session
from repository.beverage_repository import BeverageRepository


class BeverageService:
    """
    음료 서비스 클래스
    """

    def __init__(self, db: Session):
        self.beverage_repository = BeverageRepository(db)

    def add(self, beverage_name: str, beverage_quantity: int):
        """
        음료 생성 함수
        Args:
            beverage_name: 음료 이름
            beverage_quantity: 음료 수량
        Returns:
            성공 여부
        """
        self.beverage_repository.create(beverage_name, beverage_quantity)
        return True

    def get_by_name(self, beverage_name: str):
        """
        음료 ID 조회 함수
        Args:
            beverage_name: 음료 이름
        Returns:
            beverage_id: 음료 ID
        """
        beverage = self.beverage_repository.read_by_name(beverage_name)
        return beverage

    def get_all(self):
        """
        모든 음료 조회 함수
        Args:
        Returns:
            beverages: 음료 정보 리스트
        """
        beverages = [
            {"id": beverage.id, "name": beverage.name, "quantity": beverage.quantity}
            for beverage in self.beverage_repository.read_all()
        ]
        return beverages

    def remove(self, beverage_id: int):
        """
        음료 삭제 함수
        Args:
            beverage_id: 음료 ID
        Returns:
            성공 여부
        """
        self.beverage_repository.delete_by_id(beverage_id)
        return True

    def refill(self, beverage_id: int):
        """
        음료 보충 함수
        Args:
            beverage_id: 음료 ID
        Returns:
            성공 여부
        """
        beverage = self.beverage_repository.read_by_id(beverage_id)
        beverage.quantity += 1
        self.beverage_repository.update(beverage)
        return True

    def order(self, beverage_id: int):
        """
        음료 주문 함수
        Args:
            beverage_id: 음료 ID
        Returns:
            성공 시 True, 실패 시 False
        """
        beverage = self.beverage_repository.read_by_id(beverage_id)
        if beverage.quantity == 0:
            return False
        else:
            beverage.quantity -= 1
            self.beverage_repository.update(beverage)
            return True
