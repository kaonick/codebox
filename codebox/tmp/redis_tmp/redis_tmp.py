import redis

# Connect to the database
r = redis.Redis(host='localhost', port=6379)

# Store a key
print("set key1 123")
print(r.set('key1', '123'))

# Retrieve the key
print("get key1")
print(r.get('key1'))