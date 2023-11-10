from mtcnn import MTCNN
import cv2 
import os


detector = MTCNN()
cnt = -1
#  read the image
main = os.getcwd()
path = os.path.join( main , 'output' , 'test_pho1.jpg')

img = cv2.imread('test_pho1.jpg') # file path 

valid_img = []
main = os.getcwd()
folder_name = os.path.join( main , 'output')


faces = detector.detect_faces(img)
for face in  faces:
    x,y ,w ,h = face['box']
    if face['confidence'] >= 0.9:
        cnt = cnt+1
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (255,0, 0), 3)
        cropped_img = img[y:y+h  , x:x+w]
        
        # file_name = str(cnt)+'.'+'jpg'  # file name of each photos
        # file_path = os.path.join(folder_name , file_name) # file path of each photos
        
        valid_img.append(cropped_img) 
        # cv2.imwrite(file_path , vaild_img[cnt]) # to save the photos at the output folder
 
print('no of faces are --->' , cnt )
print(len(valid_img))

# cv2.imshow('window' , vaild_img[1])   
# cv2.waitKey(0)
  
#   box = x, y  ,w , h 
# print(vaild_img[0].shape)
# image_resized= cv2.resize(vaild_img[0], (224,224))
# print(image_resized.shape)
    