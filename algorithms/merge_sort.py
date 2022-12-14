def merge_sort(arr):
	if len(arr) > 1:
		left_arr = arr[: len(arr) // 2]
		right_arr = arr[len(arr) // 2 :]

		merge_sort(left_arr)
		merge_sort(right_arr)

		left_arr_index = 0
		right_arr_index = 0
		merged_arr_index = 0
		while left_arr_index < len(left_arr) and right_arr_index < len(right_arr):
			if left_arr[left_arr_index] < right_arr[right_arr_index]:
				arr[merged_arr_index] = left_arr[left_arr_index]
				left_arr_index += 1
			else:
				arr[merged_arr_index] = right_arr[right_arr_index]
				right_arr_index += 1
				
			merged_arr_index += 1

		while left_arr_index < len(left_arr):
			arr[merged_arr_index] = left_arr[left_arr_index]
			left_arr_index += 1
			merged_arr_index += 1

		while right_arr_index < len(right_arr):
			arr[merged_arr_index] = right_arr[right_arr_index]
			right_arr_index += 1
			merged_arr_index += 1

def sort_set(arr):
	merge_sort(arr)
	return arr



