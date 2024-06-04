from functools import reduce
from math import sqrt
class Loc:
    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1
    def __add__(self,q):
        return Loc(self.x + q.x, self.y + q.y)
    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
    def dist(self):
        return sqrt(self.x**2 + self.y**2)
location = Loc(0,0)
location_list = []
dist_list = []
robot_location = []
while True:
    try:
        x,y = map(int,input().split())
        location_list.append(Loc(x,y))
        now_location = reduce(lambda a,b:a+b, location_list, location)
        robot_location.append(now_location)
        D = now_location.dist()
        dist_list.append(D)
    except EOFError:
        break
dic = {}
for i,w in enumerate(robot_location):
    dic[dist_list[i]] = w
print(dic[min(dist_list)])
print(f"{min(dist_list):.2f}")
