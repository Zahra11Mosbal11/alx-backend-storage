#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Represents an object for storing data in a Redis data storage."""
    def __init__(self):
        """Initializes a Cache instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage."""
        return self.get(key, lambda x: int(x))
