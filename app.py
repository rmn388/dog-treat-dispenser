from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from bin.dispenser import Dispenser
from bin.photo import Photo
import config as c

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Treat Server is live!</h1>'

@app.route("/receive_message", methods=['GET', 'POST'])
def receive_message():
    message = request.values
    sms_sender_number = message.get('From')
    sms_body = message.get('Body')
    print(("{}: {}").format(sms_sender_number, sms_body))
    
    dispenser = Dispenser(c.alert_GPIO_pin, c.treat_GPIO_pin,)
    dispenser.alert_pet(c.alert_reps)
    print("Pet alerted")
    
    photo = Photo()
    img_filename = photo.take_picture(c.img_width, c.img_height)
    print("Photo filename:", img_filename)
    
    dispenser.give_treat(c.num_treats)
    print("Treat given")
    
    img_url = photo.upload_to_dropbox(c.dropbox_access_token,
                                      c.dropbox_folder)
    print("Image url:", img_url)
    
    twilio_client = Client(c.twilio_account_sid, c.twilio_auth_token)
    response = twilio_client.messages.create(to= sms_sender_number,
                                             from_= c.twilio_phone_number,
                                             body= "",
                                             media_url= img_url)
    print("Message sent")
    
    #photo.delete_photo()

    resp = MessagingResponse()

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=c.port, debug=True)
