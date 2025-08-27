from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler

from .features.ai_questionnaire.controller import ai_router
from .database.core import create_all_tables
from .features.auth.student.controller import student_auth_router
from app.features.profile.controller import user_profile_router
from app.utils.scheduled_jobs import revive_redis_db
from .database.cloudinary_config import set_cloudinary_config
from .logging import log


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Code to execute when before api starts accepting requests"""
    log.info("[bold blue]Running start event[/]")

    app.mount("/static", StaticFiles(directory="static"), name="static")

    scheduler = BackgroundScheduler()
    trigger = CronTrigger(day_of_week=6, hour=0, minute=0)
    scheduler.add_job(
        revive_redis_db,
        trigger,
        name="Triggers the RedisDB to prevent it from getting deleted.",
    )
    scheduler.start()

    create_all_tables()
    set_cloudinary_config()

    yield
    """Code to execute when after exiting app"""


app = FastAPI(lifespan=lifespan)
app.include_router(ai_router)
app.include_router(student_auth_router)
app.include_router(user_profile_router)


@app.get("/")
def home():
    return "Welcome to AI Career Finder App - Xplore"
