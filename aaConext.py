from ast import Slice
import pyautogui
import os, random
import re
import time
from datetime import datetime


################################################################################
# CONST variables
################################################################################
# ableton display
SLEEP_TIME = 1

POSITION_CENTER = (1023, 543)

POSITION_FILE = (18, 39)
POSITION_COLLECT = (18, 300)
POSITION_OPEN = (18, 89)

POSITION_CREATE = (100, 36)
POSITION_IMPORT = (178, 487)

def add_position(loc, diff):
    return tuple(map(sum, zip(loc, diff)))

LOC_FRONT_DIFF = (0, 20)
LOC_SEL_DIFF = (10, 100)

POSITION_LOC_2 = (650, 181)
POSITION_LOC_2_FRONT = add_position(POSITION_LOC_2, LOC_FRONT_DIFF)
POSITION_LOC_2_SEL = add_position(POSITION_LOC_2, LOC_SEL_DIFF)

POSITION_LOC_3 = (920, 181)
POSITION_LOC_3_FRONT = add_position(POSITION_LOC_3, LOC_FRONT_DIFF)
POSITION_LOC_3_SEL = add_position(POSITION_LOC_3, LOC_SEL_DIFF)

POSITION_TEMPO = (126, 73)
POSITION_INSTR = (1553, 208)
POSITION_TRACK = (1481, 224)
POSITION_RESET = (777, 78)

POSITION_PREWARP = (1069, 207)
POSITION_WARP = (265, 927)


# ableton functions; !display must be full-size
def ableton_open_path(path):
    click(POSITION_CREATE)
    click(POSITION_IMPORT) 
    type_url(path)

def ableton_focus_instrument():
    click(POSITION_INSTR)
    click(POSITION_RESET)

def ableton_change_tempo(bpm):
    click(POSITION_TEMPO)
    for c in bpm:
        pyautogui.typewrite(c)
    pyautogui.typewrite('\n')

def ableton_select_template(root, b):
    tp_bpm_path = root + b
    tp_dir_name = '\%s'%grab_rand_file(tp_bpm_path)

    tp_path = tp_bpm_path + tp_dir_name
    prj_name = '\%s'%grab_rand_file(tp_path)

    prj_path = tp_path + prj_name
    als_name = prj_name[:-8] + ".als"
    als_path = prj_path + als_name
    return als_path

def ableton_select_template2(root, b):
    tp_bpm_path = root + b
    tp_dir_name = '\%s'%grab_rand_file(tp_bpm_path)

    tp_path = tp_bpm_path + tp_dir_name
    prj_name = '\%s'%grab_rand_file(tp_path)

    prj_path = tp_path + prj_name
    als_name = prj_name[:-8] + ".als"

    click(POSITION_CENTER)
    sleep(SLEEP_TIME)
    click(POSITION_FILE)
    sleep(SLEEP_TIME)
    click(POSITION_OPEN)

    sleep(SLEEP_TIME)
    pyautogui.typewrite(als_name[1:], interval = 0.01)
    sleep(SLEEP_TIME)
    type_url(prj_path)
    pyautogui.hotkey("alt", "o")
    sleep(20)

def ableton_unwarp():
    doubleClick(POSITION_PREWARP)
    click(POSITION_WARP)

# slice functions
def ableton_slice():
    click(POSITION_PREWARP)
    click(POSITION_RESET)
    slice_verse()

def slice_verse():
    # separate the verse section
    click(POSITION_LOC_2)
    rightClick()
    click(POSITION_LOC_2_SEL)
    pyautogui.hotkey("ctrl", "e")
    
    # erase the remainder and duplicate the verse
    click(POSITION_LOC_3_FRONT)
    pyautogui.hotkey('backspace')
    click(POSITION_LOC_2_FRONT)
    pyautogui.hotkey("ctrl", "d")
    pyautogui.hotkey("ctrl", "d")

def ableton_extract(path, name):
    # save
    click(POSITION_CENTER)
    pyautogui.hotkey("ctrl", "shift", "s")
    sleep(SLEEP_TIME)
    pyautogui.typewrite(name, interval = 0.01)
    sleep(SLEEP_TIME)
    type_url(path)

    # collect
    pyautogui.hotkey("alt", "s")
    sleep(10)
    click(POSITION_FILE)
    click(POSITION_COLLECT)
    sleep(SLEEP_TIME + 1)
    pyautogui.hotkey("Enter")
    sleep(10)

    # extract
    pyautogui.hotkey("ctrl", "shift", "r")
    pyautogui.hotkey("Enter")

    pyautogui.typewrite(name, interval = 0.01)
    sleep(SLEEP_TIME)
    type_url(path)
    pyautogui.hotkey("alt", "s")
    sleep(75)
    


# automation functions
def click(loc):
    pyautogui.click(loc, interval = 0.1)

def doubleClick(loc):
    pyautogui.doubleClick(loc, interval = 0.1)

def rightClick():
    pyautogui.click(button="right")

def grab_rand_file(path):
    return random.choice(os.listdir(path))

def grab_first_num(str):
    return re.search(r'\d+', str).group()

def sleep(interval):
    time.sleep(interval)

def position():
    print(pyautogui.position())
    exit()

def type_url(path):
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite(path, interval = 0.01)
    sleep(SLEEP_TIME)
    pyautogui.press("Enter")
    
def do_file(name):
    pyautogui.hotkey('alt', 'n')
    pyautogui.typewrite(name, interval = 0.01)
    sleep(SLEEP_TIME)
    pyautogui.press("Enter")

def get_time():
    now = datetime.now()
    return now.strftime("%H_%M_%S")



    
def open_file(file_path):
    pyautogui.press("win")
    pyautogui.typewrite(file_path, interval = 0.01)
    pyautogui.press("Enter")
    sleep(20)
