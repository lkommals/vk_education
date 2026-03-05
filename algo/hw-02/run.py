from hw import (Node, Queue, reverse_node, middle, removeElem,
                  is_substring, findpair, ispalindrom, remove_duplicates, merge)

def list_to_nodes(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def nodes_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def test_reverse_node_empty():
    assert reverse_node(None) is None
    print("Пройден тест: test_reverse_node_empty")

def test_reverse_node_single():
    head = Node(1)
    new_head = reverse_node(head)
    assert new_head.val == 1
    assert new_head.next is None
    print("Пройден тест: test_reverse_node_single")

def test_reverse_node_multiple():
    head = list_to_nodes([1, 2, 3, 4, 5])
    new_head = reverse_node(head)
    assert nodes_to_list(new_head) == [5, 4, 3, 2, 1]
    print("Пройден тест: test_reverse_node_multiple")

def test_middle_empty():
    assert middle(None) is None
    print("Пройден тест: test_middle_empty")

def test_middle_odd():
    head = list_to_nodes([1, 2, 3, 4, 5])
    mid = middle(head)
    assert mid.val == 3
    print("Пройден тест: test_middle_odd")

def test_middle_even():
    head = list_to_nodes([1, 2, 3, 4])
    mid = middle(head)
    assert mid.val == 3
    print("Пройден тест: test_middle_even")

def test_removeElem_empty():
    assert removeElem(None, 5) is None
    print("Пройден тест: test_removeElem_empty")

def test_removeElem_head():
    head = list_to_nodes([1, 2, 3])
    new_head = removeElem(head, 1)
    assert nodes_to_list(new_head) == [2, 3]
    print("Пройден тест: test_removeElem_head")

def test_removeElem_middle():
    head = list_to_nodes([1, 2, 3, 4])
    new_head = removeElem(head, 3)
    assert nodes_to_list(new_head) == [1, 2, 4]
    print("Пройден тест: test_removeElem_middle")

def test_removeElem_tail():
    head = list_to_nodes([1, 2, 3])
    new_head = removeElem(head, 3)
    assert nodes_to_list(new_head) == [1, 2]
    print("Пройден тест: test_removeElem_tail")

def test_removeElem_multiple():
    head = list_to_nodes([2, 2, 1, 2, 3])
    new_head = removeElem(head, 2)
    assert nodes_to_list(new_head) == [1, 3]
    print("Пройден тест: test_removeElem_multiple")

def test_removeElem_not_found():
    head = list_to_nodes([1, 2, 3])
    new_head = removeElem(head, 99)
    assert nodes_to_list(new_head) == [1, 2, 3]
    print("Пройден тест: test_removeElem_not_found")

def test_is_substring_empty_sub():
    assert is_substring("abc", "") == True
    print("Пройден тест: test_is_substring_empty_sub")

def test_is_substring_empty_line():
    assert is_substring("", "abc") == False
    print("Пройден тест: test_is_substring_empty_line")

def test_is_substring_true():
    assert is_substring("abcde", "ace") == True
    print("Пройден тест: test_is_substring_true")

def test_is_substring_false():
    assert is_substring("abcde", "aec") == False
    print("Пройден тест: test_is_substring_false")

def test_is_substring_contiguous():
    assert is_substring("hello world", "world") == True
    assert is_substring("hello world", "word") == True
    print("Пройден тест: test_is_substring_contiguous")

def test_findpair_empty():
    assert findpair([], 10) == False
    print("Пройден тест: test_findpair_empty")

def test_findpair_single():
    assert findpair([5], 5) == False
    print("Пройден тест: test_findpair_single")

def test_findpair_pair_at_ends():
    assert findpair([1, 2, 3, 4], 5) == True
    assert findpair([1, 2, 3, 4], 6) == False
    print("Пройден тест: test_findpair_pair_at_ends")

def test_findpair_pair_adjacent():
    assert findpair([1, 2, 3, 4], 3) == False
    print("Пройден тест: test_findpair_pair_adjacent")

def test_findpair_longer():
    arr = [1, 2, 3, 4, 5]
    assert findpair(arr, 6) == True
    assert findpair(arr, 7) == False
    print("Пройден тест: test_findpair_longer")

def test_ispalindrom_empty():
    assert ispalindrom("") == True
    print("Пройден тест: test_ispalindrom_empty")

def test_ispalindrom_single():
    assert ispalindrom("a") == True
    print("Пройден тест: test_ispalindrom_single")

def test_ispalindrom_even():
    assert ispalindrom("abba") == True
    assert ispalindrom("abca") == False
    print("Пройден тест: test_ispalindrom_even")

def test_ispalindrom_odd():
    assert ispalindrom("racecar") == True
    assert ispalindrom("hello") == False
    print("Пройден тест: test_ispalindrom_odd")

def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []
    print("Пройден тест: test_remove_duplicates_empty")

def test_remove_duplicates_no_dup():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    print("Пройден тест: test_remove_duplicates_no_dup")

def test_remove_duplicates_all_dup():
    assert remove_duplicates([1, 1, 1]) == [1]
    print("Пройден тест: test_remove_duplicates_all_dup")

def test_remove_duplicates_mixed():
    assert remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    print("Пройден тест: test_remove_duplicates_mixed")

def test_remove_duplicates_negative():
    assert remove_duplicates([-2, -2, -1, 0, 0, 1]) == [-2, -1, 0, 1]
    print("Пройден тест: test_remove_duplicates_negative")

def test_merge_both_empty():
    assert merge(None, None) is None
    print("Пройден тест: test_merge_both_empty")

def test_merge_one_empty():
    l2 = list_to_nodes([1, 2, 3])
    merged = merge(None, l2)
    assert nodes_to_list(merged) == [1, 2, 3]

    l1 = list_to_nodes([4, 5])
    merged = merge(l1, None)
    assert nodes_to_list(merged) == [4, 5]
    print("Пройден тест: test_merge_one_empty")

def test_merge_interleaved():
    l1 = list_to_nodes([1, 3, 5])
    l2 = list_to_nodes([2, 4, 6])
    merged = merge(l1, l2)
    assert nodes_to_list(merged) == [1, 2, 3, 4, 5, 6]
    print("Пройден тест: test_merge_interleaved")

def test_merge_one_exhausted():
    l1 = list_to_nodes([1, 2])
    l2 = list_to_nodes([3, 4, 5])
    merged = merge(l1, l2)
    assert nodes_to_list(merged) == [1, 2, 3, 4, 5]
    print("Пройден тест: test_merge_one_exhausted")

def test_merge_duplicates():
    l1 = list_to_nodes([1, 2, 2, 3])
    l2 = list_to_nodes([2, 3, 4])
    merged = merge(l1, l2)
    assert nodes_to_list(merged) == [1, 2, 2, 2, 3, 3, 4]
    print("Пройден тест: test_merge_duplicates")

def test_merge_negative():
    l1 = list_to_nodes([-5, -1, 0])
    l2 = list_to_nodes([-3, 2])
    merged = merge(l1, l2)
    assert nodes_to_list(merged) == [-5, -3, -1, 0, 2]
    print("Пройден тест: test_merge_negative")

def run_all_tests():
    tests = [
        test_reverse_node_empty,
        test_reverse_node_single,
        test_reverse_node_multiple,
        test_middle_empty,
        test_middle_odd,
        test_middle_even,
        test_removeElem_empty,
        test_removeElem_head,
        test_removeElem_middle,
        test_removeElem_tail,
        test_removeElem_multiple,
        test_removeElem_not_found,
        test_is_substring_empty_sub,
        test_is_substring_empty_line,
        test_is_substring_true,
        test_is_substring_false,
        test_is_substring_contiguous,
        test_findpair_empty,
        test_findpair_single,
        test_findpair_pair_at_ends,
        test_findpair_pair_adjacent,
        test_findpair_longer,
        test_ispalindrom_empty,
        test_ispalindrom_single,
        test_ispalindrom_even,
        test_ispalindrom_odd,
        test_remove_duplicates_empty,
        test_remove_duplicates_no_dup,
        test_remove_duplicates_all_dup,
        test_remove_duplicates_mixed,
        test_remove_duplicates_negative,
        test_merge_both_empty,
        test_merge_one_empty,
        test_merge_interleaved,
        test_merge_one_exhausted,
        test_merge_duplicates,
        test_merge_negative,
    ]

    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"{test.__name__} failed: {e}")
        except Exception as e:
            print(f"{test.__name__} raised an exception: {e}")

    print(f"\nУспешных тестов: {passed}/{len(tests)}")

if __name__ == "__main__":
    run_all_tests()