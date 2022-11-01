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



def main(number_of_tab,link,max_time):

	# Open browser + change position
	profile_path = r'./chromedriver'


	driver = webdriver.Chrome(executable_path="./chromedriver.exe")
	# driver.set_window_position(position, position, windowHandle ='current')
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
			profile_path = r'./chromedriver'
			options=Options()
			driver = Chrome(options=options)
			driver = Chrome(service=service, options=options)
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
				profile_path = r'./chromedriver'
				options=Options()
				driver = Chrome(options=options)
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

main(number_of_tab,link,max_time);
	




		