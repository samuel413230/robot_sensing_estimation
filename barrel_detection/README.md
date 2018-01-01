To label images with roipoly and parse file name for distances:
	python2 label_images.py


To train:
	Require masks.npy and distances.npy
	Open HW1_Trainset_Code.ipynb


To run tests:
	Open HW1_Testset_Code.ipynb
	Run 1st cell to compile all functions
	Run 2nd cell to run testing on images in folder "testset"
	For each image, this will print out:
		image name
		original picture with bounding box for detected barrel
		coordinates for bottom left and top right
		distance


Folder testset_result_images:
	Contain pictures of mask, contours, and bounding box for each image in the testsets