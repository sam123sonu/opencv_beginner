import cv2
img=cv2.imread("lena.jpg",-1)
print(img)

cv2.imshow('sam',img)
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s') or ord('S'):
    cv2.imwrite('sam_copy.jpg',img)
    cv2.destroyAllWindows()
