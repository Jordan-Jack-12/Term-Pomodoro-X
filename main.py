import time
import os

# Clear screen
os.system('cls')

# Global variable
is_work = False
is_rest = False
current_interval = 1
print(" Focus time")
set_hh_work = int(input("focus (hrs): "))
set_mm_work = int(input("focus (min): "))
set_ss_work = int(input("focus (sec): "))
os.system('cls')
print(" short break time")
set_mm_short_rest = int(input("short rest (min): "))
set_ss_short_rest = int(input("short rest (sec): "))
os.system('cls')
print(" Long break time ")
set_mm_long_rest = int(input("long rest (min): "))
set_ss_long_rest = int(input("long rest (sec): "))
os.system('cls')
print("total interval")
set_interval_total = int(input("number of interval : "))
os.system('cls')
print("long break interval")
set_long_break_interval = int(input("long break after ___ interval : "))
os.system('cls')
print("\/ Confirm the start \/")
confirm = input("Start (y/n) :")
if confirm == 'y':
    is_work = True
os.system('cls')

interval_total = 2*set_interval_total - 1

def print_time(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))


while interval_total > 0:
    # initializing values from input
    time_work = set_hh_work*3600 + set_mm_work*60 + set_ss_work
    time_short_rest = set_mm_short_rest*60 + set_ss_short_rest
    time_long_rest = set_mm_long_rest*60 + set_ss_long_rest
    long_break_here = current_interval%set_long_break_interval

    if is_work == True and is_rest == False:
        while time_work > 0:
            print("========Focus========")
            print("||    ", print_time(time_work), "   ||")
            print("=====================")
            time_work -= 1
            time.sleep(1)
            os.system('cls')
        is_work = False
        is_rest = True
        confirm_rest = input("Start rest (y/n): ")
        if confirm_rest == 'y':
            pass
        else:
            break
    elif is_work == False and is_rest == True:
        if long_break_here == 0:
            while time_long_rest > 0:
                print("=====Long Break=====")
                print("||    ",print_time(time_long_rest), "   ||")
                print("=====================")
                time_short_rest -= 1
                time.sleep(1)
                os.system('cls')
            is_work = True
            is_rest = False
        else:
            while time_short_rest > 0:
                print("====Short Break=====")
                print("||    ",print_time(time_short_rest), "   ||")
                print("=====================")
                time_short_rest -= 1
                time.sleep(1)
                os.system('cls')
            is_work = True
            is_rest = False
        confirm_focus = input("Start focus (y/n): ")
        if confirm_focus == 'y':
            pass
        else:
            break
    interval_total -= 1
    current_interval += 1

    






