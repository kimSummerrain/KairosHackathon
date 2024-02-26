from collections import defaultdict

class Category:
    # 카테고리에 속하는 단어들을 정의합니다.
    mile = {'롯데리아', '맥도날드', '피자', '돼지', '갈비', '커피', '디저트', '스타벅스', '다방'}
    shopping = {'쇼핑몰', '쿠팡', '문구', '문방구'}
    hobby = {'랜드', '방', 'cgv', '영화관', '노래방'}
    traffic = {'택시', '버스'}

    def __init__(self):
        # 결과를 저장할 defaultdict를 초기화합니다.
        self.result = defaultdict(lambda: {'mile': 0, 'shopping': 0, 'hobby': 0, 'traffic': 0, 'nothing': 0})
        self.result_dict = defaultdict(lambda: {'mile': [], 'shopping': [], 'hobby': [], 'traffic': [], 'nothing': []})

    def filter(self, Dict):
        # 주어진 데이터를 분류하고 결과를 저장합니다.
        for date, (stores, prices) in Dict.items():
            for store, price in zip(stores, prices):
                # 매장 이름에 속하는 단어가 있는지 확인하여 카테고리에 따라 분류합니다.
                if any(word in store for word in self.mile):
                    self.result[date]['mile'] += price
                    self.result_dict[date]['mile'].append(f"{store.capitalize()}: {price}")
                elif any(word in store for word in self.shopping):
                    self.result[date]['shopping'] += price
                    self.result_dict[date]['shopping'].append(f"{store.capitalize()}: {price}")
                elif any(word in store for word in self.hobby):
                    self.result[date]['hobby'] += price
                    self.result_dict[date]['hobby'].append(f"{store.capitalize()}: {price}")
                elif any(word in store for word in self.traffic):
                    self.result[date]['traffic'] += price
                    self.result_dict[date]['traffic'].append(f"{store.capitalize()}: {price}")
                else:
                    # 카테고리에 속하지 않는 경우에는 'nothing' 카테고리로 분류합니다.
                    self.result[date]['nothing'] += price
                    self.result_dict[date]['nothing'].append(f"{store.capitalize()}: {price}")

        # 결과 출력
        for date, categories in self.result.items():
            print(f"Date: {date}")
            for category, total_price in categories.items():
                print(f"{category.capitalize()}: {total_price}")
            print()

        print(self.result_dict)
        return self.result_dict