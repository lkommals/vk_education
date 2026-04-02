

def binarySearchSqrt(num: int): 
    if num == 0:
        return 0 
    l, r = 0, num
    while l < r:
        mid = (l + r + 1) // 2
        if mid * mid <= num:
            l = mid
        else:
            r = mid - 1
    return l

def copyTime(n, x, y): 
    if n == 1:  
        return min(x, y)
    l, r = 0, (n - 1) * min(x, y)
    while l < r:
        mid = (l + r) // 2
        if (mid // x) + (mid // y) >= n - 1:
            r = mid
        else:
            l = mid + 1
    return l + min(x, y)

def feedAnimals(animals, food): 
    if len(animals) == 0 or len(food) == 0: 
        return 0 
    
    animals = sorted(animals)
    food = sorted(food) 

    count = 0 
    for f in food: 
        if f >= animals[count]:
            count += 1 
        
        if count >= len(animals):
            break 
    return count 

def extraLetter(a, b): 
    a = str(a) 
    b = str(b) 
    res = 0
    for ch in (a + b): 
        res ^= ord(ch) 
    return chr(res) 

def twoSum(data, target): 
    cache = dict() 
    for i in range(len(data)):
        val = target - data[i] 
        if val in cache: 
            return [val, data[i]] 
        cache[data[i]] = i 
    return []      
        