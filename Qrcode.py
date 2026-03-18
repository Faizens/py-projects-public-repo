#Creating qrcode using python 

import qrcode          #pip install qrcode[pil]

url = input("Enter the URL: ").strip()
file_path = "qrcode.png"       #file save location 

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()          #this will generate the actual qrcode image 
img.save(file_path)            #to save it 

print("qrcode generated")