import os
import glob 
import cv2

# dir  = os.getcwd()
# res = os.path.join(dir , 'photos' , '122')
# os.mkdir(res)
# print(res)

# id : str = input("enter your roll ")
# # dir = os.getcwd()
# # res = os.path.join( dir , 'photos ' , id )
# # os.mkdir('photos/' + id)
# print(f'hello/{id}')
main = os.getcwd()
res = glob.glob(main + '/output/*.jpg')
image=cv2.imread(res[0])
print(image.shape)

# image_resized= cv2.resize(image, (224,224))
# cv2.imshow('window' , image_resized)

 
 
# C:\Users\hp\Desktop\face_recognition

# folder =  os.walk('photos')
# for root , dir , file in folder:
#    sub =  [s for s in  dir]
#    sub.sort()
   
#    for f in sub:
#        if f == '10':
#                  folder_path =  os.path.join(main , 'photos' , f)
#                  file_path = os.path.join(folder_path , '.png')
       
#                  with open(file_path, 'w') as file:
#                       file.write("hello")

     
   
    
print(os.listdir('photos'))
os.makedirs('test')
cnt = 0
for dir in os.listdir('photos'):
    if cnt <21:
      folder_path= os.path.join(main , 'test')
      file_name = dir + str(cnt) + '.jpg' 
      file_path = os.path.join(folder_path , file_name)
      img =  cv2.imread(file_path)
      cv2.imwrite(file_name , img )
      cnt = cnt+1