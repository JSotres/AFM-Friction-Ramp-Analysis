###############################################################################
# Import of neccesary packages
###############################################################################
import re
import numpy as np
import argparse
import io
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class NanoscopeRamp():

    def __init__(self, file_name):
        self.headerParameters = {'Sens. Zsens:': [],
                                 'Data offset': [],
                                 'Data length:': [],
                                 'Z magnify': [],
                                 '4:Ramp Size:': [],
                                 'Samps/line:': [],
                                 '4:Image Data:': [],
                                 'Bytes/pixel':[],
                                 '@4:Z scale': []
                                 }
        # At the beginning we are not at the end of the header
        # or at the endof the file
        self.header_end = 0
        self.eof = 0
        self.file_name = file_name
        self.Ramp = []

    def readHeader(self):

        file = open(self.file_name, 'r', encoding='cp1252')
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
                if key == '4:Image Data:':
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
                    if key == '@4:Z scale':
                        self.headerParameters[key].append(float(numbers[0]))
                    elif re.search(r'LSB', _line) or re.search(r'@', _line):
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

    def readRamps(self):
        file = open(self.file_name, 'rb')
        for i in range(len(self.headerParameters['Data offset'])):
            self.Ramp.append({
                'Channel': self.headerParameters['4:Image Data:'][i+1],
                'RawX': np.linspace(
                    0,
                    1,
                    int(self.headerParameters['Samps/line:'][-1])
                ),
                'RawY': np.empty([
                    2, int(self.headerParameters['Samps/line:'][-1])
                ])
            })
            file.seek(int(self.headerParameters['Data offset'][i]))
            s = file.read(int(self.headerParameters['Data length:'][i+1]))
            print(len(s))
            s = np.frombuffer(
                s,
                dtype='<i{}'.format(2*self.headerParameters['Bytes/pixel'][i]),
                count=int(2*self.headerParameters['Samps/line:'][-1])
                ).reshape((
                    2,
                    int(self.headerParameters['Samps/line:'][-1])
                ))*self.headerParameters['@4:Z scale'][i]
            self.Ramp[i]['RawY'] = s
            self.Ramp[i]['RawX'] *= self.headerParameters['4:Ramp Size:'][i]
            self.Ramp[i]['RawX'] *= self.headerParameters['Sens. Zsens:']

    def test1(self):
        print(self.headerParameters['Sens. Zsens:'])
        print(self.headerParameters['Data offset'])
        print(self.headerParameters['Data length:'])
        print(self.headerParameters['Z magnify'])
        print(self.headerParameters['4:Ramp Size:'])
        print(self.headerParameters['Samps/line:'])
        print(self.headerParameters['4:Image Data:'])
        print(self.headerParameters['Bytes/pixel'])
        print(self.headerParameters['@4:Z scale'])
        # print(self.Ramp[0]['RawX'])
        plt.plot(self.Ramp[0]['RawX'], self.Ramp[0]['RawY'][0][:])
        plt.plot(self.Ramp[0]['RawX'], self.Ramp[0]['RawY'][1][:])
        plt.show()

###############################################################################
# Run if this is the main program
###############################################################################
if __name__ == "__main__":
    # Load parsed input force volume file and output database
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="path to the Nanoscope file")
    args = vars(ap.parse_args())

    # Create an object of the NanoscopeForceVolumeFileToDataBase class
    rampObject = NanoscopeRamp(args['input'])
    rampObject.readHeader()
    # rampObject.searchForParameters()
    rampObject.readRamps()

    rampObject.test1()
