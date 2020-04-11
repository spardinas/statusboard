from gpiozero import StatusBoard, PingServer
from gpiozero.tools import negated, smoothed
from time import sleep
from signal import pause
import requests

#def website_up(url):
#    try:
#        r = requests.get(url)
#        return r.ok
#    except:
#        return False

sb = StatusBoard('DDNS', 'VPN', 'CAM', 'WEB', 'APAGADO')  # only using 4 strips

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)

statuses = {
    PingServer('10.0.10.253'): sb.CAM,PingServer('http://bocata.ddns.net/'): sb.DDNS,
}
#if website_up('http://bocata.ddns.net/'):
#            sb.DDNS.lights.green.on()
#            sb.DDNS.lights.red.off()
#       else:
#            sb.DDNS.lights.red.on()
#            sb.DDNS.lights.green.off()

for server, strip in statuses.items():
    strip.lights.green.source = smoothed(server.values, 2, any)  # allow 1 false negative out of 2
    strip.lights.green.source_delay = 60
    strip.lights.red.source = negated(strip.lights.green.values)
# for strip in sb:
    strip.lights.red.on()   # when the button is pressed, toggle the lights
    strip.button.when_pressed = strip.lights.toggle

#    strip.lights.green.source = strip.button.values
#    strip.lights.red.source = negated(strip.button.values)
#
# pause()
#
#
#
# sb.on()  # all leds on
# sleep(1)
# sb.off()  # all leds off
# sleep(1)
# sb.DDNS.on()  # both leds of first strip on
# sleep(1)
# sb.strip2.lights.green.on()  # green led of fourth strip on
# sleep(1)
#
#
# from gpiozero import StatusBoard, PingServer
# from gpiozero.tools import negated, smoothed
# from signal import pause
#
# sb = StatusBoard('mum', 'dad', 'alice')
#
# statuses = {
#     PingServer('192.168.1.5'): sb.mum,
#     PingServer('192.168.1.6'): sb.dad,
#     PingServer('192.168.1.7'): sb.alice,
# }
#
# for server, strip in statuses.items():
#     strip.lights.green.source = smoothed(server.values, 2, any)  # allow 1 false negative out of 2
#     strip.lights.green.source_delay = 60
#     strip.lights.red.source = negated(strip.lights.green.values)
#
# pause()
