def solution(cacheSize, cities):
    time = 0
    cache = {}
    for (idx, item) in enumerate(cities):
        lower = item.lower()
        if lower in cache:
            cache[lower] = idx
            time += 1
        else:
            time += 5
            if cacheSize == 0:
                continue

            if len(cache) < cacheSize:
                cache[lower] = idx
            else:
                sort_cache = sorted(cache.items(), key=lambda item: item[1])
                first = sort_cache[0]
                del cache[first[0]]
                cache[lower] = idx

    return time


if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                       "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
                       "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                       "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                       "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
