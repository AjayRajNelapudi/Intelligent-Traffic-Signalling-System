import time
import Buffer

active = False
rem_time = 0
kill_flag = False

def emulated_sleep(time_slice, direction, emg):
    global kill_flag
    kill_flag = False

    global active
    active = True

    global rem_time

    Buffer.set(direction)
    start = time.time()

    while not kill_flag:
        stop = time.time()
        if stop - start >= time_slice:
            break

    stop = time.time()
    active = False

    run_time = stop - start
    print('Served time:' ,int(run_time), 'seconds')
    if run_time + 5 < time_slice:
        rem_time = time_slice - run_time
    else:
        rem_time = 0
