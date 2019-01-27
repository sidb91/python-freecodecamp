from add_diff import *
try:
    a,b=[int(x) for x in input('enter a,b - ').split(',')]
    print("add",add_num(a,b))
    print("diff",diff_num(a,b))
except ValueError as e:
    print(e)
