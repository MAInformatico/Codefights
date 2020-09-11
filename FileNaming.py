def fileNaming(names):
    Dictionary = {}
    result = []

    for name in names:
        if (not (name in Dictionary)):
            Dictionary[name] = 1
            result.append(name)
        else:
            iterdict = name + "(" + str(Dictionary[name]) + ")"
            while (iterdict in Dictionary):
                Dictionary[name] += 1
                iterdict = name + "(" + str(Dictionary[name]) + ")"
            Dictionary[name] += 1
            Dictionary[iterdict] = 1
            result.append(iterdict)

    return result
