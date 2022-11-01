from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import pyautogui
import threading
from threading import Thread
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from stockfishpy.stockfishpy import *

# Init Stockfish
chessEngine = Engine(r'./stockfish_15_x64_avx2.exe', param={'Threads': 2, 'Ponder': 'true'})

# Init clipboard
root = tk.Tk()
root.withdraw()  # keep the window from showing

# Init chrome - load existing chromeprofile
# op = webdriver.ChromeOptions()
# op.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 1")
# ser = Service(r'./chromedriver.exe')
# s = webdriver.Chrome(service=ser, options=op)
#s.get("https://www.chess.com/")

# Open extension - get FEN
#time.sleep(3)
#pyautogui.click('./logo_extension.png')    
pyautogui.click('./scan_button.png')
time.sleep(3)
pyautogui.click('./copy.png')
fen = root.clipboard_get()
print(fen)

## Get best moves
chessEngine.ucinewgame()
chessEngine.setposition(fen)
move = chessEngine.bestmove()
time.sleep(2)
move_full = move['bestmove']
move1 = move_full[0:1]
move2 = move_full[1:2]
move3 = move_full[2:3]
move4 = move_full[3:4]
print(move1)
print(move2)
print(move3)
print(move4)

## Board cordinates
x_root = 275
y_root = 1055  
distance = 1055 - 928

if (move1 == "a"):
	x_before = x_root

if (move1 == "b"):
	x_before = x_root + distance

if (move1 == "c"):
	x_before = x_root + distance*2

if (move1 == "d"):
	x_before = x_root + distance*3

if (move1 == "e"):
	x_before = x_root + distance*4

if (move1 == "f"):
	x_before = x_root + distance*5

if (move1 == "g"):
	x_before = x_root + distance*6

if (move1 == "h"):
	x_before = x_root + distance*7

y_before = y_root - distance*(int(move2)-1)

if (move3 == "a"):
	x_after = x_root

if (move3 == "b"):
	x_after = x_root + distance

if (move3 == "c"):
	x_after = x_root + distance*2

if (move3 == "d"):
	x_after = x_root + distance*3

if (move3 == "e"):
	x_after = x_root + distance*4

if (move3 == "f"):
	x_after = x_root + distance*5

if (move3 == "g"):
	x_after = x_root + distance*6

if (move3 == "h"):
	x_after = x_root + distance*7

y_after = y_root - distance*(int(move4)-1)

print(x_before)
print(y_before)
print(x_after)
print(y_after)


pyautogui.moveTo(x_before,y_before)
pyautogui.click(x_before,y_before)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(x_after, y_after, 0.5)
pyautogui.click(x_after,y_after)