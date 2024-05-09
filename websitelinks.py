import webbrowser
from readval import *

class weblink:
    def __init__(self) -> None:
        self.strike = 0
        self.write = fileReader()

    def printf(self):
        print("dev dextra")
        
    def linkOpen(self,link):
        print("linkOpner")

        if(link == "leet"):
            webbrowser.open("https://leetcode.com/problemset/algorithms/")
        elif(link == "chef"):
            webbrowser.open("https://www.codechef.com/practice/topics/")
        elif(link == "hack"):
            webbrowser.open("https://www.hackerrank.com/challenges/")
        elif(link == "solo"):
            webbrowser.open("https://leetcode.com/problemset/algorithms/")
        else:
            print("BAD Request")
        
        # if not self.write.readValue():
        #     self.strike += 1
        self.strike = int(self.write.readValue()) + 1
        self.write.writeValue(self.strike)
        print(self.strike)

    # def val(self):
    #     return self.strike    


