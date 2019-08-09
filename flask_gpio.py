import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
   4 : {'name' : 'RPI PWR' , 'state' : GPIO.LOW},
   3 : {'name' : 'MB PWR'  , 'state' : GPIO.LOW},
   2 : {'name' : 'Door'    , 'state' : GPIO.LOW},
   27 : {'name' : 'UP'     , 'state' : GPIO.LOW},
   22 : {'name' : 'DOWN'   , 'state' : GPIO.LOW},
   17 : {'name' : 'STOP'   , 'state' : GPIO.LOW}
   }

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.HIGH)

@app.route("/")
def main():
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
      }
   return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
   changePin = int(changePin)
   deviceName = pins[changePin]['name']
   if action == "on":
      if deviceName == "Door":
         GPIO.output(changePin, GPIO.HIGH)
         message = "Turned " + deviceName + " on."
      else:
         pass
   if action == "off":
      if deviceName == "Door":
         GPIO.output(changePin, GPIO.LOW)
         message = "Turned " + deviceName + " off."
      else:
         GPIO.output(changePin, GPIO.LOW)
         time.sleep(0.5)
         GPIO.output(changePin, GPIO.HIGH)

   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)