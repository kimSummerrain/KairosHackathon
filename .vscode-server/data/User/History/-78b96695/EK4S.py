class Category:
    mile = {'롯데리아', '맥도날드', '피자', '돼지', '갈비', '커피', '디저트', '스타벅스', '다방'}
    shopping = {'쇼핑몰', '쿠팡', '문구', '문방구'}
    hobby = {'랜드', '방', 'cgv', '영화관', '노래방'}
    traffic = {'택시', '버스'}

    def __init__(self):
        self.date = []
        self.result = {'mile': [], 'shopping': [], 'hobby': [], 'traffic': [], 'nothing': []}

    def filter(self, Dict):
        self.date = list(Dict.keys())
        for i in self.date:
            for j in range(len(Dict[i][0])):
                store = Dict[i][0][j]
                if store in self.mile:
                    self.result['mile'].append(store)
                elif store in self.shopping:
                    self.result['shopping'].append(store)
                elif store in self.hobby:
                    self.result['hobby'].append(store)
                elif store in self.traffic:
                    self.result['traffic'].append(store)
                else:
                    self.result['nothing'].append(store)
        print(self.result)
        return self.result
        # return self.result
