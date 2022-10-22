def asteroid_collision(asts, lis):
    collide, i = lis
    if i == len(asts) - 1 or len(asts) in [0, 1]:
        i = 0
        if(collide == False):
            return asts
    if i == 0 :
        collide = False
    if len(asts) > 1 :
        now, next = [asts[i], asts[i+1]]
        if now > 0 and next < 0 :
            if abs(now) <= abs(next) :
                asts.pop(i)
            if abs(now) >= abs(next) :
                asts.pop(i+1 if(len(asts) > 1 and abs(now) != abs(next)) else i)
            collide = True
        return asteroid_collision(asts, [False, i+1 if(collide == False) else 0])

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x, [False, 0]))