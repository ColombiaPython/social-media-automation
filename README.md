# **Selenium Scripts To Post In Facebook, Twitter And Linkedin** 

**A Selenium Script to post an image with text on the Facebook Groups you are member.**  
**A Selenium Script to post an image with text on twitter.**  
**A Selenium Script to post an image with text linkedin Groups you are member, companies you are admin or from your profile.**

### Facebook script
* Verify you have Python 3.6.x installed
* Install [pip](https://bootstrap.pypa.io/get-pip.py)
* Install python virtual environments   
```
$ pip install virtualenv
```
* Create your virtual environment  
```
$ virtualenv venv
```
* Activate your virtual environment  
```
$ source venv/bin/activate
```
* Install Python bindings for Selenium  
```
$ (venv) pip install selenium
```
* Clone this repo  
git clone https://github.com/ColombiaPython/social-media-automation
* Move to the social-media-automation  
```
$ (venv) cd social-media-automation
```
* Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put in line 23 the path to this. Configure the script and enjoy!  
There is a main method in the script, you need to edit and provide your user and password, the path to the image and the link of facebook groups
* Run the script  
```
$ (venv) python fbposter.py
```
### Linkedin script
* the same above steps until step 8
* Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put in line 23 the path to this. Configure the script and enjoy!  
There is a main method in the script, you need to edit and provide your user and password, the path to the image or the link of the companie. If you want to publish from your profile do not put data of company or groups
* Run the script  
```
$ (venv) python linkedinpost.py  
```

### Twitter script
* the same above steps until step 8
* Download put in line 23 the path to this and put in line 22 the path to this. Configure the script and enjoy!  
There is a main method in the script, you need to edit and provide your user and password, the path to the image
* Run the script  
```
$ (venv) python tweetpost.py
```
