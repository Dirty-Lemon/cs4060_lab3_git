import cv2
import matplotlib
import matplotlib.pyplot as plt

class MyQR():
    def __init__(self):
        print("QR Code Detector")
        
    # Read and display image
    def myImgRead(self, imgName):
        matplotlib.rcParams['figure.figsize'] = (8.0, 8.0)
        imgPath = 'img/' + imgName
        
        print("Reading " + imgName + "...")
        return cv2.imread(imgPath)
        
        # cv2.imwrite(imgPath, cv2_qr)
        # plt.imshow(cv2_qr); plt.title(pltTitle)
        # plt.show()
    
    # Detects a QR code
    def myDetect(self, qrImg):
        # Detect QR code in image
        # Output stored in (this order):
        #     opencvData, bbox, rectifiedImage
        qrDetector = cv2.QRCodeDetector()
        
        print("Detecting QR Code...")
        qrDataArray = qrDetector.detectAndDecode(qrImg)
        return qrDataArray
    
    def myBoundBox(self, bbox):
        n = len(bbox)
        