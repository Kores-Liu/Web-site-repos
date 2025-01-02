import redis

myHostname = "messageboard.redis.cache.windows.net"
myPassword = "uREqQjvshIIYFIG5h1p1Z3TbZiIqLGzdYAzCaP14y2Y="

r = redis.Redis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.get("Message")
print("GET Message returned : " + result)

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print(f"id : {c['id']}, addr : {c['addr']}")


r = redis.Redis(host='messageboard.redis.cache.windows.net', port=6380, password='uREqQjvshIIYFIG5h1p1Z3TbZiIqLGzdYAzCaP14y2Y=', ssl=True)