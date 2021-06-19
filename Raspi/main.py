#!/usr/bin/python3
import requests

import serial
import time
import string 
import pynmea2

import asyncio
import json
import websockets


class Car:

    name = ''
    passwd = ''
    access_token = ''
    refresh_token = ''

    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def authen(self,url):
        data = json.dumps({'email':self.name, 'password':self.passwd})
        headers = {
            "Content-type": "application/json",
        }
        res = json.loads(requests.post(url,data,headers=headers).text)

        self.access_token = res['access']
        self.refresh_token = res['refresh']

    def refresh(self,url):
        data = json.dumps({'refresh':self.refresh_token})
        headers = {
            "Content-type": "application/json",
        }
        res = json.loads(requests.post(url,data,headers=headers).text)
        self.access_token = res['access']


    async def get_send_location(self,url) :
        async with websockets.connect(url) as websocket:
            
            while True :
                
                port = "/dev/ttyUSB0"
                ser = serial.Serial(port,baudrate=9600,timeout=0.5)
                dataout = pynmea2.NMEAStreamReader()
                newdata = ser.readline().decode()
                #print(newdata[0:6])

                if newdata[0:6]=="$GPRMC":
                
                    newmsg = pynmea2.parse(newdata)
                    lat = newmsg.latitude
                    lng = newmsg.longitude

                    data = json.dumps({'latitude':lat, 'longitude':lng})
                    await websocket.send(data)

                #gps="Latitude=" +str(lat) + " and Longitude=" +str(lng)
                #print(gps)


if __name__=='__main__' :
    host = '10.42.0.1:8000'
    name = 'test@test.test'
    passwd = 'test'
    mycar = Car(name,passwd)
    mycar.authen('http://' + host + '/api/token/')
    asyncio.get_event_loop().run_until_complete(mycar.get_send_location('ws://' + host + '/ws/test/?token=' + mycar.access_token))
