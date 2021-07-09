from melanc.apps.users import models
from melanc.core.db import db_session
from melanc.utils.singleton import Singleton


class UserCRUD(Singleton):  # TODO: remove
    @staticmethod
    def list(db: db_session):
        return db.query(models.User).all()
