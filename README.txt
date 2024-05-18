To Train any model of the specified models :
1-Open the "ModelNametrain" file in your Jupyter notebook

2-make sure all the libraries specified are imported

3-Change "DATASET_DIR" to the directory that holds the folder of your data set 
the architecture of the data set should be as follows :
->dataset
  ->Shoulder Press Correct
    videos of Correct Shoulder Press exercise
  ->Shoulder Press Wrong
    videos of Wrong Shoulder Press exercise
			

so that every Exercise has  2 folders one for the correct form and the other for the wrong form and the name of the folder is the name of that Exercise and whether it's correct or not which will also be the label that will be displayed during testing and the folder contains the videos of that exercise


4-Change "CLASSES_LIST" to the list of folders' names that you have in tyour dataset


5- Run all cells and after that you'll find that the model is saved 



To Test The Model:

1-Open the "App.py" file in Visual studio code or any python IDE

2-make sure all the libraries specified are imported

3-change "model" to the name of the saved model that exixts in the folder of the project

4-specify the dataset directory in "data_dir" to get the labels

5- Run the project and it will open the webcam to get the input and show the results
 