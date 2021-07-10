from melanc.core.app import melanc_app
from melanc.apps.users import views as user_views
from melanc.apps.diaries import views as diary_views
from melanc.core.db import Base, engine

Base.metadata.create_all(bind=engine)

melanc_app.include_router(user_views.router, prefix="/users", tags=["users"])
melanc_app.include_router(diary_views.router, prefix="/diaries", tags=["diaries"])
