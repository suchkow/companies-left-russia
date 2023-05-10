def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x >= 0 and x < 10:
        return True
    else:
        size = len(str(x))
        rev = ''

        while size != 0:
            rev += str(x)[size - 1]
            size -= 1   

        for i, j in zip(str(x), rev):
            if i != j:
                return False
    return True

number = int(input())
print(isPalindrome(number))