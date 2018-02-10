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
            # To continuously monitor the flags for emergency vehicles
            server.kill_flag = emg.flag
            if emg.side != -1:
                data.ev_queue.append(emg.side - 1)
            emg.side = -1

        elif len(data.ev_queue) == 0:
            # To compute the time and set the green light for the computed time
            if server.rem_dir != -1 and server.rem_time != 0:
                service_time = server.rem_time
                dir = server.rem_dir
                emg.flag = False
                rem_set = threading.Thread(target=server.emulated_sleep, args=[service_time, dir])
                rem_set.start()

            else:
                service_time = calculate.time_slice(data.traffic[i])
                print('Service Time:', service_time, 'seconds')
                emg.flag = False
                normal_set = threading.Thread(target=server.emulated_sleep, args=[service_time, i])
                normal_set.start()
                i = (i + 1) % 4

        else:
            # To set max time and allow the emergency vehicles to go first
            print ('Emergency Vehicle encountered')
            emg.flag = False
            side = data.ev_queue.pop(0)
            service_time = 5 #For testing only, change to 30s after testing ***
            emergency_set = threading.Thread(target=server.emulated_sleep, args=[service_time, side])
            emergency_set.start()


begin_emergency()
emulate()

