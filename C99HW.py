import os
import shutil
import time

def main():
    deletedFolders = 0
    deletedFiles = 0
    path = ""
    days = 30
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for folders, rootfolder, files in os.walk(path):
            if seconds >= getage(rootfolder):
                removeFolder(rootfolder)
                deletedFolders = deletedFolders + 1
            else:
                for folder in folders:
                    folderpath = os.path.join(rootfolder, folder)
                    if seconds >= getage(folderpath):
                        removeFolder(folderpath)
                        deletedFolders = deletedFolders + 1
                for file in files:
                    filepath = os.path.join(rootfolder, file)
                    if seconds >= getage(filepath):
                        removeFile(filepath)
                        deletedFiles = deletedFiles + 1
            else:
                if seconds >= getage(path):
                    removeFile(path)
                    deletedFiles = deletedFiles + 1
    else:
        print("Path not found")
print(deletedFolders, deletedFiles)
def removeFolder(path):
    if not shutil.rmtree(path):
        print("Folder removed")
    else:
        print("Unable to delete the folder")
def removeFile(path):
    if not os.remove(path):
        print("File removed")
    else:
        print("Unable to delete the file")
def getage(path):
    seetime = os.stat(path).st_ctime
    return seetime
main()