class Category:
    def __init__(self):
        self.date=[]

    def filter(self, Dict):
        self.date=Dict.key()
        print(self.date)
        return self.result
