class Category:
    #음식, 쇼핑, 취미 ,교통 기타
    mile={'롯데리아','맥도날드','피자','돼지','갈비','커피','디저트','스타벅스','다방'}
    shopping={'쇼핑몰','쿠팡','문구','문방구'}
    hobby={'랜드','방','cgv','영화관','노래방'}
    traffic={'택시','버스'}

    def __init__(self):
        self.date=[]

    def filter(self, Dict):
        self.date=list(Dict.keys())
        print(self.date[3])
        print(Dict(self.date[3]))
       # return self.result
