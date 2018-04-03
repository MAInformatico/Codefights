from itertools import product

def pressingButtons(buttons):
    Teclado = [""   ,""    ,"abc","def" ,"ghi","jkl",
              "mno","pqrs","tuv","wxyz"]
    Array = [Teclado[int(num)] for num in buttons]

    return [''.join(s) for s in product(*Array) if s]
