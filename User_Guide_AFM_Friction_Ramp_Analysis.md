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

(**4**) In the upper right section of the GUI a set of widgets are shown within the Group Box named **Navigation**. These widgets allow to:

- change the visualized file among those previously loaded.
- change the currently visualized row.
- select the minimum and maximum rows and columns numbers that will be used to calculate friction (after changing these, click **Update**).

(**5**) In the middle right section of the GUI a set of widgets are shown within the Group Box named **Calibration**. These allow to set values for the parameters needed to transform the raw data (photodetector signals) 
into force values. You can have a look at this [paper](https://pubs.acs.org/doi/full/10.1021/la201673r) and references therein for the underlying theory and meaning of the different parameters. 
The user will need to obtain some of these parameters independently, and provided them to the software: i) the effective tip height (in nm), ii) the lateral sensitivity of the AFM (in rad/V), iii) the torsional constant of 
the cantilever (in nm\*nN/rad), iv) the vertical sensitivity (in nm/V) and v) the normal constant of the cantilever (in N/m).

This group of parameters within the **Calibration** Group Box also include the vertical photodetector signal corresponding to the cantilever far from the sample at the beginning and at the end of the experiment i.e., the 
offset equilibrium values. The user can enter these values directly if they have been previously found. However, the software also allows to calculate them from normal force measurements in case they have been acquired at 
the beginning and end of the experiment. For this, in the menu bar go to (**6**) **Analysis**->**Offset from FZ**. You will be asked to load a normal force measurement. Then, the following gui will show up:

![FZ GUI](UserGuideImages/FZ1.png)

You will need to zoom in the region corresponding to the free non-interacting cantilever. For this, first select the Zoom icon in the plot menu bar and then zoom in the corresponding region as indicate in the figure 
above. You should see something like the following: 

![FZ GUI](UserGuideImages/FZ2.png)

First, you will need to select in (**A**) whether to calculate the offset from the forward curve, from the backward curve, or from the average of both. Then, press the **Vertical Offset** button (**B**). The 
calculated average value will show up in the gui edit box. Finally, press **Send to Vi** or **Send to Vf** buttons (**C**) to send to the Main Window the calculated offset as the one corresponding to the start 
or to the end of the experiment.

Back in the Main Window tou can now press the **Calibrate** push button. This will provide both load and friction in force (N) units. It will update as well the friction vs load plot (**3f**), now 
in force units.

If you go in the menu bar to (**6**) **Analysis**->**Friction Fit**, you will be able to fit the calibrated friction vs load data to either a **Single Asperity Model** or to a **Multiple Asperity Model**. The obtaned fricton 
coefficient (mu) and adhesion force will show up in the Group Box named **Fit Parameters** in the bottom right section of the gui (**7**).

(**8**) In **View** within the Menu Bar you will be able to switch between raw and calibrated data.

(**9**) in **Export** within the Menu Bar you will be able to export different sets of data as csv files. Specifically, the friction ramp (in raw or calibrated units) and the visualized friction profiles i.e., 
those in (**3e**).

(**10**) In case that your files include friction channels obtained while operating in the lift mode, you can perform all the analysis detailed above on these channels by selecting instead **Lift** within the **Scan Type** 
menu in the menu bar.




