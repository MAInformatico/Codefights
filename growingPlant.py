def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight < upSpeed:
        return 1
    return int((desiredHeight - downSpeed) / (upSpeed - downSpeed) + 0.5)
