#Contributed by @Hinal-Srivastava

def binarySearch( arr, l, r, x): 
	if r >= l: 
		mid = l + ( r-l ) / 2

		if arr[mid] == x: 
			return mid 
		
		if arr[mid] > x: 
			return binarySearch(arr, l, mid - 1, x) 

		return binarySearch(arr, mid + 1, r, x) 

	return -1


def exponentialSearch(arr, n, x): 

	if arr[0] == x: 
		return 0

	i = 1
	while i < n and arr[i] <= x: 
		i = i * 2

	return binarySearch( arr, i / 2, min(i, n), x) 
	

# Driver Code 
arr = [] 
n = int(input('Number of elements: '))
print('Enter elements ', end='')
for i in range(n):
    arr.append(int(input()))
arr.sort()
x = int(input('Search element: '))  
result = exponentialSearch(arr, n, x) 
if result == -1: 
	print("Element not found")
else: 
	print("Elementfound at %d" %(result))

