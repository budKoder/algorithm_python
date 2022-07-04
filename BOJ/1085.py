import sys
x,y,w,h = map(int,sys.stdin.readline().split())
left_x = x
right_x = w-x
down_y = y
up_y = h-y
print(min(left_x,right_x,down_y,up_y))