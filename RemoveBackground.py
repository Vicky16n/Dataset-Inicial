from  PIL  import Image
from rembg import remove
import glob
import cv2
import os 
cur_path = "./DataSetCompleto/"


i=1
for file in glob.glob(cur_path + "/*"):  
        print("Processing Image"+ str(i) )
        # read the images path
        image = cv2.imread(file)
        # remove bg 
        output = remove(image)
        # save images
        save_path = './BGRemove/'
        cv2.imwrite(os.path.join(save_path , 'Imagen_' + str(i) + '.png'), output)
        i=i+1