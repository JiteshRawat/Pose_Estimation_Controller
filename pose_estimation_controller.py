import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import pyautogui
import time

pose_names= {0: 'stand', 1: 'duck',
             2: 'jump',  3: 'punch',
             4: 'power', 5: 'kick',
             6: 'throw'}

model = load_model('Body_Pose_Model_v3')

#Using mediapipe pose solution
mpPose = mp.solutions.pose
pose= mpPose.Pose()
mpDraw= mp.solutions.drawing_utils

cap= cv2.VideoCapture(0)

#model prediction
def predict_image(image):
    pred_array = model.predict(image)
    result = pose_names[np.argmax(pred_array)]
    score = float("%0.2f" % (max(pred_array[0]) * 100))
    print(f'Result: {result}; Score: {score}')
    if max(pred_array[0]) < 1.0:
        return "no_result"

    return result

while True:
    success, img = cap.read()
    frame = cv2.flip(img, 1)  # flip the frame horizontally
    imgRGB= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results= pose.process(frame)
    
    # Extract and draw pose on plain white image
    h, w, c = img.shape   # get shape of original frame
    opImg = np.zeros([128, 128, c])  # create blank image with original frame size
    opImg.fill(255)  # set white background. put 0 if you want to make it black

    # draw extracted pose on black white image
    mpDraw.draw_landmarks(opImg, results.pose_landmarks, mpPose.POSE_CONNECTIONS,
                           mpDraw.DrawingSpec((255, 0, 0), 2, 2),
                           mpDraw.DrawingSpec((0, 0, 255), 2, 2))
    
    #Processing image for model prediction
    gray = cv2.cvtColor(opImg.astype('uint8'), cv2.COLOR_RGB2GRAY)
    target= gray.reshape(-1, 128, 128, 1)
    prediction = predict_image(target)
    
    #perform move based on prediction
    if prediction == 'punch':
            pyautogui.keyDown('right')
            pyautogui.press('d')
            time.sleep(0.2)
            pyautogui.press('d')
            time.sleep(0.2)
            pyautogui.press('d')
            time.sleep(0.2)
            pyautogui.press('d')
            
    elif prediction == 'power':
            pyautogui.keyDown('up')
            pyautogui.press('f')
            time.sleep(0.1)
            pyautogui.press('f')

    elif prediction == 'kick':
            pyautogui.keyDown('right')
            pyautogui.press('s')
            time.sleep(0.2)
            pyautogui.press('s')

    elif prediction == 'duck':
        pyautogui.keyDown('down')
        pyautogui.press('down')
        time.sleep(0.2)
        pyautogui.keyDown('left')
        pyautogui.press('left')

    elif prediction == 'jump':
        pyautogui.keyDown('up')
        pyautogui.press('up')
        time.sleep(0.2)
        
    elif prediction == 'throw':
        pyautogui.press('w')
        pyautogui.press('w')
        time.sleep(0.2)

    elif prediction == 'no_result':
        print(prediction)