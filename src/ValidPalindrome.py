def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        while left < right and not isAlphanumeric(s[left]):
            left += 1
        while right>left and not isAlphanumeric(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left=left+1
        right=right-1
    return True

def isAlphanumeric(s):
    return (ord('a') <= ord(s) <= ord('z')
    or ord('0')<=ord(s)<= ord('9') or ord('A') <= ord(s) <= ord('Z'))


if __name__ == "__main__":
    print(isPalindrome('raceacar'))
