import os
from dotenv import load_dotenv
from redis import asyncio as aioredis  # use redis.asyncio instead of aioredis
import redis
load_dotenv()

class Redis:
    def __init__(self):
        """Initialize Redis connection"""
        self.REDIS_URL = os.environ.get('REDIS_URL')
        self.REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
        self.REDIS_USER = os.environ.get('REDIS_USER')
        self.REDIS_HOST = os.environ.get('REDIS_HOST')
        self.REDIS_PORT = os.environ.get('REDIS_PORT')

        # If REDIS_URL is available, use that. Otherwise build URL manually.
        if self.REDIS_URL:
            self.connection_url = self.REDIS_URL
        else:
            self.connection_url = f"rediss://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    async def create_connection(self):
        self.connection = aioredis.from_url(
            self.connection_url,
            decode_responses=True,  # ensures values are returned as strings, not bytes
        )
        return self.connection
    def create_rejson_connection(self):
        self.redisJson = redis.Redis(host=self.REDIS_HOST,
                                port=self.REDIS_PORT, decode_responses=True, username=self.REDIS_USER, password=self.REDIS_PASSWORD)

        return self.redisJson