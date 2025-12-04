from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.middlewares.auth_middleware import AuthMiddleware

# Routers
from app.api.v1 import auth, users, barang, sales

# DB
from app.db.base import Base
from app.db.session import engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# ----------------------------
# CORS middleware
# ----------------------------
origins = ["*"]  # Adjust in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Auth Middleware
# ----------------------------
app.add_middleware(AuthMiddleware)

# ----------------------------
# API Routers
# ----------------------------
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(users.router, prefix=settings.API_V1_STR)
app.include_router(barang.router, prefix=settings.API_V1_STR)
app.include_router(sales.router, prefix=settings.API_V1_STR)

# ----------------------------
# Root endpoint
# ----------------------------
@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
