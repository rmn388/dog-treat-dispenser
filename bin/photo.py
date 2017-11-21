import datetime
import os
import dropbox
import picamera

class Photo(object):
    
    def __init__(self):
        date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H;%M;%S")
        filename = ("photos/Pic-{}.jpg").format(date_time)
        self.filename = filename
        
    def take_picture(self, width = 3280, height = 2464):
        """Take picture with Raspberry Pi Cam and return the filename"""
        with picamera.PiCamera() as camera:
            camera.resolution = (width, height)
            camera.capture(self.filename)
        return self.filename

    def upload_to_dropbox(self, dropbox_access_token, dropbox_folder):
        """Upload picture to Dropbox Return Sharable URL"""
        dbx = dropbox.Dropbox(dropbox_access_token)
        self.dbx_filename = ("/{}/{}").format(dropbox_folder, self.filename)
        f = open(self.filename, 'rb')
        dbx.files_upload(f.read(), self.dbx_filename)
        self.img_url = dbx.sharing_create_shared_link(self.dbx_filename).url
        self.img_url = str.replace(self.img_url, "dl=0", "raw=1")
        return self.img_url 
    
    def delete_photo(self):
        """ Deletes the photo jpg on the Raspberry Pi filesystem"""
        os.remove(self.filename)
