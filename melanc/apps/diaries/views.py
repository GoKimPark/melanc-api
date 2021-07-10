from fastapi import Depends, HTTPException, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from melanc.core.db import db_session, get_db
from melanc.apps.diaries import models, schemas

router = InferringRouter()


@cbv(router)
class DiaryViewSet:
    @router.get("/")
    def list(self, db: db_session = Depends(get_db)):
        diaries = db.query(models.Diary).order_by(models.Diary.id).all()
        return diaries

    @router.get("/{diary_id}", response_model=schemas.Diary)
    def retrieve(self, diary_id: int, db: db_session = Depends(get_db)):
        diary = db.query(models.Diary).get(diary_id)

        if not diary:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found."
            )

        return diary

    @router.post(
        "/", status_code=status.HTTP_201_CREATED, response_model=schemas.DiaryCreate
    )
    def create(self, diary_data: schemas.DiaryCreate, db: db_session = Depends(get_db)):
        diary = models.Diary(**diary_data.dict())
        db.add(diary)
        db.commit()

        return diary

    @router.put("/{diary_id}", response_model=schemas.DiaryBase)
    def update(
        self,
        diary_id: int,
        diary_data: schemas.DiaryBase,
        db: db_session = Depends(get_db),
    ):
        query_diary = db.query(models.Diary).filter_by(id=diary_id)

        if query_diary.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found."
            )

        query_diary.update(diary_data.dict())
        query_diary.commit()

        return diary_data

    @router.delete("/{diary_id}", status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, diary_id: int, db: db_session = Depends(get_db)):
        diary = db.query(models.Diary).get(diary_id)

        if not diary:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found."
            )

        db.delete(diary)
        db.commit()
