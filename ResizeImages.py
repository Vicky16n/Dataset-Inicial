import cv2
import os


path= r'C:\Users\monca\Desktop\WebScraping\DataSetCompleto'


for i in os.listdir(path):
    #read the image
    img = cv2.imread(path+"\\"+i)
    #Current image message
    print(path+"\\"+i)
    #Image filter 
    if img.shape[1]<300:
        print(i)
        #Delet Image
        os.remove(path+"\\"+i)
    else:
        #Resize Image
        width= int(300)
        height = int(350)
        dim=(width,height)
        resize= cv2.resize(img,dim)
        cv2.imwrite(path+"\\"+i,resize)
    
