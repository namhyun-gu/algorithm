def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    for time, city in enumerate(cities):
        city = city.lower()

        if city not in cache:
            answer += 5

            if cacheSize > 0 and len(cache) == cacheSize:
                sortedItems = []
                for val, key in cache.items():
                    sortedItems.append((key, val))
                sortedItems.sort()
                del cache[sortedItems[0][1]]

                cache[city] = time
            elif len(cache) < cacheSize:
                cache[city] = time
        else:
            answer += 1
            cache[city] = time

    return answer


if __name__ == "__main__":
    ret = solution(
        2,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
    print(ret)

    ret = solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
    print(ret)

    ret = solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
    print(ret)