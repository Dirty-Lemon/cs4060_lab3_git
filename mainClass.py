from MyQRClass import *

class main():
    qr = MyQR()
    
    # Task 1 - Read image
    qrImg = qr.myImgRead('qrcode.png')
    
    # Task 2 - Detect QR Code in image
    opencvData, bbox, rectifiedImage = qr.myDetect(qrImg)
    if opencvData != None:
        print("QR Code Detected")
        
        # Task 3 - Draw bounding box
        qr.myBoundBox(bbox)
    else: print("QR Code Not Detected")


if __name__ == "__main__":
    main()