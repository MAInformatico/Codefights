def chessBoardCellColor(cell1, cell2):    
    pos1 = int(cell1, 32)
    pos2 = int(cell2, 32)
    if (pos1//32)%2 == (pos2//32)%2 and pos1%2 == pos2%2:
        return bool(1)
    if (pos1//32)%2 != (pos2//32)%2 and pos1%2 != pos2%2:
        return bool(1)
    return bool(0)
