from fastapi import APIRouter
from app.router.v1 import drawer
from router.v1 import home, beverage, auth

router = APIRouter(
    # prefix="/api/v1"
)

router.include_router(home.router)
router.include_router(drawer.router)
router.include_router(beverage.router)
router.include_router(auth.router)
