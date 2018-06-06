from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def main():
	#your account user and password, path to image and message
	usr = ""
	pwd = ""
	message = ""
	image_path = ""

	#delete cache
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	# Path to geckodriver executable
	driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver')
	driver.implicitly_wait(15)

	# Login to twitter
	driver.get("https://twitter.com")
	sleep(3)
	elem = driver.find_element_by_name("session[username_or_email]")
	elem.send_keys(usr)
	elem = driver.find_element_by_name("session[password]")
	elem.send_keys(pwd)
	c = driver.find_element_by_class_name("EdgeButton")
	c.click()
	sleep(3)
	# Enter the text we want to post to twitter and the image 
	mess = driver.find_element_by_id("tweet-box-home-timeline")
	mess.send_keys(message)
	sleep(5)
	ima = driver.find_element_by_name("media_empty")
	sleep(3)
	ima.send_keys(image_path)
	# Get the 'Post' button and click on it
	Post_button = driver.find_element_by_class_name("tweet-action")
	sleep(3)
	Post_button.click()
	sleep(3)
	driver.close()

if __name__ == '__main__':
  main()