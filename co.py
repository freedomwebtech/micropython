
##File name is change it's co.py not network.py####
import network
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print ("connecting to network")
        wlan.connect("valorant","freedomtech")
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())
      
do_connect()
 
