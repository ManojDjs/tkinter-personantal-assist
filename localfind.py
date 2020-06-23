import os, win32api, fnmatch, sys
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

def getDrives():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]
	return drives

filesList = []
def find(query, drive, isList=False):
	filesList.append("\t\t\t ------------------------------ Files in " +drive+ " Drive ------------------------------------")
	for dirpath, dirnames, filenames in os.walk(drive):
		for fileName in filenames:
			if fnmatch.fnmatch(fileName, query): # Match search string
				if  not isList:
					speak.Speak("Opening " + query)
					os.startfile(os.path.join(dirpath, fileName))
					return
				else:
					filesList.append(os.path.join(dirpath, fileName))
def openFile(query):
	drivelist = getDrives()
	for drive in drivelist:
		find(query, drive)
		
def listAllFiles(query):
	filesList.clear()
	query = query.replace('files', '')
	query = query.replace('file', '')
	query = "*."+query
	drivelist = getDrives()
	for drive in drivelist:
		find(query, drive, True)
	speak.Speak('Total files found '+len(filesList))
	return filesList
		
openFile('Desktop')