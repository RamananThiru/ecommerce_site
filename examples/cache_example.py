from django.core.cache import cache

"""
1. settings.py setup:


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

2. start memcache server in local. (It automatically binds itself to port 11211)

3. Use the below snippet to test the caching mechanism
from examples.cache_example import cache_operations
cache_operations()


"""

def cache_operations():
    """
    Example of how to use Django's caching system.
    This example demonstrates setting, getting, and deleting cache.
    """
    # Adding data to cache with a timeout of 15 minutes (60*15 seconds)
    cache.set('my_key', 'my_value', timeout=60*15)
    print("Data added to cache with key 'my_key'.")

    # Retrieving data from the cache
    cached_value = cache.get('my_key')
    print(f"Retrieved value from cache: {cached_value}")

    # Deleting data from the cache
    deletion_success = cache.delete('my_key')
    if deletion_success:
        print("Data with key 'my_key' has been deleted from cache.")

    # Trying to retrieve the deleted data
    cached_value = cache.get('my_key')
    if cached_value is None:
        print("Cache miss: The key 'my_key' was not found or has expired.")
    else:
        print(f"Retrieved value from cache after deletion: {cached_value}")
