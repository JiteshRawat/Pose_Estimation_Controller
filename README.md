# Pose_Estimation_Controller

A Convolutional neural network is trained on data of 7 different pose to predict them and control game moves in real time.
## Data 
  - Data is collected using Mediapipe's Blaze pose landmark model.
  - 7 different pose recorded : stand, jump, duck, punch, throw, power.
  - 500 images 128 x 128 for each class.
  - You can access dataset from here : https://www.kaggle.com/rawatjitesh/body-pose-recognition
  - In the below image positions duck, punch, kick, throw, stand, jump and power are shown respectively
 
![body_pose_classes](https://user-images.githubusercontent.com/73243338/158011170-5eece4ab-5b66-4ba2-bfa9-dc9b28024b94.png)
  
## Requirements and steps
- You will require an android emulator like Bluestacks5
- Download and install Shadow Fight 3

- Edit game control to the specified keys or edit the gameplay_controller.py for custom keys that are pressed using pyautogui when model predicts a pose
- You can access the model from here : https://drive.google.com/file/d/1UKfa_cSMnQftEFs4ix8bJ1LQwxoFUm8v/view?usp=sharing

