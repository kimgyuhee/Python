import datetime


g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

routes = ["E 2","S 2","W 1"]
for route in routes:
    direction, distance = route.split()
    print(g[direction])


now = datetime.datetime(2022,5,19)
print(now)
now_after = now + datetime.timedelta(days=6*30)
print(now_after)

print(now_after>now)