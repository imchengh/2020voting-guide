"""
Source: https://github.com/g0v-money-flow/g0v-money-flow.github.io/tree/master/page-data
"""
import glob
import json
import os

# 這是這次候選人的姓名清單
target_list = [
    {"name": "伊斯坦大．貝雅夫．正福"},
    {"name": "伍麗華"},
    {"name": "何志偉"},
    {"name": "何景榮"},
    {"name": "何欣純"},
    {"name": "余天"},
    {"name": "余筱菁"},
    {"name": "傅大偉"},
    {"name": "傅家賢"},
    {"name": "傅崐萁"},
    {"name": "凌子楚"},
    {"name": "劉世芳"},
    {"name": "劉國隆"},
    {"name": "劉建國"},
    {"name": "劉櫂豪"},
    {"name": "吳佩蓉"},
    {"name": "吳光中"},
    {"name": "吳志揚"},
    {"name": "吳思瑤"},
    {"name": "吳怡農"},
    {"name": "吳成典"},
    {"name": "吳文凱"},
    {"name": "吳旭智"},
    {"name": "吳木"},
    {"name": "吳琪銘"},
    {"name": "吳秉叡"},
    {"name": "吳達偉"},
    {"name": "呂國華"},
    {"name": "呂孫綾"},
    {"name": "呂應宏"},
    {"name": "呂玉玲"},
    {"name": "周佳琪"},
    {"name": "周凱崙"},
    {"name": "周武榮"},
    {"name": "周江杰"},
    {"name": "孔文吉"},
    {"name": "孫博萮"},
    {"name": "孫大千"},
    {"name": "孫繼正"},
    {"name": "宋瑋莉"},
    {"name": "廖國棟"},
    {"name": "廖蓓瑩"},
    {"name": "張余健"},
    {"name": "張嘉郡"},
    {"name": "張國樑"},
    {"name": "張宏陸"},
    {"name": "張幸松"},
    {"name": "張廖萬堅"},
    {"name": "張志明"},
    {"name": "張永津"},
    {"name": "張渝江"},
    {"name": "張瀚天"},
    {"name": "張睿倉"},
    {"name": "張穆庭"},
    {"name": "張耿輝"},
    {"name": "張衞航"},
    {"name": "張誠"},
    {"name": "張銘祐"},
    {"name": "彭俊豪"},
    {"name": "彭新銘"},
    {"name": "徐定禎"},
    {"name": "徐志榮"},
    {"name": "徐慶煌"},
    {"name": "徐立信"},
    {"name": "敖博勝"},
    {"name": "曾楷耀"},
    {"name": "朱哲成"},
    {"name": "朱智德"},
    {"name": "朱立凡"},
    {"name": "朱英濠"},
    {"name": "李中"},
    {"name": "李伯利"},
    {"name": "李佳玲"},
    {"name": "李俊德"},
    {"name": "李克焜"},
    {"name": "李問"},
    {"name": "李國憲"},
    {"name": "李婉鈺"},
    {"name": "李建輝"},
    {"name": "李彥秀"},
    {"name": "李應文"},
    {"name": "李旻蔚"},
    {"name": "李昆澤"},
    {"name": "李晉豪"},
    {"name": "李武龍"},
    {"name": "李永萍"},
    {"name": "李玉蕙"},
    {"name": "李縉穎"},
    {"name": "李翁月娥"},
    {"name": "李鎔任"},
    {"name": "李雅靜"},
    {"name": "林佳新"},
    {"name": "林佳瑋"},
    {"name": "林俊憲"},
    {"name": "林信義"},
    {"name": "林國慶"},
    {"name": "林國政"},
    {"name": "林國春"},
    {"name": "林培基"},
    {"name": "林奕華"},
    {"name": "林宜瑾"},
    {"name": "林岱樺"},
    {"name": "林德福"},
    {"name": "林志文"},
    {"name": "林思銘"},
    {"name": "林明正"},
    {"name": "林昶佐"},
    {"name": "林泰龍"},
    {"name": "林淑娟"},
    {"name": "林淑芬"},
    {"name": "林為洲"},
    {"name": "林燕祝"},
    {"name": "林碩彥"},
    {"name": "林秋屏"},
    {"name": "林郁方"},
    {"name": "林金結"},
    {"name": "林金連"},
    {"name": "柯呈枋"},
    {"name": "柯富國"},
    {"name": "柯志恩"},
    {"name": "梁雅羿"},
    {"name": "楊智淵"},
    {"name": "楊曜"},
    {"name": "楊書銘"},
    {"name": "楊瓊瓔"},
    {"name": "楊石城"},
    {"name": "楊詩龍"},
    {"name": "楊進福"},
    {"name": "歐中慨"},
    {"name": "歐崇敬"},
    {"name": "段體佩"},
    {"name": "江啟臣"},
    {"name": "江永昌"},
    {"name": "池國樑"},
    {"name": "汪志冰"},
    {"name": "沈宜璇"},
    {"name": "沈智慧"},
    {"name": "洪偉富"},
    {"name": "洪和成"},
    {"name": "洪孟楷"},
    {"name": "洪宗熠"},
    {"name": "洪志恒"},
    {"name": "洪恆珠"},
    {"name": "洪慈庸"},
    {"name": "洪正"},
    {"name": "洪正一"},
    {"name": "洪秀柱"},
    {"name": "温俊勇"},
    {"name": "潘偉龍"},
    {"name": "潘政治"},
    {"name": "王全中"},
    {"name": "王向榮"},
    {"name": "王啟澧"},
    {"name": "王定宇"},
    {"name": "王斯儀"},
    {"name": "王炳忠"},
    {"name": "王章記"},
    {"name": "王美惠"},
    {"name": "王郁揚"},
    {"name": "王金山"},
    {"name": "王長明"},
    {"name": "王齡嬌"},
    {"name": "盧月香"},
    {"name": "石人仁"},
    {"name": "秦詩雁"},
    {"name": "章正輝"},
    {"name": "童小芸"},
    {"name": "簡明廉"},
    {"name": "羅和讚"},
    {"name": "羅明才"},
    {"name": "羅致政"},
    {"name": "羅貴星"},
    {"name": "羅鼎城"},
    {"name": "翁美春"},
    {"name": "苗豐隆"},
    {"name": "范雲"},
    {"name": "莊子富"},
    {"name": "莊瑞雄"},
    {"name": "莊競程"},
    {"name": "莊貽量"},
    {"name": "萬美玲"},
    {"name": "葉壽山"},
    {"name": "蔡其昌"},
    {"name": "蔡培慧"},
    {"name": "蔡宗穎"},
    {"name": "蔡宜芳"},
    {"name": "蔡承攸"},
    {"name": "蔡明峰"},
    {"name": "蔡易餘"},
    {"name": "蔡永泉"},
    {"name": "蔡沐霖"},
    {"name": "蔡淑惠"},
    {"name": "蔡育輝"},
    {"name": "蔡適應"},
    {"name": "蔣月惠"},
    {"name": "蔣絜安"},
    {"name": "蔣萬安"},
    {"name": "蕭亞譚"},
    {"name": "蕭景田"},
    {"name": "蕭美琴"},
    {"name": "蕭赫麟"},
    {"name": "蘇博廷"},
    {"name": "蘇巧慧"},
    {"name": "蘇志仁"},
    {"name": "蘇恆"},
    {"name": "蘇治芬"},
    {"name": "許智傑"},
    {"name": "許淑華"},
    {"name": "許淑華"},
    {"name": "許能通"},
    {"name": "謝佩芬"},
    {"name": "謝文卿"},
    {"name": "謝淑亞"},
    {"name": "謝衣鳳"},
    {"name": "費鴻泰"},
    {"name": "賀樺"},
    {"name": "賴品妤"},
    {"name": "賴嘉倫"},
    {"name": "賴士葆"},
    {"name": "賴建豪"},
    {"name": "賴惠員"},
    {"name": "賴瑞隆"},
    {"name": "趙天麟"},
    {"name": "趙正宇"},
    {"name": "邱志偉"},
    {"name": "邱烽堯"},
    {"name": "邱議瑩"},
    {"name": "邱靖雅"},
    {"name": "郭國文"},
    {"name": "郭大衛"},
    {"name": "郭新政"},
    {"name": "郭瑞豐"},
    {"name": "鄭品娟"},
    {"name": "鄭天財"},
    {"name": "鄭宏輝"},
    {"name": "鄭寶清"},
    {"name": "鄭文龍"},
    {"name": "鄭朝方"},
    {"name": "鄭正鈐"},
    {"name": "鄭運鵬"},
    {"name": "錢一凡"},
    {"name": "鍾佳濱"},
    {"name": "阮昭雄"},
    {"name": "陳亭妃"},
    {"name": "陳俊憲"},
    {"name": "陳俊龍"},
    {"name": "陳允萍"},
    {"name": "陳冠宇"},
    {"name": "陳大松"},
    {"name": "陳學聖"},
    {"name": "陳峻涵"},
    {"name": "陳志傑"},
    {"name": "陳志成"},
    {"name": "陳怡潔"},
    {"name": "陳惠敏"},
    {"name": "陳愷寧"},
    {"name": "陳明文"},
    {"name": "陳明義"},
    {"name": "陳昭宏"},
    {"name": "陳杰"},
    {"name": "陳柏惟"},
    {"name": "陳根德"},
    {"name": "陳歐珀"},
    {"name": "陳泓維"},
    {"name": "陳玉珍"},
    {"name": "陳瑩"},
    {"name": "陳癸佑"},
    {"name": "陳秀寳"},
    {"name": "陳素月"},
    {"name": "陳美雅"},
    {"name": "陳致曉"},
    {"name": "陳超明"},
    {"name": "陳雪生"},
    {"name": "陳麗娜"},
    {"name": "顏寬恒"},
    {"name": "顏耀星"},
    {"name": "顏銘緯"},
    {"name": "馬文君"},
    {"name": "高嘉瑜"},
    {"name": "高李孟萍"},
    {"name": "高潞·以用·巴魕剌"},
    {"name": "高金素梅"},
    {"name": "高鈺婷"},
    {"name": "魯明哲"},
    {"name": "黃世杰"},
    {"name": "黃仁"},
    {"name": "黃兆呈"},
    {"name": "黃啟嘉"},
    {"name": "黃國書"},
    {"name": "黃國華"},
    {"name": "黃天辰"},
    {"name": "黃宏成台灣阿成世界偉人財神總統"},
    {"name": "黃定和"},
    {"name": "黃志雄"},
    {"name": "黃昭順"},
    {"name": "黃朝淵"},
    {"name": "黃柏霖"},
    {"name": "黃桂蘭"},
    {"name": "黃玉芬"},
    {"name": "黃秀芳"},
    {"name": "黃綉晶"},
    {"name": "黃足貞"},
    {"name": "黃韻涵"},
    {"name": "黃馨慧"},
]
target_list = [candidate["name"] for candidate in target_list]


store_folder = "./2016_payment"
os.makedirs(store_folder, exist_ok=True)

for page in glob.glob("./candidates/*/*"):
    with open(page) as fp:
        page_data = json.load(fp)
    name = page_data["result"]["pageContext"]["candidate"]["name"]
    prev_path = page_data["result"]["pageContext"]["prevPath"]
    if name in target_list and prev_path.startswith("elections/2016-legislator-election"):
        print(name, page)
        with open(f"{store_folder}/{name}.json", "w") as fp:
            json.dump(page_data["result"]["pageContext"], fp, ensure_ascii=False)
