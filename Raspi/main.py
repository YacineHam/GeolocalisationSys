#!/usr/bin/python3
import requests

import serial
import time
import pynmea2

import asyncio
import json
import websockets


from AESCipher import AESCipher
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64decode,b64encode
import random

import rsa

from string import printable
import os

username = os.environ['CAR_NAME']
passwd = os.environ['CAR_PASSWD']
host = '10.42.0.1:8000'
host = os.environ['GPS_HOST']
#host = 'localhost:8000'
http_host = 'http://' + host
ws_host = 'ws://' + host
ws_url = ws_host + '/ws/location/'
auth_url = http_host + '/api/token/'
refresh_url = auth_url + '/refresh/'
rsa_url = http_host + '/rsakey/'
aes_url = http_host + '/aeskey/'

class Car:

    username = ''
    passwd = ''
    access_token = ''
    refresh_token = ''
    aes_key= Random.new().read(AES.block_size)


    def __init__(self,name,passwd):
        self.username = name
        self.passwd = passwd
        self.aes_key = ''.join(random.choices(printable,k=32)).encode() #Random.new().read(AES.block_size)
        self.aes_cipher = AESCipher(self.aes_key)
        print('aes key',self.aes_key)
        

    def authen(self,url):
        data = json.dumps({'username':self.username, 'password':self.passwd})
        headers = {
            "Content-type": "application/json",
        }
        res = json.loads(requests.post(url,data,headers=headers).text)

        self.access_token = res['access']
        self.refresh_token = res['refresh']

    def refresh(self, url):
        data = json.dumps({'refresh':self.refresh_token})
        headers = {
            "Content-type": "application/json",
        }
        res = json.loads(requests.post(url,data,headers=headers).text)
        self.access_token = res['access']


    def rsa_enc_aes(self, url): #/rsakey
        data = json.dumps({'access':self.access_token,})
        headers = {
            "Content-type": "application/json",
        }
        res = requests.post(url, data, headers=headers).text
        print(res)
        res = json.loads(res)
        rsa_pubkey = rsa.PublicKey(int(res['pubkey']['n']),int(res['pubkey']['e']))

        enc_aes_key = rsa.encrypt(self.aes_key, rsa_pubkey)
        self.send_aes_key(enc_aes_key, aes_url)


    def send_aes_key(self, enc_aes_key, url): #/aeskey

        data = json.dumps({'access':self.access_token, 'aes_key':b64encode(enc_aes_key).decode(),})
        headers = {
            "Content-type": "application/json",
        }
        requests.post(url,data,headers=headers)


    async def get_send_location(self,url) :
        async with websockets.connect(url) as websocket:
            
            while True :

                port = "/dev/ttyUSB0"
                ser = serial.Serial(port,baudrate=9600,timeout=0.5)
                dataout = pynmea2.NMEAStreamReader()
                newdata = ser.readline().decode()
                #print(newdata[0:6])
                
                if newdata[0:6] in ["$GPRMC", "$GPGGA", "$GPGLL"] :
                #if True :
                
                    newmsg = pynmea2.parse(newdata)
                    if not(newmsg.is_valid) :
                        print("Invalid GPS data")
                        continue 
                    #lat = 20 
                    lat = newmsg.latitude
                    #lng = 30 
                    lng = newmsg.longitude
                    
                    lat = self.aes_cipher.encrypt(str(lat)).decode()
                    lng = self.aes_cipher.encrypt(str(lng)).decode()
                    data = json.dumps({'latitude':lat, 'longitude':lng})
                    print('Sending Location')
                    await websocket.send(data)


if __name__=='__main__' :
    while True :
        try :
            mycar = Car(username,passwd)
            mycar.authen( auth_url )
            mycar.rsa_enc_aes(rsa_url)
        
            asyncio.get_event_loop().run_until_complete(mycar.get_send_location( ws_url + '?token=' + mycar.access_token))
        except Exception as e :
            print(e)
