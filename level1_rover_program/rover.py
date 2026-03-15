import math

try:
    x1,y1 = map(float, input("Origin (x1 y1): ").split())
    x2,y2 = map(float, input("Destination (x2 y2): ").split())

    u = float(input("Initial velocity (u): "))
    a = float(input("Acceleration (a): "))
    vmax = float(input("Max speed (vmax): "))

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    t1 = (vmax-u)/a
    d1 = u*t1 + 0.5*a*t1**2

    if d1 >= d:
        t = (-u + math.sqrt(u**2 + 2*a*d))/a
    else:
        t = t1 + (d-d1)/vmax

    print("Distance:",round(d,1),"m")
    print("Time:",round(t,1),"seconds")

except:
    print("Invalid input")
