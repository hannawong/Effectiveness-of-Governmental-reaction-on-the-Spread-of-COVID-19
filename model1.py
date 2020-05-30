import pandas as pd
import numpy as np
import datetime
def log(x):
    if(x!=0): return np.log(x)
    else: return 0
def date_to_int(date):
    return (date-datetime.datetime(2020,1,21)).days
traffic_dic={"广东":datetime.datetime(2020,3,10),"吉林":datetime.datetime(2020,3,12),"江西":datetime.datetime(2020,3,18),"四川":datetime.datetime(2020,3,16),"宁夏":datetime.datetime(2020,3,15),
             "北京":datetime.datetime(2020,3,10),"黑龙江":datetime.datetime(2020,3,13),"山东":datetime.datetime(2020,3,15),"贵州":datetime.datetime(2020,3,10),"新疆":datetime.datetime(2020,3,15),
             "天津":datetime.datetime(2020,3,24),"上海":datetime.datetime(2020,3,9),"河南":datetime.datetime(2020,3,25),"云南":datetime.datetime(2020,3,12),
             "山西":datetime.datetime(2020,3,13),"江苏":datetime.datetime(2020,3,18),"湖北":datetime.datetime(2020,3,25),"西藏":datetime.datetime(2020,3,11),
             "内蒙古":datetime.datetime(2020,3,11),"浙江":datetime.datetime(2020,3,19),"湖南":datetime.datetime(2020,3,7),"陕西":datetime.datetime(2020,3,17),
             "辽宁":datetime.datetime(2020,3,13),"安徽":datetime.datetime(2020,3,24),"广西":datetime.datetime(2020,3,16),"甘肃":datetime.datetime(2020,3,16),
             "福建":datetime.datetime(2020,3,18),"海南":datetime.datetime(2020,3,24),"青海":datetime.datetime(2020,3,16)
             }
merge_tot=pd.read_excel("DATA\\merge_tot.xlsx")
print(merge_tot.columns)
traffic1_=[]
day=datetime.timedelta(days=2)
#===========================================traffic 平移=========================================
#======after 1
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]-day
    if(date<opendate):
        traffic1_.append(0)
    else:
        traffic1_.append(1)
merge_tot["traffic1_"]=traffic1_
#=======after 2
traffic2_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]-day-day
    if(date<opendate):
        traffic2_.append(0)
    else:
        traffic2_.append(1)
merge_tot["traffic2_"]=traffic2_
#----------after3
traffic3_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]-day-day-day
    if(date<opendate):
        traffic3_.append(0)
    else:
        traffic3_.append(1)
merge_tot["traffic3_"]=traffic3_
#----after4
traffic4_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]-day-day-day-day
    if(date<opendate):
        traffic4_.append(0)
    else:
        traffic4_.append(1)
merge_tot["traffic4_"]=traffic4_
#=====after 5
traffic5_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]-day-day-day-day-day
    if(date<opendate):
        traffic5_.append(0)
    else:
        traffic5_.append(1)
merge_tot["traffic5_"]=traffic5_
#======before 1
_1traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]+day
    if(date<opendate):
        _1traffic.append(0)
    else:
        _1traffic.append(1)
merge_tot["_1traffic"]=_1traffic
#==========before 2
_2traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]+day+day
    if(date<opendate):
        _2traffic.append(0)
    else:
        _2traffic.append(1)
merge_tot["_2traffic"]=_2traffic
###=====before 3
_3traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]+day+day+day
    if(date<opendate):
        _3traffic.append(0)
    else:
        _3traffic.append(1)
merge_tot["_3traffic"]=_3traffic
#======
traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,2]
    date=merge_tot.iat[i,1]
    opendate=traffic_dic[province]
    if(date<opendate):
        traffic.append(0)
    else:
        traffic.append(1)
merge_tot["traffic"]=traffic
###填缺失值######
merge_tot["AQI"]=merge_tot.groupby("province")["AQI"].transform(lambda x:x.fillna(x.mode()[0]))
merge_tot.drop(["Unnamed: 0","weather"],axis=1,inplace=True)
merge_tot["新增确诊"]=merge_tot["新增确诊"].map(lambda x:log(x))
merge_tot=merge_tot.sort_values(by=["date","province"])
merge_tot=merge_tot.set_index(["province","date"])
merge_norm = (merge_tot - merge_tot.mean()) / (merge_tot.max() - merge_tot.min())
print(merge_norm)
from linearmodels import PanelOLS
y=merge_norm[["新增确诊"]]
x=merge_norm[["max_temp","是否复工","traffic1_","traffic2_","traffic3_","traffic","_1traffic","_2traffic","_3traffic"]]  #change here
reg=PanelOLS(y, x, entity_effects=True,time_effects=True)
res=reg.fit(cov_type='clustered', cluster_entity=True)
print(res)

