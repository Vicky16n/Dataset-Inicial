from  PIL  import Image
from rembg import remove
import glob
import cv2
import os 
cur_path = "./DataSetCompleto"
i=1
for file in glob.glob(cur_path + "/*"):
        
        print("Processing Image"+ str(i) )
        # read the images path
        image = cv2.imread(file)
        # denoising images
        dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
        b,g,r = cv2.split(dst)
        rgb_dst = cv2.merge([r,g,b])
        # save images
        save_path = './denoising/'
        cv2.imwrite(os.path.join(save_path ,  'ImagenSR_' + str(i) + '.jpg'),
                    cv2.cvtColor(rgb_dst,cv2.COLOR_RGB2BGR))
        i=i+1