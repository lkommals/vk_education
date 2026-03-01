
class Node:
    def __init__(self, val):
        self.next = None 
        self.val = val 

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
    if head.val == val: 
        res = head.next 
        head.next = None
        return res  
    else: 
        curr = head 
        prev = curr 
        while curr != None and curr.val != val:
            prev = curr 
            curr = curr.next 
        if curr != None: 
            prev.next = curr.next 
            curr.next = curr 
        return head 


