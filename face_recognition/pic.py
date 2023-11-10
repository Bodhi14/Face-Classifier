import cv2
import os
detector = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)

id = input("Enter your Roll No : ")
main_folder = os.getcwd()
os.mkdir('photos/' + id)
sampleNum =  0

while(True):
    ret , frame = cam.read()
    faces = detector.detectMultiScale(frame , 1.3 , 5)
    for( x, y ,w ,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w ,y+h) , (255,0,0) , 2)
        folder_name = os.path.join(main_folder , 'photos', id)
        file_name = id+ '.' + str(sampleNum) + '.jpg'
        file_path = os.path.join(folder_name , file_name)
        
        cv2.imwrite(file_path , frame[y:y+h , x:x+w])
        sampleNum = sampleNum+1
        cv2.imshow('frame' , frame)   
    if sampleNum > 100:
      break
       
cam.release()
cv2.destroyAllWindows()    
