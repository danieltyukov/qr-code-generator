import qrcode
import image

qr = qrcode.QRCode(
    version=15, 
    box_size=10, 
    border=5
)

data = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed"

