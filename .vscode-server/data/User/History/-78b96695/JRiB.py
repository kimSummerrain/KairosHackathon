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
                if any(word in store for word in self.mile):
                    self.result[date]['mile'] += price
                elif any(word in store for word in self.shopping):
                    self.result[date]['shopping'] += price
                elif any(word in store for word in self.hobby):
                    self.result[date]['hobby'] += price
                elif any(word in store for word in self.traffic):
                    self.result[date]['traffic'] += price
                else:
                    self.result[date]['nothing'] += price
        return self.result
        
        # 결과 출력
        for date, categories in self.result.items():
            print(f"Date: {date}")
            for category, total_price in categories.items():
                print(f"{category.capitalize()}: {total_price}")
            print()