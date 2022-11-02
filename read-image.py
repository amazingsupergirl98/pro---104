import cv2

#read image
img = cv2.imread("butterfly.jpeg")

#display colored image
cv2.imshow("Display Image",img)

#convert colored image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#display grayscale image
#cv2.imshow("Grayscale", gray_img)

#print(gray_img)

cv2.waitKey(0)