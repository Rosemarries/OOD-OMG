def asteroid_collision(asts, i):
    collide = False
    if i == len(asts) - 1 or len(asts) in [0, 1]:
        return asts
    if len(asts) > 1 :
        now, next = [asts[i], asts[i+1]]
        if now > 0 and next < 0 :
            if abs(now) <= abs(next) :
                asts.pop(i)
            if abs(now) >= abs(next) :
                asts.pop(i+1 if(len(asts) > 1 and abs(now) != abs(next)) else i)
            collide = True
        return asteroid_collision(asts, i+1 if(collide == False) else 0)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x, 0))