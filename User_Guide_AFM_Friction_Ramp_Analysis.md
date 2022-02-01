# AFM-Friction-Ramp-Analysis User Guide

This python (developed with 3.8.10 version) application can be used to analyze ramps/series of AFM lateral force images, providing the correspondig friction vs load plots. 

At present it has only been tested for images obtained with the Nanoscope v9 software on a Multimode 8 AFM. It will probably work for images obtained with some other Nanoscope versions and Bruker/Veeco AFMs, but I am not sure.

## Quick Start

### Running the software

1. Fork/download the repository. 
2. A list of required packages is provided in *requirements.txt*. I suggest you install them in a virtual environment, e.g.:
	```
	python3 -m venv friction_env
	source friction_env/bin/activate
	pip install -r requirements.txt
	```
	If you do not have virtualenv, just follow e.g., these [instructions](https://virtualenv.pypa.io/en/latest/installation.html).
3. From the main folder run:
	```
	python3 -m friction_ramp_analysis
	```
	This will open the following graphical Interface:
	
	![Main Window](UserGuideImages/MainWindow.png)

### Common workflow

The common workflow for analyzing AFM friction data could be as follows:

After initializing the application, go to the menu bar and in **File** (**1**) click on **Load Images**. Then select a set of AFM images containing friction images, in both trace and retrace directions, 
obtained while varying the set point i.e., a common AFM friction data set. You will see something like:

![Main Window](UserGuideImages/MainWindowWithData.png)

You will see the name of the displayed file in (**2**) and the file related data in the plot area (**3**). Specifically:

(**3a**) The topography channel (in case it was registered). You will also see a red horizontal line that highlights the current row, which is actually displayed in (**3b**).

The trace and retrace friction channels are shown in (**3c**) and (**3d**) respectively. The friction traces corresponding to the rows highlighted in red in the friction channels are shown in (**3e**).

The calculated friction vs. load data is shown in (**3f**). At first, this plot will show the raw photodetector signals.

(**4**) In the upper right section of the GUI a set of widgets are shown within the Group Box name **Navigation**. These widgets allow to:

- change the visualized file among those previously loaded.
- change the currently visualized row.
- select the minimum and maximum rows and columns numbers that will be used to calculate friction (after changing these, click **Update**).


## Data Analysis
In the bottom right corner of the main window one can enter the parameters needed for transforming into forces the raw lateral and vertical photodetector signals. Have a look at this [paper](https://pubs.acs.org/doi/full/10.1021/la201673r) and its referenced for the underlying theory.

In the same section it is also possible to enter the vertical photodetector signals corresponding to the cantilever far from the sample at the beginning and end of the experiment. 
This allows correcting drifts in this signal during the time of the experiment. These quantities can be entered manually, or obtained from force curves. For this latter approach, in the menu bar 
go to Analysis->Offset from FZ. The following window will show up:

![FZ GUI](UserGuideImages/FZ1.png)

Zoom in the region corresponding to the free non-interacting cantilever, select whether to calculate the offset from the forward curve, from the backward curve, or from the average of both:

![FZ GUI](UserGuideImages/FZ2.png)

Press the Vertical Offset Button. The press Send to Vi or Send to Vf buttons to send to the Main Window the calculated offset as the one corresponding to the start or to the end of the experiment.

Finally, in the Main Window press Calibrate to get the friction vs load plot in force units.

## Export Data
In the Menu Bar, go to Export->Friction Ramp, and there select between Raw and Calibrated. This will allow you to export the (raw or calibrated) friction vs load plot in 2 columns ASCII file.


