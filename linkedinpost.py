from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def main():
	# Your account user and password, path to image, links to groups and message
	usr = ""
	pwd = ""
	title = ""
	message = ""
	image = ""
	group_links = [ #"https://www.linkedin.com/groups/group_id"]
	empresa_links = [ #"https://www.linkedin.com/company/company_id/admin/updates/"]
	
	# Delete cache
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	# Path to geckodriver executable
	driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver')
	driver.implicitly_wait(15)

	# Login to linkedin
	driver.get("http://www.linkedin.com")
	elem = driver.find_element_by_name("session_key")
	elem.send_keys(usr)
	elem = driver.find_element_by_name("session_password")
	elem.send_keys(pwd)
	c = driver.find_element_by_id("login-submit")
	c.click()

	# Check if there are groups of otherwise publishes from the profile that I sign
	if len(group_links) >= 1:
		for group in group_links:
			driver.get(group)
			post_box = driver.find_element_by_xpath("//*[@name='title']")
			post_box.send_keys(title)
			sleep(3)
			body_message = driver.find_element_by_xpath("//*[@name='body']")
			body_message.send_keys(message)
			if image != "":
				ima = driver.find_elements_by_class_name("js-input-upload")
				sleep(3)
				ima[0].send_keys(image)
			sleep(3)	
			post_box = driver.find_element_by_class_name("action-submit")
			sleep(3)
			post_box.click()
	elif len(empresa_links) >= 1:
		for empresa in empresa_links:
			driver.get(empresa)
			post_box = driver.find_element_by_class_name("sharing-create-share-view__create-content")
			post_box.click()
			sleep(3)
			mes = driver.find_element_by_class_name("mentions-texteditor__contenteditable")
			mes.send_keys(message)
			sleep(3)
			if image != "":
				ima = driver.find_elements_by_name("file")
				ima[0].send_keys(image)
				sleep(3)
			post_box = driver.find_element_by_xpath("//*[@data-control-name='share.post']")
			sleep(3)
			post_box.click()
	else:
		post_box=driver.find_element_by_class_name("sharing-create-share-view__create-content")
		post_box.click()
		sleep(3)
		mes = driver.find_element_by_class_name("mentions-texteditor__contenteditable")
		mes.send_keys(message)
		sleep(3)
		if image != "":
			ima = driver.find_elements_by_name("file")
			ima[0].send_keys(image)
			sleep(3)
		post_box = driver.find_element_by_xpath("//*[@data-control-name='share.post']")
		sleep(3)
		post_box.click()
	sleep(5)
	driver.close()

if __name__ == '__main__':
  main()