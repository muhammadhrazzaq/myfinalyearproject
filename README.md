                      

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
* To run the fastapi server run **uvicorn main:app --reload --host 127.0.0.1 --port 8000** if this command gives you an error please try to run with 
  **python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000**
* If you get the this ![image](https://user-images.githubusercontent.com/107313180/189058777-d16af084-bf99-4684-90f9-6d2c01bedd20.png) this mean server is       running
* Go to url (http://127.0.0.1:8000/docs#) to get the gui of api. you will get portal like this ![image](https://user-images.githubusercontent.com/107313180/189058985-10f6bd3a-01b9-4354-a954-f1aad6c01966.png)
* /obj-to-json — This endpoint is for returning the detected object value with the JSON format .You can execute the endpoint by clicking the try it out button and upload an image. .Expected result is {"result": []} with 200 status code. If the model detected something with more than 0.5, it will append in the array.
* If response successful you will get following response ![image](https://user-images.githubusercontent.com/107313180/189059716-61602f0f-f5be-4856-9c15-eb34e1f602ce.png)

* /obj-to-img — This endpoint is for returning the detected object value with image format .You can execute the endpoint by clicking the try it out button and upload an image. You will get results like this ![image](https://user-images.githubusercontent.com/107313180/189060469-dd292293-79d7-45e4-945a-f6bc64043ab9.png)
* /withoutCustomeobj-to-img - This endpoint is for returning the detected object value with image format .You can execute the endpoint by clicking the try it out button and upload an image. In this endpoint I used original yolov5 weights . This endpoints weights are trained on more then 80 classes. you will get result like this ![image](https://user-images.githubusercontent.com/107313180/189061323-6fe33db6-5281-4c6c-83b0-e54691fa646a.png)








     

