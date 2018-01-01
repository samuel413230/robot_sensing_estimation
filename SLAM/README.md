*****Instructions to run the code and where to put the required files*****

Required files:
	load_data.py, p3_utils.py should be in the same directory as the jupyter notebook code.ipynb
	The training set folders "joint", "lidar", "cam" should be in the same directory as code.ipynb, in order for the code to read in those datasets correctly. The path to look for those dataset files are hardcoded.
	The test set files should be in the same folders mentioned above with the training set files. For example, test_joint.mat should be in the "joint" folder, test_lidar.mat should be in the "lidar" folder, etc.

To run different training sets or the test set:
	In the cell for simple integration and particle filter SLAM, there are some fields you need to change to run different datasets.
	Below the definition of the function new_map(), you will see the comments # train set and # test set. These two blocks will load the respective dataset file into the variables lidar_data0 and joint_data0. (neglect the number '0' at the end of those variable names)
	For the train set block, you need to change the value of dataset_num to the corresponding number of the dataset you want to run. You also need to comment out the test set block in order to load in the train set data.
	For the test set block, you just need to uncomment it and comment the train set block.

The folder map_images contain all the maps that I saved during my code development and runs on the train and test set.

