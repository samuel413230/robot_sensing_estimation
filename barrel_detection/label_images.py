from roipoly import roipoly
import matplotlib.pylab as pl
import os
import numpy as np
import cv2

folder = "trainset"
masks = []
lengths = []

for index in range(50):
    # load files from 
	filename = os.listdir(folder)[index]
	print filename
    
    # record the distance from file name
	lengths.append(filename.split('.')[0])
    
    # read the image and mark the red regions with polygons
	img = cv2.imread(os.path.join(folder, filename))
	pl.imshow(img)
	MyROI = roipoly(roicolor='r') #let user draw first ROI 
	masks.append(MyROI.getMask(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)))

# save the masks and lengths with numpy into .npy for the training code
np.save("masks.npy",masks)
np.save("lengths.npy",lengths)
