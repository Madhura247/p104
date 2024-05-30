import cv2
img = cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.putText(img, 
            "Sun", 
            (90, 80), 
            fontScale=2,
            fontFace=cv2.FONT_HERSHEY_COMPLEX, 
            color=(0, 0, 255))
cv2.putText(img, 
            "Mercury", 
            (110, 180), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Venus", 
            (190, 260), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Earth", 
            (290, 270), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Mars", 
            (380, 250), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Jupiter", 
            (550, 370), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Saturn", 
            (700, 120), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Uranus", 
            (960, 140), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.putText(img, 
            "Neptue", 
            (1110, 150), 
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5, 
            color=(255, 255, 255))
cv2.imwrite("Solar_systemwithname.jpg",img)