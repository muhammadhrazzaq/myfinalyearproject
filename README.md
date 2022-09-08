                      

I used yolov5s to train my model on custom data. In order to run the training code use **fyp.ipynb** jupyter file. I used Fastapi python rest framework to develp the apis.

# Folder Details

* **dataset** folder contains two folders dat and labels . dat has all the images and labels are the text file of labels.
* **labelImg** is the folder which contains the code for Labelimg tool . Through **LabelImg** I have labelled my dataset.
* **model** folder contains the weights of custom trained model.
* **Yolov5** folder contains the offical code from the yolov5 repository.
* **classic_aresnal.jpg** just arsenal football team picture which is being used for just testing purposes.
* **main.py** is the main python script to run the Fastapi 
* **sg.py** file is segmentation file bascially in which custom yolov5s model weights and original pretrained model weights are being loaded.
* **yolo5s.pt** is the file of orginal weights of yolov5 model which are trained on more then 80 classes.
* **requirement.txt** is the text file which contains all the required libraries to run Fastapi.

## Installation Process

**To Run the API You Have To Install libraires through Requirements.txt by following command**
**First Create the virtual Environment If you don't have virtualenv library installed on your system please [Click to Go to virtalenv installation guide](https://pypi.org/project/virtualenv/)**
* Activate your created environment
* Run pip command to install libraries **pip install -r ./requirements.txt**
* To run the fastapi server run **uvicorn main:app --reload --host 0.0.0.0 --port 8000** if this command gives you an error please try to run with 
  **python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000**
* Go




     

