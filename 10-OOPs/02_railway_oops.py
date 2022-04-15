import pandas as pd

pd.DataFrame()      # example of class

# https://www.sololearn.com/learning/1073/2467/5126/1


class RailwayForm:
    formType = "Railway Form"       # static/class attribute

    def printData(self):
        print(f"Name is {self.name}")
        # print(f"Age is {self.age}")       # error if uncommented
        print(f"Train is {self.train}")


harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
# harrysApplication.age = 20            # error if uncommented

harrysApplication.printData()
print('Type of harry\'s application: ', harrysApplication.formType)
