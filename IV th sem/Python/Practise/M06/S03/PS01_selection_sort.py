"""Selection sort implementation with a small explanation."""


def selection_sort(arr):
	n = len(arr)
	for i in range(n - 1):
		min_index = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_index]:
				min_index = j		
		if min_index != i:
			arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr


if __name__ == "__main__":
	numbers = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
	print("Original list:", numbers)
	selection_sort(numbers)
	print("Sorted list  :", numbers)

'''Selection sort repeatedly picks the smallest element from the "
"unsorted part and places it at the correct position. "
"It is simple to understand but slower for large lists."'''
