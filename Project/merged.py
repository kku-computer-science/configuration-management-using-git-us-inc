def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
arr = quick_sort(arr)
print(arr)def bubble_sort(arr):

    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
number_to_sort = input("Please Enter the Number(Serperate by space): ")
nums = list(map(int, number_to_sort.split(" ")))

print("\nSelect Sorting Method(Ascending Only)\n1.Bubble Sort\n2.Quick Sort")
sort_method = input("Your Choice: ")
sort_method = sort_method.lower()
sort = ""
result = None

if sort_method == "1" or "bubble" in sort_method:
	result = bubble_sort(nums)
	sort = "Bubble Sort"
elif sort_method=="2" or "quick" in sort_method:
	result = quick_sort(nums)
	sort = "Quick Sort"

print("=======================\nSorting Method: ", sort)
print("Result: ",result)


