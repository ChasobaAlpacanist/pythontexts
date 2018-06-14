def main():
    a = [2,4,1,3,6,7,7,5,3,221,1,3,44,5,556,67,23,125,94]
    sorted_data = merge_sort(a)
    for i in sorted_data:
        print(i)

def merge_sort(array):
    if(len(array) == 1):
        return array
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge_sort_merge(left, right)

def merge_sort_merge(left, right):
    sorted_data = []
    left_index = 0
    right_index = 0
    while(left_index < len(left) and right_index < len(right)):
        if(left[left_index] <= right[right_index]):
            sorted_data.append(left[left_index])
            left_index += 1
        else:
            sorted_data.append(right[right_index])
            right_index += 1
    if(left_index < len(left)):
        sorted_data.extend(left[left_index:])
    else:
        sorted_data.extend(right[right_index:])
    return sorted_data

main()
