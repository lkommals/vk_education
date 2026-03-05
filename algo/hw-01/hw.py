
def reverse_by_indexes(arr, left, right):
    '''
    Функция, которая записывает наоборот часть массива, от left до right 
    '''
    if(left < 0 or right >= len(arr)):
        raise IndexError("Index out of range") 
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left] 
        left += 1 
        right -= 1

def rotate_array(arr, k):
    '''
    Дан массив целых чисел. Необходимо повернуть справа налево часть массива, которая указана параметром k. Решение должно работать за линейное время без дополнительных аллокаций. 
    arr - массив 
    k - параметр 
    '''
    n = len(arr)
    if n == 0:
        return 
    k = k % n 
    reverse_by_indexes(arr, 0, n - 1) 
    reverse_by_indexes(arr, 0, k - 1) 
    reverse_by_indexes(arr, k, n - 1) 

def merge(arr1, arr2): 
    '''
    Дано два отсортированных по возрастанию массива. Необходимо написать функцию, которая объединит эти два массива в один отсортированный за линейное время. 
    '''
    n1 = len(arr1) 
    n2 = len(arr2) 
    res = [0 for i in range(n1 + n2)] 
    left = 0
    right = 0
    ind = 0 
    while left < n1 and right < n2:
        if arr1[left] <= arr2[right]:
            res[ind] = arr1[left]
            left += 1
        else:
            res[ind] = arr2[right]
            right += 1
        ind += 1
    while left < n1:
        res[ind] = arr1[left]
        left += 1
        ind += 1
    while right < n2:
        res[ind] = arr2[right]
        right += 1
        ind += 1
    return res 

def merge_without_allocations(arr1, arr2): 
    '''
    Даны два отсортированных по возрастанию массива. Первый массив имеет размер результирующего массива, пустующие ячейки заполнены нулями. Функция объединяет эти массивы в первый, без дополнительных аллокаций за линейное время. 
    '''
    size_1 = len(arr1) 
    size_2 = len(arr2) 
    if size_2 == 0:
        return arr1
    right = size_2 - 1
    left = size_1 - size_2 - 1 
    curr_ind = size_1 - 1
    while left >= 0 and right >= 0:
        if arr1[left] >= arr2[right]:
            arr1[curr_ind] = arr1[left]
            left -= 1
        else:
            arr1[curr_ind] = arr2[right]
            right -= 1
        curr_ind -= 1


    while right >= 0:
        arr1[curr_ind] = arr2[right]
        right -= 1
        curr_ind -= 1
    return arr1 

def zeros_ones_sort(arr):
    '''
    Дан массив, содержащий только 0 и 1. Отсортировать массив так, чтобы все нули оказались в начале, а все единицы - в конце. Решение должно быть in-place. 
    '''
    if len(arr) == 0:
        return
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right: 
            arr[left], arr[right] = arr[right], arr[left] 
    return arr 

def netherland_flags(arr):
    '''
    Дан массив, состоящие из 0, 1 и 2. Отсортировать его за линейное время
    '''
    n = len(arr) 
    left = 0 
    right = n - 1 
    mid = 0
    while mid <= right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid] 
            mid += 1
            left += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid] 
            mid += 1
            right -= 1
    return arr 

def reverse_evens(arr):
    '''
    функция для переноса в начало неотсортированного массива четных чисел. Перераспределение стабильно.  
    '''
    n = len(arr) 
    evens = []
    odds = []
    for x in arr:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    arr[:] = evens + odds
    return arr

def zeros_last(arr):
    '''
    Перенос ненулевых элемнтов в начало массива за один проход и стабильно
    '''
    n = len(arr)
    index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    return arr