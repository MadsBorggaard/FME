import os, uuid, pyodbc
import fme
import pathlib
import datetime

# variabler der skal tilpasses
serverNavn = 'NAVNET PÅ SQL SERVEREN'
databaseNavn = 'DATABASENAVN'
schemaNavn = 'SCHEMANAVN'
tabelNavn = 'TABELNAVN'

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
failureMessage = str(fme.failureMessage).replace("'", '"')
if 'Terminator: Termination Message:' in failureMessage:
    
    failureMessage = failureMessage.replace('Terminator: Termination Message: ', '').replace('"', '')
    status = 'Termination'
featuresRead = str(fme.featuresRead).replace("'", '"')
featuresWritten = str(fme.featuresWritten).replace("'", '"')
totalFeaturesRead = fme.totalFeaturesRead
totalFeaturesWritten = fme.totalFeaturesWritten
now = datetime.datetime.now()
dt_string = now.strftime("%y/%m/%d %H:%M:%S")
sql = f'''INSERT INTO [{schemaNavn}].[{tabelNavn}] (dato, id, name, status, elapsedRunTime, cpuSysTime, cpuUserTime, cpuTime, failureMessage, featuresRead, featuresWritten, totalFeaturesRead, totalFeaturesWritten)
                VALUES ('{now}', '{local_uuid[0]}', '{workspaceName}', '{status}', {elapsedRunTime}, {cpuSysTime}, {cpuUserTime}, {cpuTime}, '{failureMessage}', '{featuresRead}', '{featuresWritten}', {totalFeaturesRead}, {totalFeaturesWritten})
                '''
connectionString = (f'''Driver={{SQL Server}};Server={serverNavn};Database={databaseNavn};Trusted_Connection=yes;''')      
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

cursor.execute(sql)
conn.commit()
