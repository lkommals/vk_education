from hw import (
    reverse_by_indexes,
    rotate_array,
    merge,
    merge_without_allocations,
    zeros_ones_sort,
    netherland_flags,
    reverse_evens,
    zeros_last,
)
def test_reverse_by_indexes_normal():
    arr = [1, 2, 3, 4, 5]
    reverse_by_indexes(arr, 1, 3)
    assert arr == [1, 4, 3, 2, 5]
    print("Пройден тест: test_reverse_by_indexes_normal")

def test_reverse_by_indexes_single():
    arr = [1, 2, 3]
    reverse_by_indexes(arr, 1, 1)
    assert arr == [1, 2, 3]
    print("Пройден тест: test_reverse_by_indexes_single")

def test_reverse_by_indexes_left_greater():
    arr = [1, 2, 3]
    reverse_by_indexes(arr, 2, 1)
    assert arr == [1, 2, 3]
    print("Пройден тест: test_reverse_by_indexes_left_greater")

def test_reverse_by_indexes_full():
    arr = [1, 2, 3, 4]
    reverse_by_indexes(arr, 0, 3)
    assert arr == [4, 3, 2, 1]
    print("Пройден тест: test_reverse_by_indexes_full")

def test_reverse_by_indexes_error_left_negative():
    arr = [1, 2, 3]
    try:
        reverse_by_indexes(arr, -1, 1)
        assert False, "Expected IndexError"
    except IndexError:
        pass
    print("Пройден тест: test_reverse_by_indexes_error_left_negative")

def test_reverse_by_indexes_error_right_out():
    arr = [1, 2, 3]
    try:
        reverse_by_indexes(arr, 1, 3)
        assert False, "Expected IndexError"
    except IndexError:
        pass
    print("Пройден тест: test_reverse_by_indexes_error_right_out")

def test_rotate_normal():
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 2)
    assert arr == [4, 5, 1, 2, 3]
    print("Пройден тест: test_rotate_normal")

def test_rotate_zero():
    arr = [1, 2, 3]
    rotate_array(arr, 0)
    assert arr == [1, 2, 3]
    print("Пройден тест: test_rotate_zero")

def test_rotate_full_length():
    arr = [1, 2, 3]
    rotate_array(arr, 3)
    assert arr == [1, 2, 3]
    print("Пройден тест: test_rotate_full_length")

def test_rotate_greater_than_length():
    arr = [1, 2, 3, 4]
    rotate_array(arr, 6)
    assert arr == [3, 4, 1, 2]
    print("Пройден тест: test_rotate_greater_than_length")

def test_rotate_negative():
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, -2)
    assert arr == [3, 4, 5, 1, 2]
    print("Пройден тест: test_rotate_negative")

def test_rotate_empty():
    arr = []
    rotate_array(arr, 3)
    assert arr == []
    print("Пройден тест: test_rotate_empty")

def test_merge_both_non_empty():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    print("Пройден тест: test_merge_both_non_empty")

def test_merge_one_empty():
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]
    print("Пройден тест: test_merge_one_empty")

def test_merge_both_empty():
    assert merge([], []) == []
    print("Пройден тест: test_merge_both_empty")

def test_merge_duplicates():
    assert merge([1, 2, 2, 5], [2, 3, 4]) == [1, 2, 2, 2, 3, 4, 5]
    print("Пройден тест: test_merge_duplicates")

def test_merge_different_lengths():
    assert merge([1, 4, 7, 10], [2, 3]) == [1, 2, 3, 4, 7, 10]
    print("Пройден тест: test_merge_different_lengths")

def test_merge_without_normal():
    arr1 = [1, 3, 5, 0, 0, 0]
    arr2 = [2, 4, 6]
    result = merge_without_allocations(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]
    print("Пройден тест: test_merge_without_normal")

def test_merge_without_arr2_empty():
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_without_allocations(arr1, arr2)
    assert result == [1, 2, 3]
    print("Пройден тест: test_merge_without_arr2_empty")

def test_merge_without_arr1_zeros():
    arr1 = [0, 0, 0]
    arr2 = [1, 2, 3]
    result = merge_without_allocations(arr1, arr2)
    assert result == [1, 2, 3]
    print("Пройден тест: test_merge_without_arr1_zeros")

def test_merge_without_duplicates():
    arr1 = [1, 2, 4, 0, 0]
    arr2 = [2, 3]
    result = merge_without_allocations(arr1, arr2)
    assert result == [1, 2, 2, 3, 4]
    print("Пройден тест: test_merge_without_duplicates")

def test_zeros_ones_mixed():
    arr = [1, 0, 1, 0, 1]
    zeros_ones_sort(arr)
    assert arr == [0, 0, 1, 1, 1]
    print("Пройден тест: test_zeros_ones_mixed")

def test_zeros_ones_all_zeros():
    arr = [0, 0, 0]
    zeros_ones_sort(arr)
    assert arr == [0, 0, 0]
    print("Пройден тест: test_zeros_ones_all_zeros")

def test_zeros_ones_all_ones():
    arr = [1, 1, 1]
    zeros_ones_sort(arr)
    assert arr == [1, 1, 1]
    print("Пройден тест: test_zeros_ones_all_ones")

def test_zeros_ones_empty():
    arr = []
    zeros_ones_sort(arr)
    assert arr == []
    print("Пройден тест: test_zeros_ones_empty")

def test_netherland_mixed():
    arr = [2, 0, 1, 2, 1, 0]
    netherland_flags(arr)
    assert arr == [0, 0, 1, 1, 2, 2]
    print("Пройден тест: test_netherland_mixed")

def test_netherland_all_zeros():
    arr = [0, 0, 0]
    netherland_flags(arr)
    assert arr == [0, 0, 0]
    print("Пройден тест: test_netherland_all_zeros")

def test_netherland_all_ones():
    arr = [1, 1, 1]
    netherland_flags(arr)
    assert arr == [1, 1, 1]
    print("Пройден тест: test_netherland_all_ones")

def test_netherland_all_twos():
    arr = [2, 2, 2]
    netherland_flags(arr)
    assert arr == [2, 2, 2]
    print("Пройден тест: test_netherland_all_twos")

def test_netherland_sorted():
    arr = [0, 0, 1, 1, 2, 2]
    netherland_flags(arr)
    assert arr == [0, 0, 1, 1, 2, 2]
    print("Пройден тест: test_netherland_sorted")

def test_netherland_reverse():
    arr = [2, 2, 1, 1, 0, 0]
    netherland_flags(arr)
    assert arr == [0, 0, 1, 1, 2, 2]
    print("Пройден тест: test_netherland_reverse")

def test_reverse_evens_normal():
    arr = [1, 2, 3, 4, 5, 6]
    reverse_evens(arr)
    assert arr == [2, 4, 6, 1, 3, 5]
    print("Пройден тест: test_reverse_evens_normal")

def test_reverse_evens_all_evens():
    arr = [2, 4, 6]
    reverse_evens(arr)
    assert arr == [2, 4, 6]
    print("Пройден тест: test_reverse_evens_all_evens")

def test_reverse_evens_all_odds():
    arr = [1, 3, 5]
    reverse_evens(arr)
    assert arr == [1, 3, 5]
    print("Пройден тест: test_reverse_evens_all_odds")

def test_reverse_evens_with_zeros():
    arr = [1, 0, 2, 3, 0, 4]
    reverse_evens(arr)
    assert arr == [0, 2, 0, 4, 1, 3]
    print("Пройден тест: test_reverse_evens_with_zeros")

def test_reverse_evens_stability():
    arr = [1, 2, 2, 3, 4, 1]
    reverse_evens(arr)
    assert arr == [2, 2, 4, 1, 3, 1]
    print("Пройден тест: test_reverse_evens_stability")

def test_zeros_last_normal():
    arr = [4, 0, 0, 6, 1, 8, 1, 10, 0]
    zeros_last(arr)
    assert arr == [4, 6, 1, 8, 1, 10, 0, 0, 0]
    print("Пройден тест: test_zeros_last_normal")

def test_zeros_last_all_zeros():
    arr = [0, 0, 0]
    zeros_last(arr)
    assert arr == [0, 0, 0]
    print("Пройден тест: test_zeros_last_all_zeros")

def test_zeros_last_no_zeros():
    arr = [1, 2, 3]
    zeros_last(arr)
    assert arr == [1, 2, 3]
    print("Пройден тест: test_zeros_last_no_zeros")

def test_zeros_last_empty():
    arr = []
    zeros_last(arr)
    assert arr == []
    print("Пройден тест: test_zeros_last_empty")

def test_zeros_last_stability():
    arr = [0, 2, 1, 0, 3, 0]
    zeros_last(arr)
    assert arr == [2, 1, 3, 0, 0, 0]
    print("Пройден тест: test_zeros_last_stability")

def run_all_tests():
    tests = [
        test_reverse_by_indexes_normal,
        test_reverse_by_indexes_single,
        test_reverse_by_indexes_left_greater,
        test_reverse_by_indexes_full,
        test_reverse_by_indexes_error_left_negative,
        test_reverse_by_indexes_error_right_out,
        test_rotate_normal,
        test_rotate_zero,
        test_rotate_full_length,
        test_rotate_greater_than_length,
        test_rotate_negative,
        test_rotate_empty,
        test_merge_both_non_empty,
        test_merge_one_empty,
        test_merge_both_empty,
        test_merge_duplicates,
        test_merge_different_lengths,
        test_merge_without_normal,
        test_merge_without_arr2_empty,
        test_merge_without_arr1_zeros,
        test_merge_without_duplicates,
        test_zeros_ones_mixed,
        test_zeros_ones_all_zeros,
        test_zeros_ones_all_ones,
        test_zeros_ones_empty,
        test_netherland_mixed,
        test_netherland_all_zeros,
        test_netherland_all_ones,
        test_netherland_all_twos,
        test_netherland_sorted,
        test_netherland_reverse,
        test_reverse_evens_normal,
        test_reverse_evens_all_evens,
        test_reverse_evens_all_odds,
        test_reverse_evens_with_zeros,
        test_reverse_evens_stability,
        test_zeros_last_normal,
        test_zeros_last_all_zeros,
        test_zeros_last_no_zeros,
        test_zeros_last_empty,
        test_zeros_last_stability,
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