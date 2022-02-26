import face_recognition
import cv2
import numpy as np
from application import *
import os,sys
import cv2





#sys.path.append(os.path.abspath(os.path.curdir))

'''
for encoding in imageEncodings:
    for j in range(len(dataEncodingsList)):
        matches = face_recognition.compare_faces(dataEncodingsList,encoding,tolerance=0.6)
'''

def login_face_authentication():

    cap=cv2.VideoCapture(0)

    #bilal1_img=face_recognition.load_image_file(r"D:\python\AI\vision\documents\images_videos\bilal.jpeg")
    bilal2_img=face_recognition.load_image_file(r"D:\python\AI\vision\documents\images_videos\bilal.jpg")
    #muthasim_image=face_recognition.load_image_file(r"D:\python\AI\vision\documents\images_videos\muthasim.png")

    #b1face_loc=face_recognition.face_locations(bilal1_img)
    #bilal1_encoding=face_recognition.face_encodings(bilal1_img,b1face_loc)

    b2face_loc=face_recognition.face_locations(bilal2_img)#print(b2face_loc)
    bilal2_encoding=face_recognition.face_encodings(bilal2_img,b2face_loc)[0]    #print(bilal2_encoding) # [array(encodings)]   arr[0]

    #muthasim_face_loc=face_recognition.face_locations(muthasim_image)#print(b2face_loc)
    #muthasim_encoding=face_recognition.face_encodings(muthasim_image,muthasim_face_loc)    #print(bilal2_encoding) # [array(encodings)]   arr[0]
    #print(muthasim_encoding[0].shape)            #128

    #result=face_recognition.compare_faces([bilal1_encoding[0]],bilal2_encoding[0])

    #known_encodings_database=[bilal2_encoding[0],muthasim_encoding[0]]
    known_names=['bilal2','muthasim']
    #result=False
    while True:
        ret,frame=cap.read()
        if ret:
            #cv2.imshow('video',frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #colored output image
            unknow_face_loc=face_recognition.face_locations(frame)           #[(192, 489, 415, 266)]      x1,y1      w,h        
            if len(unknow_face_loc)>0:                             # for no error in following lines
                print(unknow_face_loc)
                #(x1,y1,w,h)=unknow_face_loc[0]
                (top,right,bottom,left)=unknow_face_loc[0]
                #p1,p2=(x1,y1),(x1+w,y1+h)
                p1,p2=(left,top),(right,bottom)
                #print("p1 ",p1," p2 ",p2)
                #print(unknow_face_loc)             # when [] then error in face_encoding []  so no array(face) inside [] so index[0] shows out of range error
                #print(face_recognition.face_encodings(frame,unknow_face_loc)) 
                unknow_face_encodings=face_recognition.face_encodings(frame,unknow_face_loc)[0]         # [array(face)]    so [0] index
                #result=face_recognition.compare_faces([unknow_face_encodings],bilal2_encoding[0])
                matches = face_recognition.compare_faces([bilal2_encoding],unknow_face_encodings,tolerance=0.5)      #known_encodings_database it is in list format so no need for [enoding]
                index_argmax=np.argmax(matches)
                #print(matches,"\t",index_argmax)
                #result=face_recognition.compare_faces([unknow_face_encodings],muthasim_encoding[0])                #print(result)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #colored output image
                cv2.imshow(known_names[index_argmax],frame) 
                if matches[0]==True:
                    cv2.rectangle(frame,p1, p2,(0,255,255),2)
                    #cv2.putText(frame,known_names[index_argmax],(x1,y1-3),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)
                    cv2.putText(frame,known_names[index_argmax],(left+5,top-3),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)
                    
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #colored output image
                    cv2.imshow(known_names[index_argmax],frame)
                    result='authenticated {}'.format(known_names[index_argmax])
                    print(result)
                    #login_window.destroy()
                    #app()
                    #logged_in=True
                #print(face)
        if cv2.waitKey(1) & 0xFF==ord('q'):         
            #print(cv2.waitKey(1))            
            cap.release()
            cv2.destroyAllWindows()

login_face_authentication()
#login_face_authentication()


        


