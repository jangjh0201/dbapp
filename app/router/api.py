from fastapi import APIRouter
from router.v1 import home, drawer, beverage, auth

router = APIRouter(
    # prefix="/api/v1"
)

router.include_router(home.router)
router.include_router(drawer.router)
router.include_router(beverage.router)
router.include_router(auth.router)
