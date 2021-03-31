import qrcode #QRCode

print("QR-Code-Generator")
print("\n")

#ask Filename
file_name = inputt("Filename (myQR-Code):  ")

#fileextension .png/jpg.
file_ext = ".png"

#ask message:
msg = input("Message:   ")

#qr code generator
def make_qr(filename, msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()


make_qr(file_name + file_ext, msg)









