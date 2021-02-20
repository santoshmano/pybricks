import heapq

a = ['s', 'o', 'r', 't', 'e', 'x', 'a', 'm', 'p', 'l', 'e']

heapq.heapify(a)

print(a,)

l = heapq.nlargest(5, a)

print(l)

l = heapq.nlargest(len(a), a)
print(l)

heapq.heappush(a, 'z')

print(a)

l = heapq.nlargest(len(a), a)
print(l)
