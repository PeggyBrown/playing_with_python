def binary_search(list, item)
    low = 0
    hight = len(list) - 1
    while low <= hight:
        mid = (low + hight) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

my_list = [1, 2, 5, 7, 9]
Print binary_search(my_list, 3)
Print binary_search(my_list, -1) 
