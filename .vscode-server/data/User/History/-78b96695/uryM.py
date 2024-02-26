class Category:
    def __init__(self):
        self.date=[]

    def filter(self, Dict):
        self.date=Dict.value()
        print(self.date)
        return self.result
