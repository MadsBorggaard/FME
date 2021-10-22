import os, uuid, pyodbc
import fme
import pathlib

logFile = fme.logFileName
path = pathlib.Path(fme.getAbsolutePath(logFile)).parent.resolve()

uuidFile = os.path.join(path, 'uuid.txt')
local_uuid = ''
if not os.path.isfile(uuidFile):
    with open(uuidFile, 'w') as f:
        local_uuid = uuid.uuid4()
        f.write(str(local_uuid))    
