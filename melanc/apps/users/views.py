from typing import List

from fastapi import Depends, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from melanc.apps.users import schemas as user_schemas
from melanc.apps.diaries import schemas as diary_schemas
from melanc.apps.users import models
from melanc.core.db import get_db, db_session

router = InferringRouter()


@cbv(router)
class UserViewSet:
    @router.get("/", response_model=List[user_schemas.User])
    def list(self, db: db_session = Depends(get_db)):
        users = db.query(models.User).order_by(models.User.id).all()

        return users

    @router.get("/{user_id}", response_model=user_schemas.User)
    def retrieve(self, user_id: int, db: db_session = Depends(get_db)):
        user = db.query(models.User).get(user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found.")

        return user

    @router.get("/{user_id}/diaries", response_model=List[diary_schemas.Diary])
    def get_diaries(self, user_id: int, db: db_session = Depends(get_db)):
        user = db.query(models.User).get(user_id)

        return user.diaries

    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schemas.UserCreate)
    def create(self, user_data: user_schemas.UserCreate, db: db_session = Depends(get_db)):
        user = models.User(**user_data.dict())
        db.add(user)
        db.commit()

        return user_data

    @router.put("/{user_id}", response_model=user_schemas.UserBase)
    def update(self, user_id: int, user_data: user_schemas.UserBase, db: db_session = Depends(get_db)):
        query_user = db.query(models.User).filter_by(id=user_id)

        if query_user.count() == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found.")

        query_user.update(user_data.dict())
        db.commit()

        return user_data

    @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, user_id: int, db: db_session = Depends(get_db)):
        query_user = db.query(models.User).filter_by(id=user_id)

        if query_user.count() == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found.")

        db.commit()
