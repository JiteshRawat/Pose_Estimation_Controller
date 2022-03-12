# Pose_Estimation_Controller

A Convolutional neural network is trained on data of 7 different pose to predict them and control game moves in real time.
## Data 
  - Data is collected using Mediapipe's Blaze pose landmark model.
  - 7 different pose recorded : stand, jump, duck, punch, throw, power, kick.
  - 500 images 128 x 128 for each class.
  - You can access dataset from here : https://www.kaggle.com/rawatjitesh/body-pose-recognition
  - In the below image positions duck, punch, kick, throw, stand, jump and power are shown respectively.
 
![body_pose_classes](https://user-images.githubusercontent.com/73243338/158011170-5eece4ab-5b66-4ba2-bfa9-dc9b28024b94.png)
  
## Requirements and setup
- You will require an android emulator like Bluestacks5. You can download it from https://www.bluestacks.com/
- Download and install Shadow Fight 3.
- Edit game control to the specified keys or edit the gameplay_controller.py for custom keys that are pressed using pyautogui when model predicts a pose.
- You can access the model from here : https://drive.google.com/file/d/1UKfa_cSMnQftEFs4ix8bJ1LQwxoFUm8v/view?usp=sharing

## About model
- The model has 3 layers of Convolutions and 1 Dense layer. 
- The model is trained on 128 x 128 gray scale images of each class.
- Test accuracy is 92 %.
- Model prediction time is around 0.2 secs.

## Tips
- Before using controller run data collector to check your body posture is displayed as shown in data.
- Try adjusting camera angle so that the postures match postures in data.

## Example

![pose_control_gif](https://user-images.githubusercontent.com/73243338/158012262-5734cfee-9c9a-499f-bf08-465952e32d2e.gif)
