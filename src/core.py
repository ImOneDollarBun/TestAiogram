from aiogram import Router
from src.handlers import rout

router = Router()
router.include_router(rout)