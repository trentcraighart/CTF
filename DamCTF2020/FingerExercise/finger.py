import requests

url = "https://finger-warmup.chals.damctf.xyz/"
extension = ["", "4r1u8egwom4z0mmb88r9s", ""]

#I ran this for 500 loops and got the above starter

for x in range (0,1000):
    response = requests.get(
            (str(url) + str(extension[1]))
    	    )
    extension = str(response.text).split('"')
    print(response.content)
    
    

#b'<a href="un5vmavt8u5t5op1u94h">click here, if you are patient enough I will give you the flag</a>'
