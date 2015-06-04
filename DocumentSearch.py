import os
#Regular expression
import re

class DocumentSearch(object):
    """Read the document file and search word within in the documents"""

    _lstContent = []
    # append empty string at 0 index so that document number starts from 1
    #_lstContent.append("")
    _dictTextInDocumentNo = {}

    # document location
    __currentDirectory = os.path.dirname(__file__)
    __virtualFilePath = "Uploads/ap_docs.txt" #"Uploads/docs2.txt"
    __filePath = os.path.join(__currentDirectory, __virtualFilePath)
    fileReadMode = "r"


    def __init__(self, *args):
        self._dictTextInDocumentNo.clear()

    def search(self, lstSearchText):
        dictFoundDocumentNo = {}        
        previousSet = set()
        currentSet = set()

        for searchText in lstSearchText:
            dictFoundDocumentNo = self.__searchForWordInDocument(searchText)
        
        if len(dictFoundDocumentNo) <= 1:
            # text found in only 1 document
            return list(dictFoundDocumentNo.values())
               
        for value in dictFoundDocumentNo.values():
            for i,item in enumerate(value):
                currentSet.add(value[i])
                if i + 1 == len(value):
                    if len(previousSet) > 0:
                        previousSet = currentSet & previousSet
                    else:
                        previousSet = currentSet | previousSet
                    currentSet.clear()
        return list(previousSet)

    def __searchForWordInDocument(self, searchText):
        self.readFile()        
        for index in range(len(self._lstContent)):
            if re.search("\\b" + searchText + "\\b", self._lstContent[index], re.IGNORECASE) != None:
                #assign multiple values to a key in a dictionary
                self._dictTextInDocumentNo.setdefault(searchText, []).append(index)
        return self._dictTextInDocumentNo

    def readFile(self):
        try:
            with open(self.__filePath, self.fileReadMode) as doc:
                content = doc.read()
                self._lstContent = content.split("<NEW DOCUMENT>")
                # remove empty strings from the list
                self._lstContent = filter(None, self._lstContent)
        except IOError:
            print "File not found."
        return self._lstContent