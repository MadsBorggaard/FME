import os, uuid, pyodbc
import fme
import pathlib
import datetime

logFile = fme.logFileName
path = pathlib.Path(fme.getAbsolutePath(logFile)).parent.resolve()
workspaceName = logFile.split('\\')[-1][:-4]

print(f'Logfile: {logFile} - path: {path}')
uuidFile = os.path.join(path, 'uuid.txt')
local_uuid = ''

with open(uuidFile, 'r') as f:
    local_uuid = f.readlines()

status = 'OK' if fme.status else 'Fejl'
elapsedRunTime = fme.elapsedRunTime
cpuSysTime = fme.cpuSysTime
cpuUserTime = fme.cpuUserTime
cpuTime = fme.cpuTime
failureMessage = fme.failureMessage
featuresRead = str(fme.featuresRead).replace("'", '"')
featuresWritten = str(fme.featuresWritten).replace("'", '"')
totalFeaturesRead = fme.totalFeaturesRead
totalFeaturesWritten = fme.totalFeaturesWritten
now = datetime.datetime.now()
dt_string = now.strftime("%y/%m/%d %H:%M:%S")

sql = f'''INSERT INTO [dbo].[FME_Statestik] (dato, id, name, status, elapsedRunTime, cpuSysTime, cpuUserTime, cpuTime, failureMessage, featuresRead, featuresWritten, totalFeaturesRead, totalFeaturesWritten)
                VALUES ('{now}', '{local_uuid[0]}', '{workspaceName}', '{status}', {elapsedRunTime}, {cpuSysTime}, {cpuUserTime}, {cpuTime}, '{failureMessage}', '{featuresRead}', '{featuresWritten}', {totalFeaturesRead}, {totalFeaturesWritten})
                '''

#print(sql)        

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-A4RRJ6BE\SQLEXPRESS;'
                      'Database=Mads;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute(sql)
conn.commit()

print(fme.numFeaturesLogged)
