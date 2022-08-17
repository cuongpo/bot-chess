from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import pyautogui
import threading
from threading import Thread


def main(number_of_tab,link,max_time,position):

	# Open browser + change position
	driver = webdriver.Chrome(executable_path="./chromedriver")
	driver.set_window_position(position, position, windowHandle ='current')
	driver.get(link)
	

	# Click nut play
	while(True):
		try:
			time.sleep(1)
			play_button = driver.find_element(By.CSS_SELECTOR,'#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')
			print(play_button)
			play_button.click()
			break
		except:
			if (int(time.time() * 1000) - start_time > (30*1000)):
				break
			print("cho load trang")

	# Check thoi gian hien tai	
	start_time = int(time.time() * 1000)
	time.sleep(3)
	check = True
	while(True):
		print(int(time.time() * 1000) - start_time)
		# if (int(time.time() * 1000) - start_time <= (int(max_time)*1000+3000)):
		try:
			# Click quang cao
			time.sleep(3)
			x = driver.find_element(By.CLASS_NAME,'ytp-ad-button-text')
			print(x)
			x.click()
			
			# Check cookie
			print(driver.get_cookies())

			# Xoa cookie
			time.sleep(3)
			driver.delete_all_cookies()
			print('xoa cookie')

			# Tat tab 
			time.sleep(3)
			while (True):
				try:
					time.sleep(1)
					driver.close()
					driver.quit()
					time.sleep(1)
					break
				except:
					print('cho tat tab')

			# Mo tab moi
			time.sleep(3)
			driver = webdriver.Chrome(executable_path="./chromedriver")
			driver.set_window_position(position, position, windowHandle ='current')
			driver.get(link)
			start_time = int(time.time() * 1000)
			time.sleep(3)

		except:
			print('chua co quang cao')
			if (int(time.time() * 1000) - start_time > (int(max_time)*1000+3000)):
				print('qua time')
				# Xoa tab 
				while (True):
					try:
						time.sleep(1)
						driver.close()
						driver.quit()
						time.sleep(1)
						break;
					except:
						print('cho tat tab')

				# Mo tab moi
				time.sleep(3)
				driver = webdriver.Chrome(executable_path="./chromedriver")
				driver.set_window_position(position, position, windowHandle ='current')
				driver.get(link)
				start_time = int(time.time() * 1000)
				time.sleep(5)

				# Click nut play
				while(True):
					try:
						time.sleep(1)
						play_button = driver.find_element(By.CSS_SELECTOR,'#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')
						print(play_button)
						play_button.click()
						break
					except:
						if (int(time.time() * 1000) - start_time > (30*1000)):
							break
						print("cho load trang")

		time.sleep(5)


# Input
number_of_tab = input("so luong tab muon bat: ")
link = input("link youtube: ")
max_time = input("xem toi da bao nhieu giay: ")

# multi thread
thislist = ["1", "2", "3","4","5","6","7","8","9","10","1", "2", "3","4","5","6","7","8","9","10","1", "2", "3","4","5","6","7","8","9","10","1", "2", "3","4","5","6","7","8","9","10","1", "2", "3","4","5","6","7","8","9","10"]

for x in range(int(number_of_tab)):
	thislist[x] = threading.Thread(target=main, args=(number_of_tab,link,max_time,(x+1)*20))
	thislist[x].start()
	time.sleep(1)
time.sleep(3)
for x in range(int(number_of_tab)):
	thislist[x].join()
	time.sleep(1)
	




		