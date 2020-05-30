import statsmodels.api as sm
import pandas as pd
import datetime
def date_to_int(date):
    return (date-datetime.datetime(2020,1,21)).days
###################研究湖北省内#########################
'''
hubei=pd.read_excel("DATA\\湖北data.xlsx")
print(hubei)
hubei=hubei.drop(["地区"],axis=1)
hubei_norm = (hubei - hubei.mean()) / (hubei.max() - hubei.min())
x1 = hubei_norm[["population","distance_from_WUHAN","GDP"]]
y1 = hubei_norm['infected']
X = sm.add_constant(x1)
model2 = sm.OLS(y1,X).fit()
print(model2.summary())
corr=hubei_norm.corr()
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(corr,cmap="Blues",square=True,annot=True)
plt.savefig("corr_wuhan")
##################研究中国所有省，疾病峰值############################
'''
merge=pd.read_excel("DATA\\merge_tot.xlsx")
print(merge.columns)
province_tot=merge.groupby("province")["新增确诊"].agg(sum)
province=list(province_tot.index)
tot_ill=list(province_tot.values)
province_tot_df=pd.DataFrame({"province":province,"tot_ill":tot_ill})
ill_sum=0
peak=[]
first=True
for i in range(len(merge)-1):
    if(merge.iat[i,2]==merge.iat[i+1,2]):  #一个省
        ill_sum+=merge.iat[i,5]
        pr=merge.iat[i,2]
        if(ill_sum>=province_tot[pr]*0.6):
            if(not first): continue
            first=False
            print("peak",merge.iat[i,1],merge.iat[i,2])
            peak.append(date_to_int(merge.iat[i,1]))
            continue
    else:
        first=True
        print(merge.iat[i,2],ill_sum)
        ill_sum=0
province_tot_df["peak"]=peak
print(province_tot_df)

population=pd.read_excel("DATA\\各省人口密度.xlsx")
GDP=pd.read_excel("DATA\\各省GDP.xlsx")
merge_=pd.merge(province_tot_df,population,on="province")
merge__=pd.merge(merge_,GDP,on="province")
merge__.drop(["province"],axis=1,inplace=True)
merge__.columns=["Infected","Time to reach peak","Population density","Distance from Wuhan","GDP"]
print(merge__)
merge_norm=(merge__-merge__.mean())/(merge__.max() - merge__.min())
import seaborn as sns
import matplotlib.pyplot as plt
corr=merge__.corr()
print(corr)
plt.subplots(figsize=(10,10))
sns.heatmap(corr,cmap="Blues",annot=True,square=True)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.savefig("corr_province")




