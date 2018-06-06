**Selenium Scripts To Post In Facebook, Twitter And Linkedin**

*A Selenium Script to post an image with text on the Facebook Groups you are member.
*A Selenium Script to post an image with text on twitter.
*A Selenium Script to post an image with text linkedin.

Facebook script
*Verify you have Python 3.6.x installed
*Install pip
https://bootstrap.pypa.io/get-pip.py
*Install python virtual environments 
$ pip install virtualenv
* Create your virtual environment
$ virtualenv venv
5.Activate your virtual environment
$ source venv/bin/activate
6.Install Python bindings for Selenium
$ (venv) pip install selenium
7.Clone this repo
git clone https://github.com/ColombiaPython/social-media-automation
8.Move to the social-media-automation
$ (venv) cd social-media-automation
9.Download geckodriver and . Configure the script and enjoy!
There is a main method in the script, you need to edit and provide your user and password, the path to the image and the link of facebook groups
10.Run the script
$ (venv) python fbposter.py
9.Download geckodriver and put in line 23 the path to this. Configure the script and enjoy!
There is a main method in the script, you need to edit and provide your user and password, the path to the image and the link of facebook groups

Linkedin script
1.the same above steps until step 8
9.Download geckodriver and put in line 23 the path to this. Configure the script and enjoy!
There is a main method in the script, you need to edit and provide your user and password, the path to the image
10.Run the script
$ (venv) python linkedinpost.py
NOTE: The script still does not work for load images in groups even if it works to publish in the home or in a group without image

Twitter script
1.the same above steps until step 8
9.Download geckodriver and put in line 22 the path to this. Configure the script and enjoy!
There is a main method in the script, you need to edit and provide your user and password, the path to the image
10.Run the script
$ (venv) python tweetpost.py
