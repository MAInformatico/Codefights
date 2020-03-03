import re
def variableName(name):
    if re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$').match(name): return True
    else:
        return False
