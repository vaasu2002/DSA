# Python program for linear search

def linear_search(arr, search_Element):
	left = 0
	length = len(arr)
	position = -1
	right = length - 1

	# Run loop from 0 to right
  
	for left in range(0, right, 1):

		# If search_element is found with left variable

		if (arr[left] == search_Element):
			position = left
			print(f"Element found in Array at {position +1} Position with {left + 1} Attempt")
			break

		# If search_element is found with right variable

		if (arr[right] == search_Element):
			position = right
			print(f"Element found in Array at {position + 1} Position with {length - right} Attempt")
			break
		left += 1
		right -= 1

	# If element not found
  
	if (position == -1):
		print(f"Not found in Array with {left} Attempt")

#input call
array = list(int(i) for i in input("Enter elements of array: ").split(" "))
search_element = int(input("Enter the element you want to search: "))

# Function call

linear_search(array, search_element)

