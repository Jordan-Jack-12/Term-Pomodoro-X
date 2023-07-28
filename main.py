import time
import os
import csv
from datetime import date

# Clear screen
os.system('cls')

# Global variable
is_work = False
is_rest = False
current_interval = 1

# Welcom Text with aksing for inputs
def print_welcome_text():
    print(r"""
        
    __________                         .___                    ____  ___
    \______   \____   _____   ____   __| _/___________  ____   \   \/  /
    |     ___/  _ \ /     \ /  _ \ / __ |/  _ \_  __ \/  _ \   \     / 
    |    |  (  <_> )  Y Y  (  <_> ) /_/ (  <_> )  | \(  <_> )  /     \ 
    |____|   \____/|__|_|  /\____/\____ |\____/|__|   \____/  /___/\  \
                        \/            \/                           \_/

    """)
    print("\x1b[1;31;40mNote : This is strict pomodoro you can not pause once timer starts.\x1b[0m")

# Asking the input for focus time, rest time and interval    
def input_time_interval():
    pass

# App start from here
print_welcome_text()
input_time_interval()

print("Focus time")
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

# Print time in proper format
def print_time(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))

# write to csv file with date and focused time
def save_session():
    today_session_seconds = (set_hh_work*3600 + set_mm_work*60 + set_ss_work) * current_interval
    time_proper_format = time.strftime('%H:%M:%S', time.gmtime(today_session_seconds))
    today_date = str(date.today())
    write_session = [today_date, time_proper_format]
    if os.path.isfile('database.csv') == True:
        with open('database.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(write_session)
    else:
        pass

while interval_total > 0:
    # initializing values from input
    time_work = set_hh_work*3600 + set_mm_work*60 + set_ss_work
    time_short_rest = set_mm_short_rest*60 + set_ss_short_rest
    time_long_rest = set_mm_long_rest*60 + set_ss_long_rest
    long_break_here = current_interval%set_long_break_interval

    if is_work == True and is_rest == False:
        while time_work > 0:
            print('\x1b[1;32;40m========Focus======== \x1b[0m')
            print("\x1b[1;32;40m||    ", print_time(time_work), "   ||\x1b[0m")
            print("\x1b[1;32;40m=====================\x1b[0m")
            time_work -= 1
            time.sleep(1)
            os.system('cls')
        is_work = False
        is_rest = True
        current_interval += 1
        confirm_rest = input("Start rest (y/n): ")
        if confirm_rest == 'y':
            pass
        else:
            save_session()
    elif is_work == False and is_rest == True:
        if long_break_here == 0:
            while time_long_rest > 0:
                print("=====Long Break======")
                print("||    ",print_time(time_long_rest), "   ||")
                print("=====================")
                time_long_rest -= 1
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
            save_session()
    interval_total -= 1

# Saving session in csv file
save_session()

# Asking for exit or stay
def conf_exit():
    confirm_exit = input("Do you want to exit? (y/n) : ")
    if confirm_exit == 'y' or conf_exit == 'Y':
        quit()
    elif confirm_exit == 'n' or conf_exit == 'N':
        print_welcome_text()
    else:
        conf_exit()

conf_exit()






