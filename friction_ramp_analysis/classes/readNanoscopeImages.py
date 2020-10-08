###############################################################################
# Import of neccesary packages
###############################################################################
import re
import numpy as np
import argparse
import sqlite3
import io
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class NanoscopeImage():
    '''
    Class that open and read Nanoscope Image Files.
    
    Attributes:
        file_name: Name of the Nanoscope File
        header_end: For checking whether the end of the
                    file header has been reached.
        eof: For checking whether the end of the file
             has been reached.
        headerParameters: Dictionary for parameters of relevance within
                          the file header.

        Image[idx][Channel]: Image Data, where idx refers to the
        index of the image (in case multiple images are loaded) and
        Channel to the type of image

    Methods:
        __init__()
        readHeader()
        searchForParameters()
        searchForHeaderEnd()
        headerToParameters()
        readImages()
        getChannel()
        getChannelIndex()
        flattenImage()
        equalizeTopImage()
        equalizeImage()
    '''

    def __init__(self, file_name):
        '''
        Initializes an object of the class NanoscopeImage,
        uses it for reading the data in the parsed AFM file
        Input parameters:
        file_name: name of the AFM file
        '''

        # We initialize the attribute headerParameters, a dictionary
        # with keys corresponding to strings that identify the lines
        # in the file header with relevant information
        self.headerParameters = {'Data offset':[], 'Data length':[],
        						'Samps/line':[], 'Number of lines':[],
        						'Scan Size':[], 'Line Direction':[],
        						'Valid data len X':[], 'Valid data len Y':[],
        						'2:Image Data':[], 'Z magnify':[],
        						'@2:Z scale':[], '@Sens. Zsens':[],
                                '@2:AFMSetDeflection':[], 'Bytes/pixel':[]}

        # At the beginning we are not at the end of the header
        # or at the endof the file
        self.header_end = 0
        self.eof = 0

        # Name of the file
        self.file_name = file_name

        self.Image = []
        
    def readHeader(self):
        '''
        Reads the header of the Nanoscope file
        '''
        file = open(self.file_name, 'r', encoding='cp1252')

        # Keep reading the file line by line until the end of
        # the header (or the end of the file) is reached.
        # For each line, check whether it contains the keys
        # of headParameters, and if so populate their values, by
        # calling to searchForParameters(). Then, check if the end
        # of the header has been reached by calling searchForHeaderEnd()
        while (not self.header_end) and (not self.eof):
            for line in file:
                self.searchForParameters(line)
                self.searchForHeaderEnd(line, r'\*File list end')
                if self.header_end == 1:
                    break
            else:
                self.eof = 1
        file.close()

    def searchForParameters(self, _line):
        '''
        Identifies whether the input string, _line, contains one of the
        keys of headParameters. If so, pupulates its values with numbers
        contained in _line as well.
        '''
        for key in self.headerParameters:
            if re.search(re.escape(key), _line):
                # print(_line)
                if key == 'Line Direction':
                	searchString = re.findall(r'\w+$', _line)
                	searchString = searchString[0]
                	self.headerParameters[key].append(searchString)
                elif key == '2:Image Data':
                	searchString = re.split(r'"', _line)
                	searchString = searchString[-2]
                	self.headerParameters[key].append(searchString)
                elif key == 'Bytes/pixel':
                	numbers = re.findall(r'\d+$', _line)
                	self.headerParameters[key].append(int(numbers[0]))
                else:
	                numbers = re.findall(r'-?\d+\.?\d+', _line)
	                # If _line contains the strings 'LSB' or '@', only populate
	                # the key value with the last number from _line. If not,
	                # populate it with all numbers.
	                if re.search(r'LSB', _line) or re.search(r'@', _line):
	                    self.headerParameters[key].append(float(numbers[-1]))
	                else:
	                    for number in numbers:
	                        self.headerParameters[key].append(float(number))

    def searchForHeaderEnd(self, _line, _string):
        '''
        Checks if the end of the header has been reached
        '''
        if re.search(r'\*File list end', _line):
            self.header_end = 1
        else:
            self.header_end = 0

    def readImages(self):
        file = open(self.file_name, 'rb')
        for i in range(len(self.headerParameters['Data offset'])):
            self.Image.append({
                'Channel': self.headerParameters['2:Image Data'][i],
                'Line Direction': self.headerParameters['Line Direction'][i],
                'Image Data': np.empty([
                    int(self.headerParameters['Samps/line'][i]),
                    int(self.headerParameters['Number of lines'][i])
                ]),
                'Processed Image Data': np.empty([
                    int(self.headerParameters['Samps/line'][i]),
                    int(self.headerParameters['Number of lines'][i])
                ]),
                'Rows': int(self.headerParameters['Samps/line'][i]),
                'Columns': int(self.headerParameters['Number of lines'][i]),
                'Set Point': self.headerParameters['@2:AFMSetDeflection'][0]
            })
            file.seek(int(self.headerParameters['Data offset'][i]))
            s = file.read(int(self.headerParameters['Data length'][i+1]))
            s = np.frombuffer(
                s,
                dtype='<i{}'.format(2*self.headerParameters['Bytes/pixel'][i]),
                count=int(
                    self.headerParameters['Number of lines'][i])*int(self.headerParameters['Samps/line'][i])).reshape((int(self.headerParameters['Number of lines'][i]), int(self.headerParameters['Samps/line'][i])
                    )
                )
            if self.Image[i]['Channel'] == 'Height':
                s=s*self.headerParameters['@Sens. Zsens'][0]*self.headerParameters['@2:Z scale'][i]/pow(2, 8 * self.headerParameters['Bytes/pixel'][i])
            else:
                s=s*self.headerParameters['@2:Z scale'][i]/pow(2, 8 * self.headerParameters['Bytes/pixel'][i])
            self.Image[i]['Image Data'] = s
            self.Image[i]['Processed Image Data'] = s
        file.close()

    def getChannel(self, channel, direction):
        image = next(
            item for item in self.Image if item["Channel"] == channel and item["Line Direction"] == direction
        )
        return image

    def getChannelIndex(self, channel, direction):
        index = next(
            idx for idx in range(len(self.Image)) if self.Image[idx]["Channel"] == channel and self.Image[idx]["Line Direction"] == direction
        )
        return index

    def flattenImage(self, channel, direction, jdx):
        idx = self.getChannelIndex(channel,direction)
        s = self.Image[idx]['Processed Image Data'].copy()
        if jdx == 6 :
            def func(x, a, b , c, d, e, f, g):
                return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g
            initialParameters = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        elif jdx == 3:
            def func(x, a, b , c, d):
                return a * x**3 + b * x**2 + c * x + d
            initialParameters = np.array([1.0, 1.0, 1.0, 1.0])

        for j in range(self.Image[idx]['Rows']):
            xData = np.arange(self.Image[idx]['Columns'])
            yData = self.Image[idx]['Processed Image Data'][j,:]
            fittedParameters, pcov = curve_fit(func, xData, yData, initialParameters)
            modelPredictions = func(xData, *fittedParameters)
            s[j,:] -= modelPredictions

        self.Image[idx]['Processed Image Data'] = s

    def equalizeTopImage(self, channel, direction, percentile):
        idx = self.getChannelIndex(channel,direction)
        l = np.percentile(self.Image[0]['Processed Image Data'], percentile)
        s = self.Image[idx]['Processed Image Data'].copy()
        s[s>l]=l
        self.Image[idx]['Processed Image Data'] = s

    def equalizeImage(self, channel, direction, width):
        idx = self.getChannelIndex(channel,direction)
        l = np.std(self.Image[idx]['Processed Image Data'])
        mp = np.mean(self.Image[idx]['Processed Image Data'])
        
        s = self.Image[idx]['Processed Image Data'].copy()

        s[s>mp+width*l]=mp+width*l
        s[s<mp-width*l]=mp-width*l

        self.Image[idx]['Processed Image Data'] = s

    #########################################
    # Functions for testing
    #########################################

    def test1(self):
    	fig, ax = plt.subplots()
    	ax.cla()
    	plt.imshow(self.Image[0]['Processed Image Data'], cmap='gray')
    	#plt.colorbar()
    	plt.show()
    	#plt.waitforbuttonpress()

    def test4(self):
    	fig = plt.figure(frameon=False)
    	fig.set_size_inches(4,4)
    	ax = plt.Axes(fig, [0., 0., 1., 1.])
    	ax.set_axis_off()
    	fig.add_axes(ax)
    	ax.imshow(self.Image[0]['Processed Image Data'], cmap='gray', aspect='auto')
    	#plt.colorbar()
    	plt.show()

    def test3(self):
    	l = np.percentile(self.Image[0]['Processed Image Data'],99)
    	print(l)

    def test5(self):
        print(type(self.headerParameters['@2:AFMSetDeflection'][0]))
        print(self.headerParameters['@2:AFMSetDeflection'][0])
        a = self.getChannel('Friction','Retrace')
        fig = plt.figure(frameon=False)
        fig.set_size_inches(4,4)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        b=a['Processed Image Data'].copy()
        b[16,:]=np.max(a['Processed Image Data'])
        ax.imshow(a['Processed Image Data'], cmap='gray', aspect='auto')
        ax.axhline(y=16,color='red')
        plt.show()
        idx = self.getChannelIndex('Height','Retrace')
        print(idx)

    	

    	
	    


###############################################################################
# Run if this is the main program
# Used for testing
###############################################################################
if __name__ == "__main__":

    # Load parsed input Nanoscope file
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="path to the Nanoscope file")
    args = vars(ap.parse_args())

    # Create an object of the NanoscopeImage class
    imageObject = NanoscopeImage(args['input'])

    # Reads the header of file_name, and populates
    # the headerParameters dictionary
    imageObject.readHeader()

    # Read data from the file
    imageObject.readImages()
    
    # Calls a method for testing
    imageObject.test5()
