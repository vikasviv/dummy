# Import the httplib2 library and create a http object.
import httplib2
import threading
import multiprocessing
http = httplib2.Http()


# Imports some Python Date/Time functions
import time
import datetime

# Imports the PyOTA library
from iota import Iota
from iota import Address

# Define URL's used when sending http requests
url_on1 = 'http://192.168.0.9/gpio/1'
url_off1 = 'http://192.168.0.9/gpio/0'
url_on2 = 'http://192.168.0.9/gpio/2'
url_off2 = 'http://192.168.0.9/gpio/3'




class Balance:

    # Define some variables
    lightbalance = 0
    balcheckcount = 0
    lightstatus = False
    # URL to IOTA fullnode used when checking balance
    iotaNode = "https://field.carriota.com:443"
    # Create an IOTA object
    api = Iota(iotaNode, "")


    def __init__(self, address, iotabalance):
        self.address = address
        self.iotabalance = iotabalance
        

    def checkbalance(self):
        
        print("Checking balance")
        gb_result = api.get_balances(self.address)
        self.iotabalance = gb_result['balances']
        return (self.iotabalance[0])


        # Get current address balance at startup and use as baseline for measuring new funds being added.   
        currentbalance = self.checkbalance()
        lastbalance = self.currentbalance
        print(currentbalance)


    def switch(self):
        # Main loop that executes every 1 second
        while True:
            
            # Check for new funds and add to lightbalance when found.
            if balcheckcount == 10:
                currentbalance = checkbalance()
                if currentbalance > lastbalance:
                    lightbalance = lightbalance + (currentbalance - lastbalance)
                    lastbalance = currentbalance
                balcheckcount = 0
                print(currentbalance)

            # Manage light balance and light ON/OFF
            if lightbalance > 0:
                if lightstatus == False:
                    print("light ON")
                    response, content = http.request(url_on, 'GET')
                    lightstatus=True
                lightbalance = lightbalance -1       
            else:
                if lightstatus == True:
                    print("light OFF")
                    response, content = http.request(url_off, 'GET')
                    lightstatus=False
         
            # Print remaining light balance
            print(lightbalance)
            print(datetime.timedelta(seconds=self.lightbalance))

            # Increase balance check counter
            balcheckcount = balcheckcount +1

            # Pause for 1 sec.
            time.sleep(1)

# IOTA address to be checked for new light funds 
# IOTA addresses can be created using the IOTA Wallet
address1 = [Address(b'ZUBGJ9ZE9WKYTMNZPLUTOIVYQGVEGEJNLOU9ERSXFJIVEPVIYOAWFFNEGATOUTWNZPHVPMICJERCTNMT9SEPUMG9WD')]
address2 = [Address(b'EJVZLHIMMVMGLVGQICRBMP9OQTHDDBLFVMTHOBXWXJJTTNFCLZDFOJRXDRTW9SNR9RUNJEGSIWZJCE9PZLHYCDOMEY')]

# URL to IOTA fullnode used when checking balance
iotaNode = "https://field.carriota.com:443"
# Create an IOTA object
api = Iota(iotaNode, "")
print("Checking balance")
gb_result1 = api.get_balances(address1)
iotabalance1 = gb_result1['balances']

gb_result2 = api.get_balances(address2)
iotabalance2 = gb_result2['balances']

Balance1 = Balance(address1,iotabalance1)
Balance2 = Balance(address2,iotabalance2)

print(Balance1.address)
print(Balance2.iotabalance)
   
