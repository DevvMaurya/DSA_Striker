#This file do only read and write opeation..!
class fileReader():
    def __init__(self) -> None:
        self.val =0

    def readValue(self):
        with open("strikeVal.txt","r") as file:
            self.val = file.read()

            if self.val == " ":
                self.val = 0

        return self.val
    
    def writeValue(self,data):
        with open("strikeVal.txt","w") as file:
            file.write(str(data))



        
