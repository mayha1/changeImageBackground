import cv2
import numpy as np

UPPERGREEN = np.array([70, 255,255])
LOWERGREEN = np.array([40, 40,40])

def changeBackgroundImage(inputImageFileName, newBackgroundFileName):
    # read input
    inputImage = cv2.imread(inputImageFileName)
    image = inputImage.copy()
    newBackground = cv2.imread(newBackgroundFileName)
    
    # resize background
    (height, width, depth) = image.shape 
    newBackground = cv2.resize(newBackground, (width, height))

    # convert to hsv
    imageHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(imageHSV, LOWERGREEN, UPPERGREEN)
    image[mask == 255] = newBackground[mask == 255]

    # show and save
    beforeAndAfterImage = np.hstack((inputImage, image))
    cv2.imshow('before and after', beforeAndAfterImage)
    cv2.imwrite('result.jpg', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

changeBackgroundImage("inputImage.jpg", "background.jpg")
