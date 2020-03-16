def longestWord(text):
    longest = []
    currentword = []
    for i in text:
        if ord("A") <= ord(i) <= ord("Z") or ord("a") <= ord(i) <= ord("z"):
            currentword.append(i)
        else:
            if len(currentword) > len(longest):
                longest = currentword
            currentword = []
    if len(currentword) > len(longest):
        longest = currentword
    return "".join(longest)
