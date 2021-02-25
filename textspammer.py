import pyautogui
import time

print('''
  _______        _      _____                                           
 |__   __|      | |    / ____|                                          
    | | _____  _| |_  | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
    | |/ _ \ \/ / __|  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    | |  __/>  <| |_   ____) | |_) | (_| | | | | | | | | | | |  __/ |   
    |_|\___/_/\_ \__| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                             | |                                        
                             |_|                                        

Created by PythonX ~ ShahadathAkash
''')

start_time = int(input('[~] Time to start after (sec)\n>>> '))
file_name = str(input('[~] Which file you want to Use (comments, numbers)\nEx: comments\n[*] comments will spam random massages & numbers will spam numbers fron 1 to 5000\n>>> '))
time_delay = int(input('[~] Set time Delay (sec)\n>>> '))
print('[*] Move your Cursor to the Field you want to send SPAM texts in '+str(start_time)+ ' sec !!!')
time.sleep(start_time)


comments = open(file_name, "r")
for words in comments:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    time.sleep(time_delay)

