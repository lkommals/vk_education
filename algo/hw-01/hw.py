
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
    k = k % n 
    reverse_by_indexes(arr, 0, n - 1) 
    reverse_by_indexes(arr, 0, k - 1) 
    reverse_by_indexes(arr, k, n - 1) 

def merge_sorted(arr1, arr2): 
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

def merge_sorted_without_allocations(arr1, arr2): 
    '''
    Даны два отсортированных по возрастанию массива. Первый массив имеет размер результирующего массива. Функция объединяет эти массивы в первый, без дополнительных аллокаций за линейное время. 
    '''
    

def main():
    arr1 = [1,2,3, 7,]
    arr2 = [1]
    res = merge_sorted(arr1, arr2) 
    print(res) 

if __name__ == '__main__':
    main() 