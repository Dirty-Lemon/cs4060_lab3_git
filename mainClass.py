from detectorClass import *

class main():
    qr = Qr()
    
    # Task 1 - Read image
    qr.myImgRead('img/qrcode.png', 'QR Code')
    
    # Task 2 - Detect QR Code in image
    qr.qrCodeDetector('img/qrcode.png')
    

if __name__ == "__main__":
    main()