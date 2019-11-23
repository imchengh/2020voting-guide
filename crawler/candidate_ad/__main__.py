import json

import numpy as np
import pandas as pd

# from db import AD, mysql_db

df = pd.read_csv("../data/manual/ad.csv")
df.columns = [
    "constituency",  # 選區
    "name",  # 參選人
    "adId",  # AD_ID
    "politicalAD",  # 登錄為政治廣告
    "startDate",  # 開始日期
    "endDate",  # 結束日期
    "content",  # 廣告內容
]

data = df[df["content"].notnull()].replace({np.nan: None}).to_dict(orient="records")
with open("../mobile/src/data/ad_static.json", "w") as fp:
    json.dump(data, fp, ensure_ascii=False)

# data = [
#     {**i, i["content"]: bytes(i["content"] or "", "utf8")} for i in df.replace({np.nan: None}).to_dict(orient="records")
# ]
# AD.drop_table()
# AD.create_table()
# mysql_db.execute_sql(
#     """ALTER TABLE
#     ad
#     CHANGE content content
#     blob
#     CHARACTER SET utf8mb4
#     COLLATE utf8mb4_unicode_ci;"""
# )
# AD.insert_many(data).execute()
