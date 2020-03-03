def evenDigitsOnly(n):
    check = [int(i)%2 == 0 for i in str(n)]
    if False in check:
        return False
    else:
        return True
