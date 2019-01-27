def _init_(x,y):
    x.y=y


try:
    a,b=[int(x) for x in input('enter a,b').split(',')]
    if(a==b):
        raise myexcep("a==b not allowed")
    res=a/b
    print(res)
except (ValueError, ZeroDivisionError) as e:
    print(e)
except myexcep as me:
    print(me)
else:
    print('no exception')
finally:
    print('bye')
