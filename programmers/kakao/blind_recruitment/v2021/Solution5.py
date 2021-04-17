def to_sec(time):
    h, m, s = map(int, time.split(":"))
    return (h * 60 * 60) + (m * 60) + s


def to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60

    ret = []
    ret.append(str(h) if h > 9 else f"0{h}")
    ret.append(str(m) if m > 9 else f"0{m}")
    ret.append(str(s) if s > 9 else f"0{s}")
    return ":".join(ret)


def solution(play_time, adv_time, logs):
    play_time_sec = to_sec(play_time)
    adv_time_sec = to_sec(adv_time)
    total_time = [0] * (100 * 60 * 60)

    for log in logs:
        start, end = map(to_sec, log.split("-"))
        total_time[start] += 1
        total_time[end] -= 1

    for i in range(1, play_time_sec):  # Count
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, play_time_sec):  # Acc
        total_time[i] = total_time[i] + total_time[i - 1]

    max_time = total_time[adv_time_sec - 1]
    max_start_time = 0

    for i in range(play_time_sec - adv_time_sec):
        temp = total_time[i + adv_time_sec] - total_time[i]
        if temp > max_time:
            max_time = temp
            max_start_time = i + 1

    return to_time(max_start_time)


if __name__ == "__main__":
    ret = solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30",
        ],
    )
    print(ret)

    ret = solution(
        "99:59:59",
        "25:00:00",
        [
            "69:59:59-89:59:59",
            "01:00:00-21:00:00",
            "79:59:59-99:59:59",
            "11:00:00-31:00:00",
        ],
    )
    print(ret)

    ret = solution(
        "50:00:00",
        "50:00:00",
        ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
    )
    print(ret)
