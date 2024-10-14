from sqlalchemy.orm import Session
from repository.item_repository import ItemRepository


class ItemService:
    """
    물품 보관 서비스 클래스
    """

    def __init__(self, db: Session):
        self.item_repository = ItemRepository(db)

    def add(self, item_name: str):
        """
        물품 추가 함수
        Args:
            item_name: 물품 이름
            storage: 물품 보관 여부
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.item_repository.create(item_name)
        return True

    def get_all(self):
        """
        모든 물품 정보 조회 함수
        Args:
            db: 데이터베이스 세션
        Returns:
            items: 모든 물품 정보 리스트
        """
        items = [
            {"id": item.id, "name": item.name, "storage": item.storage}
            for item in self.item_repository.read_all()
        ]
        return items

    def remove(self, item_id: int):
        """
        물품 삭제 함수
        Args:
            item_id: 물품 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.item_repository.delete_by_id(item_id)
        return True

    def rename(self, item_id: int, name: str):
        """
        물품 이름 수정 함수
        Args:
            item_id: 물품 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        item = self.item_repository.read_by_id(item_id)
        self.item_repository.update(item, name, None)
        return True

    def store(self, item_id: int):
        """
        물품 보관 함수
        Args:
            item_id: 물품 ID
            db: 데이터베이스 세션
        Returns:
            성공 시 물품 정보, 실패 시 None
        """
        item = self.item_repository.read_by_id(item_id)
        result = self.item_repository.update(item, None, True)
        return result

    def use(self, item_id: int):
        """
        물품 사용 함수
        Args:
            item_id: 물품 ID
            db: 데이터베이스 세션
        Returns:
            성공 시 물품 정보, 실패 시 None
        """
        item = self.item_repository.read_by_id(item_id)
        result = self.item_repository.update(item, None, False)
        return result
