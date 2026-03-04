import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt

class Qr():
    def __init__(self):
        print("QR Code Detector")
    
    def hello(self):
        print("Hello Detector")
        
    # Read and display image
    def myImgRead(self, imgPath, pltTitle = 'Image')-> None:
        mpl.rcParams['figure.figsize'] = (8.0, 8.0)
        cv2_qr = cv2.imread(imgPath)
        plt.imshow(cv2_qr); plt.title(pltTitle)
        plt.show()
        
    def qrCodeDetector(self, imgPath):
        qrDetector = cv2.QRCodeDetector()
        
        # Detect QR code in image
        # Output stored in (this order):
        #     opencvData, bbox, rectifiedImage
        opencvData = 0
        bbox = 0
        rectifiedImage = 0
        
        if opencvData != None:
            print("QR Code Detected")
        else: print("QR Code Not Detected")