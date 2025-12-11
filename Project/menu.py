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


