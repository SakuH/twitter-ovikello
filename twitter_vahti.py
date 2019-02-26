#!/usr/bin/env python

from twython import Twython
import pygame.image
import pygame.camera
import time
import RPi.GPIO as GPIO 

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )


GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cam = None



while True:
    try:
        if cam == None:
            pygame.camera.init()
            cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(1280,720))
            time.sleep(10)
            cam.start()
            print("kamera initialized")
    

            
        
            
        if GPIO.input(18) == False:
            #cam.get_image() is used four times because of some buggy functionality of the pygame camera module
            img = cam.get_image()
            img = cam.get_image()
            img = cam.get_image()
            img = cam.get_image()
            
            

            pygame.image.save(img, "photo.jpg")
            time.sleep(1)
            #pygame.camera.quit()


            message = " "
            image = open('photo.jpg','rb')
            response = twitter.upload_media(media=image)
            media_id = [response['media_id']]

            twitter.update_status(status=message, media_ids=media_id)
            print("kuva otettu")
            time.sleep(3)
            print("camera off cooldown")
            
            
    except:
        if not(cam == None):
            #pygame.camera.quit()
            cam = None
            print("kamera ei toiminut")
            
