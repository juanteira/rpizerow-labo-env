from gpiozero import LED
from time import sleep

ledVERDE = LED(13)
ledROJO = LED(19)
ledAZUL = LED(26)

while True:
	sleep(0.25)
	ledVERDE.on()
# enciende el led verde por un cuarto de segundo 
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
# luego de medio segundo se apaga el led verde y se enciende el led azul
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.on()
# luego pasa un segundo y se apagan el azul y verde y se enciende el rojo
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
# se apagan todos los leds
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.off()
