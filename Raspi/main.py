#!/usr/bin/python3
import requests

import serial
import time
import string 
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

host = '10.42.0.1:8000'
host = 'localhost:8000'
http_host = 'http://' + host
ws_host = 'ws://' + host
ws_url = ws_host + '/ws/test/'
auth_url = http_host + '/api/token/'
refresh_url = auth_url + '/refresh/'
rsa_url = http_host + '/rsakey/'
aes_url = http_host + '/aeskey/'
name = 'test'
passwd = 'test'
class Car:

    name = ''
    passwd = ''
    access_token = ''
    refresh_token = ''
    aes_key= Random.new().read(AES.block_size)


    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        self.aes_key = ''.join(random.choices(printable,k=32)).encode() #Random.new().read(AES.block_size)
        self.aes_cipher = AESCipher(self.aes_key)
        print('aes key',self.aes_key)
        

    def authen(self,url):
        data = json.dumps({'username':self.name, 'password':self.passwd})
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
                
                if newdata[0:6]=="$GPRMC" or True:
                
                    newmsg = pynmea2.parse(newdata)
                    #lat = 20 
                    newmsg.latitude
                    #lng = 30 
                    newmsg.longitude
                    
                    lat = b64encode(self.aes_cipher.encrypt(lat)).decode()
                    lng = b64decode(self.aes_cipher.encrypt(lng)).decode()
                    data = json.dumps({'latitude':lat, 'longitude':lng})
                    await websocket.send(data)

                #gps="Latitude=" +str(lat) + " and Longitude=" +str(lng)
                #print(gps)


if __name__=='__main__' :

    mycar = Car(name,passwd)
    mycar.authen( auth_url )
    mycar.rsa_enc_aes(rsa_url)
    asyncio.get_event_loop().run_until_complete(mycar.get_send_location( ws_url + '?token=' + mycar.access_token))
