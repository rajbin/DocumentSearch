import os
#Regular expression
import re

class DocumentSearch(object):
    """Read the document file and search word within in the documents"""
    
    # private objects
    _lstContent = []
    _dictTextInDocumentNo = {}

    # document location and file read mode
    __currentDirectory = os.path.dirname(__file__)
    __virtualFilePath = "Uploads/ap_docs.txt" #"Uploads/docs2.txt"
    __filePath = os.path.join(__currentDirectory, __virtualFilePath)
    fileReadMode = "r"


    def __init__(self, *args):
        self._dictTextInDocumentNo.clear()

    # Search for word entered by the user and list the document no in which all the text were found
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
                        # use SET INTERSECTION to find document no. which contains all the search text
                        previousSet = currentSet & previousSet
                    else:
                        #Initially when previous set is empty, do a UNION with current set to assign value from current set to previous set
                        previousSet = currentSet | previousSet
                    currentSet.clear()
        return list(previousSet)

    # Search for a word in the document using regular expression and add document no. in which word was found
    def __searchForWordInDocument(self, searchText):
        self.readFile()        
        for index in range(len(self._lstContent)):
            if re.search("\\b" + searchText + "\\b", self._lstContent[index], re.IGNORECASE) != None:
                #assign multiple values i.e document no. to a key in a dictionary
                self._dictTextInDocumentNo.setdefault(searchText, []).append(index)
        return self._dictTextInDocumentNo

    # Open file and read the content and insert into a list
    def readFile(self):
        try:
            with open(self.__filePath, self.fileReadMode) as doc:
                content = doc.read().strip()
                self._lstContent = content.split("<NEW DOCUMENT>")
                # remove empty strings from the list
                #self._lstContent = filter(None, self._lstContent)

                #insert empty string at 0 index so that document number does not require index manipulation while retrieving it
                if self._lstContent[0] != "":
                    self._lstContent.insert(0,"")

        except IOError:
            print "File not found."
        return self._lstContent