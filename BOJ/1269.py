import sys

an,bn = map(int,sys.stdin.readline().split())
alist = set(map(int,sys.stdin.readline().split()))
blist = set(map(int,sys.stdin.readline().split()))

comm = alist.intersection(blist)
total = alist.union(blist)

print(len(total.difference(comm)))