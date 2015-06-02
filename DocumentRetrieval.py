from DocumentSearch import DocumentSearch
from enums import enums

def displayOption():
    print("""What would you like to do?
            1. Search for documents
            2. Read Document
            3. Quit Program\n""")
    try:
        userOption = int(raw_input("Please select you option: "))

        if userOption == enums._DisplayOption._Search:
            searchText = raw_input("Enter search words: ")
            searchForWord(searchText)
            displayOption()

        elif userOption == enums._DisplayOption._Read:            
            lstDocuments = getDocument()
            if lstDocuments:
                print "\nDocument number: 1 - {0}".format(len(lstDocuments))
                documentNumber = int(raw_input("\nEnter document number: "))
                try:
                    if documentNumber <= 0 or documentNumber > len(lstDocuments):
                        raise IndexError 

                    print("""\nDocument #{0}
    ---------------------------\n{1}\n
    ---------------------------\n""".format(documentNumber
                                    , lstDocuments[documentNumber - 1]))
                except IndexError:                
                    print "\nDocument number does not exists.\n"
                finally:
                    displayOption()

        elif userOption == enums._DisplayOption._Quit:
            try:
                exit()
            except SystemExit:
                pass

    except ValueError:
        print "Please select the correct option.\n"
        displayOption()

def getDocument():
    return DocumentSearch().readFile()

def searchForWord(searchText):
    lstSearchText = searchText.split(" ")
    lstTextInDocument = DocumentSearch().search(lstSearchText)
    lstTextInDocument.insert(0, "")
    print("Documents fitting search: {0}\n".format(lstTextInDocument))

def main():
    displayOption()

main()