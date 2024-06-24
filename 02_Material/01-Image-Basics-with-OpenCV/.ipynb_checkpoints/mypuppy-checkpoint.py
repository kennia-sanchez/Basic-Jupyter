import cv2
img = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
while True:
    cv2.imshow('window_name',img)
    # If we have waited at least 1 ms and pressed the Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
