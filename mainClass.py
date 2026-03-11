from MyQRClass import *

class main():
    qr = MyQR()
    
    # Task 1 - Read image
    
    print("What qr code would you like to read?")
    imgToRead = input()
    qrImg = qr.myImgRead(imgToRead)
    
    # Task 2 - Detect QR Code in image
    opencvData, bbox, rectifiedImage = qr.myDetect(qrImg)
    if opencvData != None:
        print("QR Code Detected")
        qr.myShowImg(qrImg)
        
        # Task 3 - Draw bounding box
        imgWithBorder = qr.myBoundBox(bbox, rectifiedImage)
        print("Loading qr code...")
        qr.myShowImg(imgWithBorder)
        
        #Task 4 - Print decoded text
        qr.myDecode(opencvData)
        
        # Task 5  Save and display result
        # qr.myShowImg(rectifiedImage)
        
    else: print("QR Code Not Detected")


if __name__ == "__main__":
    main()