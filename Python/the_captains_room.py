# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
rooms = list(map(int, input().split()))
roomSet = set(rooms)
roomSum = sum(rooms)
roomSetSum = sum(roomSet) * k
captiansRoom = (roomSetSum - roomSum) // (k - 1)
print(captiansRoom)
