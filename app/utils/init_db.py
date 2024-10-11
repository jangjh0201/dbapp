from config.database import Base, engine


def initialize_tables():
    # 테이블 삭제
    Base.metadata.drop_all(bind=engine)
    # 테이블 생성
    Base.metadata.create_all(bind=engine)
