import cv2
import os
data =()
datapath = "C:\\Users\\hicha\\Desktop\\moteur_de_recherche\\dataset"
for photo in os.listdir(datapath):
    temp = photo.rfind('/')
    tag = int(photo[photo[:temp].rfind('/')+1:temp].split('.')[0])
    img=cv2.imread(photo)
    try:
        img=cv2.resize(img,(32,32))
    except:
        break
    img=img.astype('float32')
    data.append([img,tag])
print(data)



