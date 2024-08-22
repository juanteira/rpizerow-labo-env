from gpiozero import LED
from gpiozero import buzzer

buzzer = buzzer(15)
ledVerde = LED(13)
ledRojo = LED(19)
ledAzul = LED(26)

alfa = input()

while True:
	if 'buzz' in alfa:
		if 'on' in alfa:
			buzzer.on()
		elif 'off' in alfa:
			buzzer.off()
	elif 'RGB' in alfa:
		if 'azul' in alfa:
			ledAzul.on()
		elif 'rojo' in alfa:
			ledRojo.()
		elif 'verde' in accion:
			ledVerde.toggle()

