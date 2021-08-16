# Water Jug problem

print("Solution for Water Jug problem!")
x = int(input("Enter the capacity of jug1 : "))
y = int(input("Entert the capacity of jug2 : "))

target = int(input("Enter the target volume : "))

def bfs(start, target, x, y):
	path = []
	front = []
	front.append(start)
	visited = []
	while(not (not front)):
		current = front.pop()
		x = current[0]
		y = current[1]
		path.append(current)
		if(x == target or y == target):
			print("Found!")
			return path

        if(current[0] < x and ([x, current[1]] not in visited)):
			front.append([x, current[1]])
			visited.append([x, current[1]])
        
        if(current[1] < y and ([current[0], y] not in visited)):
			front.append([current[0], y])
			visited.append([current[0], y])

        if(current[0] > x and ([0, current[1]] not in visited)):
			front.append([0, current[1]])
			visited.append([0, current[1]])
        
        if(current[1] > y and ([x, 0] not in visited)):
			front.append([x, 0])
			visited.append([x, 0])
        
        if(current[1] > 0 and ([min(x + y, x), max(0, x + y - x)] not in visited)):
            front.append([min(x + y, x), max(0, x + y - x)])
            visited.append([min(x + y, x), max(0, x + y - x)])
            
        if current[0] > 0  and ([max(0, x + y - y), min(x + y, y)] not in visited):
			front.append([max(0, x + y - y), min(x + y, y)])
			visited.append([max(0, x + y - y), min(x + y, y)])

        return -1

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

start = [0, 0] 

if target % gcd(x,y) == 0:
	print(bfs(start, target, x, y))
else:
	print("No solution")



        

    