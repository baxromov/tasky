from django.core.cache import cache
from rest_framework.response import Response


def cache_response(cache_key, expiration: str = 3600):
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            cached_data = cache.get(cache_key)

            if cached_data:
                return Response(cached_data)

            response = func(self, request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=expiration)
            return response

        return wrapper

    return decorator
