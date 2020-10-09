# AFM-Friction-Ramp-Analysis User Guide

This python application can be used to analyze ramps/series of AFM lateral force images, providing the correspondig friction vs load plots. 

At present it has only been tested for images obtained with the Nanoscope v9 software on a Multimode 8 AFM. It will probably work for images obtained with some other Nanoscope versions and Bruker/Veeco AFMs, but I am not sure.

## Quick Start

1. Clone/fetch/download the repository.(I have not tested it with other versions).
2. A virtualenv virtual environment is provided with the repository. To activate it, just go to the main folder and type:
	```python
	source env/bin/activate
	```
	If you do not have virtualenv, just follow these [instructions](https://virtualenv.pypa.io/en/latest/installation.html).

	If you prefer other strategies, you will need the following packages:
	* PyQt5 5.15.0
	* matplotlib 3.3.2
	* numpy 1.19.2 
	* scipy 1.5.2
3. From the main folder run:
	```python
	python -m friction_ramp_analysis
	```
	Thiw will open the following graphical Interface:
	![Main Window](UserGuideImages/MainWindow.png)

## Loading and looking at data
After initializing the application, go to the menu bar and in File click on Load Images. Then select a series of consecutive AFM images obtained while varying the set point.
