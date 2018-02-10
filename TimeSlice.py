def time_slice(load):
    time = load / 40
    time = time * 30

    if time < 5:
        time = 5
    return int(time)