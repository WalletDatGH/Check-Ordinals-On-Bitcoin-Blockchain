import urllib.request, json
import hashlib
import time


#You can change the 1 for the number of images to check on the blockchain
for x in range(1):
    print(x)
    varnum = str(x)
    filename = "images/" + varnum + ".png"
    with open(filename,"rb") as f:
        bytes = f.read() 
        readable_hash = hashlib.sha256(bytes).hexdigest();
        hash = readable_hash
 
    with urllib.request.urlopen("https://api2.ordinalsbot.com/search?hash=" + hash) as url:
        data = json.load(url)
    
    
        dato = data["count"]
        dato = int(dato)

    if(dato > 0):
        print("There are " + str(dato) + " on the blockchain")    
    else:
        print("Does not exist")

    time.sleep(1)
