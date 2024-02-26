from collections import defaultdict

class Category:
    mile = {'롯데리아', '맥도날드', '피자', '돼지', '갈비', '커피', '디저트', '스타벅스', '다방'}
    shopping = {'쇼핑몰', '쿠팡', '문구', '문방구'}
    hobby = {'랜드', '방', 'cgv', '영화관', '노래방'}
    traffic = {'택시', '버스'}

    def __init__(self):
        self.result = defaultdict(lambda: defaultdict(int))

    def filter(self, Dict):
        for date, (stores, prices) in Dict.items():
            for store, price in zip(stores, prices):
                if store in self.mile:
                    self.result[date]['mile'] += price
                elif store in self.shopping:
                    self.result[date]['shopping'] += price
                elif store in self.hobby:
                    self.result[date]['hobby'] += price
                elif store in self.traffic:
                    self.result[date]['traffic'] += price
                else:
                    self.result[date]['nothing'] += price
        print(self.result)
        return self.result