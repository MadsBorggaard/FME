import uuid        
import os
import pathlib
import fme
import csv

logFile = fme.logFileName        
path = pathlib.Path(fme.getAbsolutePath(logFile)).parent.resolve()
workspacename = logFile.split('\\')[-1][:-4]
csvFile = os.path.join(path, workspacename + 'Statistics.csv')

header = ['dato', 'id', 'name', 'status', 'elapsedRunTime', 'cpuSysTime', 'cpuUserTime', 'cpuTime', 'failureMessage', 'featuresRead', 'featuresWritten', 'totalFeaturesRead', 'totalFeaturesWritten']
if not os.path.isfile(csvFile):
    print('Creating Statistics file')
    with open(csvFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)  
