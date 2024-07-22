# Final Project IT412
# Entry Class Module

class Entry():
    """Class used to clean up text file"""

    def __init__(self, header, raw_data):
        """Method used to initialize the data"""
        self.data = {}
        for label,value in zip(header, raw_data):
            self.data[label.replace("#", "")] = value.replace("#", "")
        self.data.popitem()

    def getascsv(self):
        """Method used to grab the values for CSV"""
        return",".join(self.data.values())

    def get_headerascsv(self):
        """Method used to grab the header for CSV"""
        return",".join(self.data.keys())