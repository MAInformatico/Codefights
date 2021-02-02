def transposeDictionary(scriptByExtension):
    return sorted([[i[1], i[0]] for i in scriptByExtension.items()])
