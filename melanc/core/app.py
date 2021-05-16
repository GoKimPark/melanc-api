from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

melanc_app = FastAPI()

origins = [
    "http://localhost:8000",
]  # TODO: add origins for production

melanc_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
