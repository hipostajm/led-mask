# Led mask
Led mask for cosplaying perpuse. 

This repo contains:
- http server for micro controller 
- http server for some more powerfull hardware to rescale images

## Info

If you would like to make this work on other micro controllers (mine will only work on raspberry) you will need to change controller/matrix.py.

**This code does not come with any warrenty and you run it on your own risk.**

## How to addapt to your needs

### Micro controller:
1. If you want to change pinout layout you will need to change it in controller/app.py 
2. If you want to chnage the size of matrix you will need to change it in controller/app.py

### Server:
1. If you want to change IP you will need to change it in server/app.py

## How does it work

To show how it works I will use this cute connection

**your phone/pc -> server <-> micro controller -> led matrix**

I use for it HUB75 interface which has some problems with it becouse its not welly documented. Here is the best info I found [is this](https://learn.lushaylabs.com/led-panel-hub75/). I use GPIO which is not the best option but its the only one that I could use

Micro controller runs a flask http server which functions as a api for display and its able to display static and animated images.

Server also runs a http flask server which functions as a backend and frontend for display.

## How to send static and animated images to api

- For static images you need to send a http post request on /set-all/ endpoint with request containg key pixels with value as matrix of tupple of 3 ints (from 0 to 7) (list[list[tupple[int, int, int]]])

- For animated images you need to send a http post request on /animate/ with keys delay with value of number. The delay will be a time between the frames are presented. The secound key will be frames contaning a list of matrix'es the same as for static images