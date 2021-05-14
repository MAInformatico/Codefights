def roadsBuilding(cities, roads):
    cities_visited = set()
    result = []

    for i in roads:
        x = i[0] if i[0] < i[1] else i[1]
        y = i[1] if i[1] > i[0] else i[0]

        cities_visited.add((x, y))

    for city in range(cities):
        for route in range(cities):
            if city != route:
                x = city if city < route else route
                y = route if route > city else city

                if (x, y) not in cities_visited:
                    cities_visited.add((x, y))
                    result.append([x, y])

    return result
