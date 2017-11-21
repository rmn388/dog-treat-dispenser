# dog-treat-dispenser

This repository contains all of the code and CAD models for the Dog Treat Dispenser project.

Video of the device in action: https://www.youtube.com/watch?v=wkbKYwNOw7A

Blog post about the project: http://richnelson.me/side-project/2015/12/25/treat-dispenser.html

## Some Configuration Required

The configuration file is not included in this repository,  to set up your project **create a file called config.py in the root directory** and paste in the following, filling in your API credentials and other settings:
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
