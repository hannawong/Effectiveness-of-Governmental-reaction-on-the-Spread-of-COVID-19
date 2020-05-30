import datetime
import pandas as pd

traffic_dic={"广东":datetime.datetime(2020,2,27),"吉林":datetime.datetime(2020,2,22),"江西":datetime.datetime(2020,3,2),"四川":datetime.datetime(2020,2,25),"宁夏":datetime.datetime(2020,2,28),
             "北京":datetime.datetime(2020,3,2),"黑龙江":datetime.datetime(2020,3,13),"山东":datetime.datetime(2020,3,18),"贵州":datetime.datetime(2020,2,21),"新疆":datetime.datetime(2020,3,23),
             "天津":datetime.datetime(2020,2,24),"上海":datetime.datetime(2020,2,25),"河南":datetime.datetime(2020,3,7),"云南":datetime.datetime(2020,3,1),
             "山西":datetime.datetime(2020,3,24),"江苏":datetime.datetime(2020,2,21),"湖北":datetime.datetime(2020,3,28),"西藏":datetime.datetime(2020,2,24),
             "内蒙古":datetime.datetime(2020,2,21),"浙江":datetime.datetime(2020,3,8),"湖南":datetime.datetime(2020,2,22),"陕西":datetime.datetime(2020,2,29),
             "辽宁":datetime.datetime(2020,2,25),"安徽":datetime.datetime(2020,2,25),"广西":datetime.datetime(2020,2,21),"甘肃":datetime.datetime(2020,2,27),
             "福建":datetime.datetime(2020,2,28),"海南":datetime.datetime(2020,3,3),"青海":datetime.datetime(2020,2,26)
             }
df=pd.read_excel("DATA\\各省数据totalby0504.xlsx")
merge_tot=df[df["省份"].isin(traffic_dic.keys())][["日期","省份","新增确诊"]]
print(merge_tot)
day=datetime.timedelta(days=4)
day_14=datetime.timedelta(days=14)
startdate=datetime.datetime(2020,1,23)
traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]+day_14
    if(startdate<date and date<opendate):
        traffic.append(0)
    else:
        traffic.append(1)
merge_tot["traffic"]=traffic
#======after 1
traffic1_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]-day+day_14
    if(startdate<date and date<opendate):
        traffic1_.append(0)
    else:
        traffic1_.append(1)
merge_tot["traffic1_"]=traffic1_
#=======after 2
traffic2_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]-day-day+day_14
    if(startdate<date and date<opendate):
        traffic2_.append(0)
    else:
        traffic2_.append(1)
merge_tot["traffic2_"]=traffic2_
#----------after3
traffic3_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]-day-day-day+day_14
    if(startdate<date and date<opendate):
        traffic3_.append(0)
    else:
        traffic3_.append(1)
merge_tot["traffic3_"]=traffic3_
#----after4
traffic4_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]-day-day-day-day+day_14
    if(startdate<date and date<opendate):
        traffic4_.append(0)
    else:
        traffic4_.append(1)
merge_tot["traffic4_"]=traffic4_
#=====after 5
traffic5_=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]-day-day-day-day-day+day_14
    if(startdate<date and date<opendate):
        traffic5_.append(0)
    else:
        traffic5_.append(1)
merge_tot["traffic5_"]=traffic5_
#======before 1
_1traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]+day+day_14
    if(startdate<date and date<opendate):
        _1traffic.append(0)
    else:
        _1traffic.append(1)
merge_tot["_1traffic"]=_1traffic
#==========before 2
_2traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]+day+day+day_14
    if(startdate<date and date<opendate):
        _2traffic.append(0)
    else:
        _2traffic.append(1)
merge_tot["_2traffic"]=_2traffic
###=====before 3
_3traffic=[]
for i in range(len(merge_tot)):
    province=merge_tot.iat[i,1]
    date=merge_tot.iat[i,0]
    opendate=traffic_dic[province]+day+day+day+day_14
    if(startdate<date and date<opendate):
        _3traffic.append(0)
    else:
        _3traffic.append(1)
merge_tot["_3traffic"]=_3traffic
import numpy as np
def log(x):
    if(x!=0): return np.log(x)
    else: return 0
merge_tot["新增确诊"]=merge_tot["新增确诊"].map(lambda x:log(x))
merge_tot=merge_tot.sort_values(by=["日期","省份"])
merge_tot=merge_tot.set_index(["省份","日期"])
merge_norm = (merge_tot - merge_tot.mean()) / (merge_tot.max() - merge_tot.min())
print(merge_norm)
from linearmodels import PanelOLS
y=merge_norm[["新增确诊"]]
x=merge_norm[["_1traffic","_2traffic","_3traffic","traffic","traffic3_","traffic2_","traffic1_",]]  #change here
reg=PanelOLS(y, x, entity_effects=True,time_effects=True)
res=reg.fit(cov_type='clustered', cluster_entity=True)
print(res)
parameters=[0.0343,0.017,0.0301,0.0313,0.0146,0.016,0.017]
xline=[-3,-2,-1,0,1,2,3]
lower=[-0.0433,-0.0144,-0.0102,0.0313,-0.0093,-0.0062,-0.0102]
upper=[0.1119,0.0484,0.0704,0.0313,0.0384,0.0382,0.0441]
for i in range(len(parameters)):
    parameters[i]/=0.0301
    lower[i]/=0.0301
    upper[i]/=0.0301
import matplotlib.pyplot as plt
plt.plot(xline,parameters,marker="*",color="black")
for i in range(len(xline)):
    plt.vlines(x=xline[i],ymin=lower[i],ymax=upper[i],label="*")
plt.vlines(x=0,ymin=-1,ymax=3.0,linestyles="dashed")
plt.hlines(y=1,xmin=-3,xmax=3,linestyles="dashed")
plt.show()