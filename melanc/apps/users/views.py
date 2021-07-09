from fastapi_utils.cbv import cbv

from melanc.apps.users.crud import UserCRUD
from melanc.core.app import melanc_app
from melanc.core.db import engine, db_session, Base

Base.metadata.create_all(bind=engine)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()


@cbv(melanc_app)
class UserViewSet:
    crud_instance = UserCRUD()

    @melanc_app.get("/users")
    def list(self):
        return "user list view"
