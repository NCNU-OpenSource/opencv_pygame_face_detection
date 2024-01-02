import pygame
import cv2
import os
import datetime


# Pygame window setup
pygame.init()
screen = pygame.display.set_mode((640,480)) 

# Open webcam
cap = cv2.VideoCapture(0)

# Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

num_faces = 0

run = True
while run:

    # Read frame from webcam
    ret, frame = cap.read()

    h, w = frame.shape[:2] 
    #print(f"Frame: ({w} x {h})")

    if not ret:
        print("Error getting frame from webcam")
    # OpenCV image processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    num_faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 

    # Convert to Pygame surface and display    
    pygame_frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1],"BGR")
    screen.blit(pygame_frame, (0,0))
    pygame.display.flip()


    img_folder = 'webcam_pics'
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    now = datetime.datetime.now()

    # Check events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # Capture image with faces marked 
                if frame is None:
                    print("Error, no webcam frame to save")
                else: 
                    filename = now.strftime('%Y%m%d_%H%M%S') + '.jpg' 
                    img_path = os.path.join(img_folder, filename)  
                    number_faces = len(num_faces)
                    print(f"Number of faces detected: {number_faces}")
                    cv2.imwrite(img_path,frame)
                    print("picture taken sucess")
    
'''
    if ret == True:
        if cv2.waitKey(1) & 0xFF==ord("c"):
            cv2.imwrite('capture.jpg', frame)  
            print("picture taken sucess")
'''
pygame.quit()
cap.release()