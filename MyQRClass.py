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
    
    # Detects a QR code in an image
    def myDetect(self, qrImg):
        qrDetector = cv2.QRCodeDetector()
        print("Detecting QR Code...")
        
        # Output stored in (this order):
        #     opencvData, bbox, rectifiedImage
        qrDataArray = qrDetector.detectAndDecode(qrImg)
        return qrDataArray
    
    # Puts a bounding box around a given QR code
    def myBoundBox(self, bbox, rectifiedImage):
        n = len(bbox[0])
        print("Border length:", n)
        
        bbox_int = bbox.astype(int)
        
        print("Drawing border...")
        # Parameters: (image, top-left, bottom-right, color (BGR), border-thickness)
        return cv2.rectangle(rectifiedImage, bbox_int[0][0], bbox_int[0][2], (0, 0, 0), 10)
    
    def myDecode(self, opencvData):
        print(opencvData)
        
    # Display an image
    def myShowImg(self, img):
        plt.imshow(img); plt.title("Image")
        plt.show()
        