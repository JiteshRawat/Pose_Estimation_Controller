import cv2
import numpy as np
import mediapipe as mp

mpPose = mp.solutions.pose
pose= mpPose.Pose()
mpDraw= mp.solutions.drawing_utils

cap= cv2.VideoCapture(0)
pTime= 0
img_counter= 0

while True:
    success, img = cap.read()
    frame = cv2.flip(img, 1)  # flip the frame horizontally
    imgRGB= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results= pose.process(frame)

    k = cv2.waitKey(10)

    if k == 27: # if Esc is pressed
        break

    # Extract and draw pose on plain white image
    h, w, c = img.shape   # get shape of original frame
    opImg = np.zeros([500, 500, c])  # create blank image with original frame size
    opImg.fill(255)  # set white background. put 0 if you want to make it black

    # draw extracted pose on black white image
    mpDraw.draw_landmarks(opImg, results.pose_landmarks, mpPose.POSE_CONNECTIONS,
                           mpDraw.DrawingSpec((255, 0, 0), 2, 2),
                           mpDraw.DrawingSpec((255, 0, 255), 2, 2), 
                           )

    gray = cv2.cvtColor(opImg.astype('uint8'), cv2.COLOR_RGB2GRAY)
    # display extracted pose on blank images
    cv2.imshow("Extracted Pose", gray)
    

    # To collect your own data uncomment below lines and edit position names for eg. stand, jump...
    #img_name= "Position_Names_{}.png".format(img_counter)
    #img_counter += 1
    #cv2.imwrite(img_name, opImg)
    #print('Screenshot captured')
    #time.sleep(0.2)

    # For number of images
    #if img_counter == 100:
    #    break 

cap.release()