N = int(input())
nums = []
for i in range(N) :
    a,b = map(int,input().split())
    nums.append((a,b))
a = sorted(nums, key = lambda x : (x[0],x[1]))
for i in a :
    print(*i)
