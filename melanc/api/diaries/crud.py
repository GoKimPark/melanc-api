from melanc.api.diaries import models, schemas
from melanc.core.db import db_session
from melanc.utils.singleton import Singleton


class DiaryCRUD(Singleton):  # TODO: refactoring (divide BasicCRUD and this)
    @staticmethod
    def list(db: db_session):
        return db.query(models.Diary).all()

    @staticmethod
    def list_by_owner(db: db_session, owner_id: int):
        diary = models.Diary
        return db.query(diary).filter(diary.owner.id == owner_id)

    @staticmethod
    def retrieve(db: db_session, diary_id: int):
        return db.query(models.Diary).get(diary_id)

    @staticmethod
    def create(db: db_session, diary: schemas.DiaryCreate):
        diary_ = models.Diary(**diary.dict())
        db.add(diary_)
        db.commit()

    @staticmethod
    def update(db: db_session, diary: schemas.Diary):  # TODO: apply service policy
        diary_ = db.query(models.Diary).get(diary.id)
        for key, value in diary.dict().items():
            setattr(diary_, key, value)

        db.commit()
