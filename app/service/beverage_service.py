from sqlalchemy.orm import Session
from repository.beverage_repository import BeverageRepository


class BeverageService:
    """
    음료 서비스 클래스
    """

    def __init__(self, db: Session):
        self.beverage_repository = BeverageRepository(db)

    def add_beverage(
        self, beverage_name: str, beverage_quantity: int
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
        self.beverage_repository.create_beverage(
            beverage_name, beverage_quantity)
        return True

    def get_all_beverages(self):
        """
        모든 음료 정보 조회 함수
        Args:
            db: 데이터베이스 세션
        Returns:
            beverages: 모든 음료 정보 리스트
        """
        beverages = self.beverage_repository.read_all_beverages()
        return beverages

    def get_all_inventories(self):
        """
        모든 음료 수량 정보 조회 함수
        Args:
            db: 데이터베이스 세션
        Returns:
            beverages: 모든 음료 수량 정보 딕셔너리
        """
        beverages = {
            bv.name: bv.quantity for bv in self.beverage_repository.read_all_beverages(self)}
        return beverages

    def remove_beverage(self, beverage_id: int):
        """
        음료 삭제 함수
        Args:
            beverage_id: 음료 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.beverage_repository.delete_beverage_by_id(beverage_id)
        return True

    def use_beverage(self, beverage_id: int):
        """
        음료 수정 함수
        Args:
            beverage_id: 음료 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        beverage = self.beverage_repository.read_beverage_by_id(beverage_id)
        if beverage.quantity == 0:
            return False
        else:
            beverage.quantity -= 1
            self.beverage_repository.update_beverage(beverage)
            return True
