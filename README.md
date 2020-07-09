# Face-Recognition
All working Face Recognition project made on PYTHON
Introduction:

The software is to provide security by detecting, recognizing the face. This software matches the detected face in the database. If the face data is found, it returns the name along with a blue box on the face. If the face is not stored in the database, it displays a red box on the specific face. 

Installation:

* Install Python 3.7.2 from https://www.python.org/downloads/..
* Install by clicking next on the prompted screen.
* After installing python 3.7.2, install openCV python package from https://pypi.org/project/opencv-python/
* Check whether Tkinter GUI is available on your machine or not. If not present, download and install tkinter.
* To check open this link and check the software version of python https://www.python.org/download/mac/tcltk/

Configuration:

* Right click on this pc.
*  Open properties from the dropdown list. 
* Select ADVANCED SYSTEM SETTING from the menu present on the left side of the screen.
*  From the prompted dialogue box, select ENVIRONMENT VARIABLE. 
* Another screen will open containing various parameters. select PATH. Set path to C:\Users\AppData\Local\Programs\Python\Python37\ .

Saving A New Face:

* To add a new face data in the database, open index.py file.
* A window will open, select ADD image option from it.
* An another screen will prompt askig for name. Add name to it.
* Camera screen will open. slightly rotate your face towards left and then towards right.
* Now again open index.py file and choose TRAIN DATA from it.
* Now your face data is saved in the database.

Delete A Face:

* To start using the face detection and recognition, open name.xls file.
* Delete the last number of the file and save it.
* Open training_img folder and delete the folders with same number inside the folder.
* The face will be deleted.

To Detect Face:

* To start using the face detection and recognition, open index.PY file.
* The camera screen will pop up and start detecting the faces.
* After detecting a face, the program will match that face data with the face data present in the database.
*  If the face data is matches to an extent of 60%, it will display a blue box and saved name on the face.
*  If the face is unknown, the camera screen will display the face with a red block.

Maintainance:

* Database should be maintained properly.
* It is compulsory that while saving a new face data, only single person should be present in front of the camera. This will ensure that while detectinhg face, it will have accuracy and correctness.
