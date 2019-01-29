import cv2
import glob
def resize(width,height):
    imagelist=glob.glob('*.jpg')

    for image in imagelist:
        img=cv2.imread(image,1)
        re=cv2.resize(img,(width,height))
        cv2.imshow('hey',re)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

        cv2.imwrite("resized_"+image,re)

print("enter the width")
width=int(input())
print("enter the height")
height=int(input())

resize(width,height)
