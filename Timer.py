import time
import Buffer

active = False
rem_time = 0
rem_dir = -1
kill_flag = False

def emulated_sleep(time_slice, direction):
    global kill_flag
    kill_flag = False

    global active
    active = True

    Buffer.set(direction)
    start = time.time()

    while not kill_flag:
        stop = time.time()
        if stop - start >= time_slice:
            break

    stop = time.time()

    run_time = stop - start
    active = False
    print('Served time:' ,int(run_time), 'seconds')

    global rem_time
    global rem_dir

    if run_time + 5 < time_slice:
        rem_time = time_slice - run_time
        rem_dir = direction

    else:
        rem_time = 0
        rem_dir = -1
