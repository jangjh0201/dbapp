from sqlalchemy.orm import Session
from repository.item_repository import ItemRepository


class DrawerService:
    """
    서랍 서비스 클래스
    """

    def __init__(self, db: Session):
        self.item_repository = ItemRepository(db)

    def add(self, item_name: str):
        """
        아이템 추가 함수
        Args:
            item_name: 아이템 이름
            storage: 아이템 보관 여부
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.item_repository.create_item(item_name, True)
        return True

    def get_all(self):
        """
        모든 아이템 정보 조회 함수
        Args:
            db: 데이터베이스 세션
        Returns:
            items: 모든 아이템 정보 리스트
        """
        items = self.item_repository.read_all_items()
        return items

    def remove(self, item_id: int):
        """
        아이템 삭제 함수
        Args:
            item_id: 아이템 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.item_repository.delete_item_by_id(item_id)
        return True

    def rename(self, item_id: int, name: str):
        """
        아이템 이름 수정 함수
        Args:
            item_id: 아이템 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        self.item_repository.update_item(item_id, name, None)
        return True

    def store(self, item_id: int):
        """
        아이템 보관 함수
        Args:
            item_id: 아이템 ID
            db: 데이터베이스 세션
        Returns:
            성공 시 아이템 정보, 실패 시 None
        """
        result = self.item_repository.update_item(item_id, None, True)
        return result

    def retrieve(self, item_id: int):
        """
        아이템 반납 함수
        Args:
            item_id: 아이템 ID
            db: 데이터베이스 세션
        Returns:
            성공 시 아이템 정보, 실패 시 None
        """
        result = self.item_repository.update_item(item_id, None, False)
        return result
