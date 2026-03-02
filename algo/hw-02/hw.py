
class Node:
    def __init__(self, val=None):
        self.next = None 
        self.prev = None 
        self.val = val 

class Queue:
    def __init__(self):
        self.head = Node() 
        self.tail = Node() 
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.size = 0 
    def push(self, val): 
        new_node = Node(val) 
        new_node.next = self.head.next 
        new_node.prev = self.head 
        self.head.next.prev = new_node 
        self.head.next = new_node 
        self.size += 1
    def pop(self): 
        if self.head.next == self.tail:
            return None 
        pop_result = self.tail.prev 
        self.tail.prev = pop_result.prev 
        pop_result.prev.next = pop_result.next 
        pop_result.next = None 
        pop_result.prev = None 
        self.size -= 1
        return pop_result.val 
    def peek(self): 
        if self.head.next == self.tail:
            return None 
        return self.tail.prev.val 
    def isempty(self):
        if self.size == 0:
            return True 
        return False 

def print_list(node):
    while node != None:
        print(node.val) 
        node = node.next 

def reverse_node(head):
    '''
    Функция принимает на вход односвязный список и разворачивает его. Разворот in-place, изменяя ссылки между узлами, алгоритм работает за O(n) 
    '''
    curr = head
    prev = None
    while curr != None: 
        tmp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = tmp  
    return prev 

def middle(head):
    '''
    Найти середину списка за O(n) без дополнительных аллокаций. Использовать метод двух указателей
    '''
    slow = head 
    fast = head 
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next 
    return slow 

def removeElem(head, val):
    '''
    Удалить элемент ноду со значением val из списка head. Удаление происходит без создания нового списка. 
    '''
    dummy = Node() 
    dummy.next = head 
    prev = dummy 
    curr = head 
    while curr != None:
        if curr.val == val:
            prev.next = curr.next 
        else:
            prev = curr 
        curr = curr.next 
        
    return dummy.next 

def is_substring(line, sub):
    '''
    Является ли строка subline подстрокой строки line 
    '''
    q = Queue() 
    for ch in sub:
        q.push(ch) 
    
    for el in line:
        if el == q.peek():
            q.pop() 

    if q.isempty():
        return True 
    return False     

def findpair(nums, target):
    '''
    Дан отсортированный массив целых чисел и таргет. Определить существуют ли два элемента, что их сумма равна таргету
    '''
    n = len(nums) 
    left = 0 
    right = n - 1
    res = False 

    while not res and left < right:
        if nums[left] + nums[right] == target:
            res = True 
        left += 1
        right -= 1
    return res 

def ispalindrom(word): 
    '''
    Дано слово. Определить является ли оно палиндромом. 
    '''
    word_size = len(word) 
    left = 0 
    right = word_size - 1
    res = True 
    while left < right: 
        if word[left] != word[right]:
            res = False 
        left += 1
        right -= 1
    return res 

def remove_duplicates(nums):
    '''
    Дан отсортированный массив целых чисел. Необходимо удалить дубликаты in-place так, чтобы каждый  элемент встречался ровно один раз 
    '''
    n = len(nums) 
    slow = 0 
    fast = 1 

    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow] 
        fast += 1
    return nums[:slow + 1]

def merge(l1, l2):
    '''
    Объединяем два отсортированных односвязных списка в один. Слияние реализуется, изменяя только ссылки между существующими узлами  
    '''
    dummy = Node() 
    tail = dummy 
    while l1 and l2:
        if l1.val < l2.val: 
            tail.next = l1 
            l1 = l1.next 
        else:
            tail.next = l2 
            l2 = l2.next 
        tail = tail.next 
    tail.next = l1 if l1 else l2 
    return dummy.next 
