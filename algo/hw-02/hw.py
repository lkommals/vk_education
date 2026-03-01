
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
        