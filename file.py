def fileExists(fileName):
	return os.path.exists(fileName)     # file exists
		&& os.path.isfile(fileName)     # is a file
		&& os.access(fileName, os.F_OK) # file exists
		&& os.access(fileName,os.R_OK)  # is readable

def loadFile(fileName):
	with(fileName, 'r') as file:
		return f.read()


def loadConfig():
	fileName = 'filename.json'
	if fileExists(fileName):
		fileData = loadFile(fileName)
		return json.loads(fileData)
	elif:
		# log an error in system messaging for relay to master
		# errors.append('config file does not exist')
		return None

