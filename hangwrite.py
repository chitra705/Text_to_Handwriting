import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hi...",save_to="write.png")

img=cv2.imread("write.png")
cv2.imshow("txt to handwrite",img)
cv2.waitKey(0)
cv2.destroyAllWindows()