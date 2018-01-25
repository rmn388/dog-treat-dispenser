# dog-treat-dispenser

All of the code and CAD models to make the Dog Treat Dispenser that is featured in the Feb/March 2018 Issue of Make Magazine.

Video of the device in action: https://www.youtube.com/watch?v=wkbKYwNOw7A

Blog post with a high level overview of the project: http://richnelson.me/side-project/2015/12/25/treat-dispenser.html


##### Setup Table of Contencts
- [1. Getting Started](#gettingstarted)
- [2. Raspberry Pi Setup](#raspberrypi)  

<a name="gettingstarted"/>


## 1. Getting Started

This detailed tutorial section is a work in progress.

This tutorial will not cover:
- Fabrication of the parts
- Basic setup of the Raspberry Pi
- Setup of Arduino IDE
- Port forwarding for your specific router

But may provide links to external resources, as there is great documentation for these tasks.

This tutorial will cover:
- Setting up the server on the Raspberry Pi
- Configuring your Twilio phone number
- Wiring up the components
- Assembly of the device

If there are any issues, please report them in the bug tracker for this repository.

<a name="raspberrypi"/>


## 2. Raspberry Pi Setup
IMPORTANT: Make sure the power supply you use for four Raspberry Pi has a high enough current rating.  2.5A is recommended, but I find 2A+ to keep things working smoothly.  A Raspberry Pi that is not getting enough current can act unpredictably when processes ramp up and the current draw increases,  I learned this the hard way trying to debug an issue for a week that was caused by an inadequate power supply and I've talked to many people with similar experiences.

### Downloading the Repository and setting up the virtual environment
Log onto your Raspberry Pi with Raspbian installed.  _(A Raspberry Pi 3 Model B with Raspbian stretch in my case)_.  You can plug directly into the Pi with an HDMI screen, mouse, and keyboard.  Or if the Pi is already on your network you can connect via SSH or VNC,  I'll be using VNC for this tutorial.

![Raspberry Pi open terminal](https://imgur.com/Pca8yHA.jpg)


Make sure you are connected to the internet through your home network.

Create a local copy of this repository.

Terminal Input:
```bash
git clone https://github.com/rmn388/dog-treat-dispenser
```
Expected Output:
```bash
Cloning into 'dog-treat-dispenser'...
remote: Counting objects: 66, done.
remote: Total 66 (delta 0), reused 0 (delta 0), pack-reused 66
Unpacking objects: 100% (66/66), done.
```

cd into the new directory

Terminal Input:
```bash
cd dog-treat-dispenser
```
Current Location _(to left of cursor)_:
```bash
~/dog-treat-dispenser $
```

You can use ls to list the files in the directory

Input:
```bash
ls
```

Expected Output:
```bash
app.py  arduino  bin  cad  README.md  requirements.txt
```

We're going to install virtualenv so that we can create a virtual environment to manage the packages and versions for the project. This step is technically not necessary, but may help to avoid headaches later with dependency issues, and it is good practice so that the libraries don't interfere with other projects.

Input:
```bash
python3 -m pip install --user virtualenv
```

Expected Output:
```bash
Collecting virtualenv
  Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
    100% |████████████████████████████████| 1.8MB 64kB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-15.1.0
```

Making sure you are still in the project directory create a virtual environment

Input:
```bash
python3 -m virtualenv env
```

Expected Output:
```bash
Using base prefix '/usr'
New python executable in /home/pi/dog-treat-dispenser/env/bin/python3
Also creating executable in /home/pi/dog-treat-dispenser/env/bin/python
Installing setuptools, pip, wheel...done.
```

You should also see a new folder in your project directory called env

Lastly to activate our virtual environment:
```bash
source env/bin/activate
```

Now your in the terminal your username/current directory should be prefaced with (env):
```bash
(env) pi@raspberrypi:~/dog-treat-dispenser $
```

Whenever we run the project we'll need to be in this environment, to deactivate the environment simply type: deactivate

### Setting up the Dependencies and Config

To install the python dependencies enter:
```bash
pip install -r requirements.txt
```
The installation should finish with the following message:
```bash
Successfully installed Flask-0.12.1 Jinja2-2.10 MarkupSafe-1.0 PyJWT-1.5.3 RPi.GPIO-0.6.3 Werkzeug-0.14.1 certifi-2018.1.18 chardet-3.0.4 click-6.7 dropbox-6.8.0 idna-2.6 itsdangerous-0.24 picamera-1.13 pysocks-1.6.8 pytz-2017.3 requests-2.18.4 six-1.11.0 twilio-6.8.3 typing-3.6.4 urllib3-1.22
```

 Next we need to create a configuration file which will contain all of the settings for your project.

 Create a file called config.py in the root directory of your project,  this can be done with the terminal text editor of choice, or with a gui by navigating to the project folder and creating the file.

 config.py
 ```python
 #config

#Private API credentials
dropbox_access_token = "################################################################" #Your Dropbox Access Token
dropbox_folder = "dog_photos" #Dropbox folder where you want to save th photos, you must create this folder in your Dropbox
twilio_phone_number = "+###########" #Your unique Twilio phone number
twilio_account_sid = "#################################" #Your Twilio Account SID
twilio_auth_token  = "################################" #Your Twilio Auth Token

#Default settings
port = 2244
img_width = 3280
img_height = 2464
alert_GPIO_pin = 17
treat_GPIO_pin = 18
alert_reps = 3
num_treats = 1
```

We will fill in those API credentials soon, but with that file made we're ready to run the flask server as the first test!

In the terminal enter:
```bash
python app.py
```
Expected Output:
```bash
* Running on http://0.0.0.0:2244/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 782-553-230
```

This means the server is running!  The first output line "Running on ..." Shows the URL of the server on the local machine.  So you can open up a browser window on the pi and type it in, you should see this.

![Flask server test](https://imgur.com/4E2npO5.jpg)

You can also visit the server from any computer that is on the same network, but you will need to use the Pi's local network IP address instead of 0.0.0.0.  To find the Pi's IP address type __ifconfig__ in the terminal, it is the "inet" address for me in the wlan section since I'm on wifi.  It usually starts with 192.168.  So you can substitute that for the "0.0.0.0" to test the server from any computer on your network.

When you visit the URL the terminal window that is running the server should show a log like this:
```bash
127.0.0.1 - - [25/Jan/2018 05:15:47] "GET / HTTP/1.1" 200 -
```

To shutdown the server press Ctrl-C



Note: This detailed setup tutorial is a work in progress next sections will be setting up the camera and API credentials.
---
