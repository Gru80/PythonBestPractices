def generator():
    i=0
    while True:
        i=i+2
        yield i

xx = generator()
for x in [0,1,2,3,4,5]:
    print(next(xx))