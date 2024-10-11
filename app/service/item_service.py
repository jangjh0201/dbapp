from repository.item_repository import ItemRepository


class ItemService:
    """
    아이템 서비스 클래스
    """

    def __init__(self):
        self.item_repository = ItemRepository()

    def add_item(self, item_name: str):
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

    def get_all_items(self):
        """
        모든 아이템 정보 조회 함수
        Args:
            db: 데이터베이스 세션
        Returns:
            items: 모든 아이템 정보 리스트
        """
        items = self.item_repository.read_all_items()
        return items

    def remove_item(self, item_id: int):
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

    def edit_item_name(self, item_id: int, name: str):
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

    def change_item_storage(self, item_id: int, request: bool):
        """
        아이템 상태 변경 함수
        Args:
            item_id: 아이템 ID
            db: 데이터베이스 세션
        Returns:
            성공 여부
        """
        if request == True:
            self.item_repository.update_item(item_id, None, False)
        elif request == False:
            self.item_repository.update_item(item_id, None, True)
        else:
            return False
