import time
import Emergency as emg
import threading
import Data as data
import TimeSlice as calculate
import Timer as server

def begin_emergency():
    emgr = threading.Thread(target=emg.emergency_detect, args=[])
    emgr.start()

def emulate():
    i = 0
    while True:
        if server.active:
            server.kill_flag = emg.flag
        elif len(data.ev_queue) == 0 and not server.active:
            service_time = calculate.time_slice(data.traffic[i])
            print('Service Time:', service_time, 'seconds')
            emg.flag = False
            normal_set = threading.Thread(target = server.emulated_sleep, args=[service_time, i, emg])
            normal_set.start()
            i = (i + 1) % 4
        else:
            side = data.ev_queue.pop(0)
            service_time = 30
            emergency_set = threading.Thread(target=server.emulated_sleep, args=[service_time, side])
            emergency_set.start()


begin_emergency()
emulate()

