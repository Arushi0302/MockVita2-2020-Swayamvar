n = int(input())
b = input()
g = input()

i = 0
while i<n:
    d = g.find(b[0])
    if d<0:
        break
    g = g[d+1:]+g[:d]
    b = b[1:]
    i = i + 1
print(len(b))
