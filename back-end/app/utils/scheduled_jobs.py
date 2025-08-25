from app.database.redis_config import get_redis_config
from datetime import timedelta
import rich

def revive_redis_db() -> None:
    """
    Run this function to trigger Redis database every 7 days to prevent the database from getting deleted.
    This is required since, 'Redis free databases are deleted after a minimum of 14 days of inactivity'.
    """

    redis = get_redis_config()
    redis.setex(name="Sample Data", value="Sample Value", time=timedelta(minutes=1))

