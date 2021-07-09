from fastapi_utils.cbv import cbv
from melanc.core.app import melanc_app
from melanc.apps.diaries.crud import DiaryCRUD
from melanc.core.db import db_session, Base, engine

Base.metadata.create_all(bind=engine)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()


@cbv(melanc_app)
class DiaryViewSet:  # TODO: implement view-set
    crud_instance = DiaryCRUD()

    @melanc_app.get("/diaries")
    def list(self):
        return "hello melancholiary"
