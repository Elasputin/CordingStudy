import sys
sinput=sys.stdin.readline
N= int(sinput().rstrip())
my_lst=list()
for i in range(N):
    x, y= map(int, sinput().rstrip().split())
    my_lst.append(x+y)
for num in my_lst:
    print(num)