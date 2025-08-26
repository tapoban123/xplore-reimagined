from app.utils.constants import REDIS_SECRETS
import redis


def get_redis_config() -> redis.Redis:
    """Configure Redis for storage."""
    redis_config = redis.Redis(
        host=REDIS_SECRETS.REDIS_HOST.value,
        port=int(REDIS_SECRETS.REDIS_PORT.value),
        decode_responses=True,
        username=REDIS_SECRETS.REDIS_USERNAME.value,
        password=REDIS_SECRETS.REDIS_PASSWORD.value,
    )
    return redis_config
