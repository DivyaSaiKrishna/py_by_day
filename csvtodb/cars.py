import pandas as pd

class CarCSVReader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
    
    def readCSV(self):
        return pd.read_csv(self.csv_path)

if __name__ == "__main__":
    cars = CarCSVReader('/Users/divyasaikrishnaavvaru/Desktop/Projects/py_by_day/csvtodb/car_data.csv')
    print(cars.readCSV())