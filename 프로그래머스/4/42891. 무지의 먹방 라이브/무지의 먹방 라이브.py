def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food = []
    for i, t in enumerate(food_times):
        food.append((t, i + 1))
    food.sort()

    previous = 0
    length = len(food_times)
    for i, (time, _) in enumerate(food):
        diff = time - previous
        if diff != 0:
            spend = diff * length
            if spend <= k:
                k -= spend
                previous = time
            else:
                result = sorted(food[i:], key=lambda x: x[1])
                return result[k % length][1]
        length -= 1
    return -1