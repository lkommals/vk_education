import pytest
from hw import binarySearchSqrt, copyTime, feedAnimals, extraLetter, twoSum

def test_binarySearchSqrt():
    assert binarySearchSqrt(0) == 0
    assert binarySearchSqrt(1) == 1
    assert binarySearchSqrt(2) == 1
    assert binarySearchSqrt(3) == 1
    assert binarySearchSqrt(4) == 2
    assert binarySearchSqrt(15) == 3
    assert binarySearchSqrt(16) == 4
    assert binarySearchSqrt(17) == 4
    assert binarySearchSqrt(100) == 10
    assert binarySearchSqrt(101) == 10

def test_copyTime():
    assert copyTime(1, 1, 2) == 1
    assert copyTime(1, 5, 7) == 5
    assert copyTime(2, 1, 1) == 2
    assert copyTime(2, 1, 2) == 2
    assert copyTime(2, 3, 5) == 6
    assert copyTime(3, 1, 1) == 2
    assert copyTime(4, 1, 2) == 3
    assert copyTime(5, 2, 3) == 8
    assert copyTime(10, 2, 2) == 12
    assert copyTime(100, 1, 1) == 51
    assert copyTime(5, 2, 3) == copyTime(5, 3, 2)

def test_feedAnimals():
    animals = [5, 3, 2]
    food = [1, 2, 3, 4, 5]
    assert feedAnimals(animals, food) == 3
    animals = [10, 20, 30]
    food = [5, 15, 25]
    assert feedAnimals(animals, food) == 2  
    animals = [1, 1, 1]
    food = [1, 1]
    assert feedAnimals(animals, food) == 2
    animals = []
    food = [1,2,3]
    assert feedAnimals(animals, food) == 0
    animals = [5,5,5]
    food = []
    assert feedAnimals(animals, food) == 0

def test_extraLetter():
    assert extraLetter("abcd", "abcde") == 'e'
    assert extraLetter("a", "aa") == 'a'
    assert extraLetter("", "x") == 'x'
    assert extraLetter("hello", "helloo") == 'o'
    assert extraLetter("xyz", "xyzz") == 'z'
    assert extraLetter("abc", "cbaa") == 'a'

def test_twoSum():
    assert twoSum([2,7,11,15], 9) == [2,7]
    assert twoSum([3,2,4], 6) == [2,4]
    assert twoSum([3,3], 6) == [3,3]
    assert twoSum([1,2,3,4], 8) == []
    assert twoSum([5], 5) == []
