import datetime
import numpy as np
begintime=datetime.datetime(2019,12,20)
N=14000000
S=N*0.9
C=0
E=0
D=0
I=5
R=0
kappa=0
sigma=1/3
gamma=1/5
d=0.2
lambdaa=1/11.2
def F(i):
    if(i<datetime.datetime(2020,1,1)):
        return 10
    else: return 0
def alpha(i):
    '''
    if(i<datetime.datetime(2020,1,23)):
        return 0
    if(datetime.datetime(2020,1,23)<i and i<datetime.datetime(2020,1,29)):
        return 0.4249
    else:
        return 0.9478
    '''
    return 0
def mu(i):
    if(i<datetime.datetime(2020,1,23)):
        return 0.0205
    else:
        return 0
delta=datetime.timedelta(days=1)
def beta(i):
    if (i < datetime.datetime(2020, 1, 23)):
        return  0.5944  #1.68
    else:
        return 0.56
def beta_t(beta,alpha,D,kappa):
    return beta*(1-alpha)*np.power((1-D/N),kappa)
daily_new=[]
datelist=[]
infected=[]
for i in range(155):
    date=begintime+delta*i
    datelist.append(date)
    print(date)
    deltaS=-((beta_t(beta(date),alpha(date),D,kappa))*S*I/N+mu(date)*S+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N)
    deltaE=beta_t(beta(date),alpha(date),D,kappa)*S*I/N-(sigma+mu(date))*E+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N
    deltaI=sigma*E-(gamma+mu(date))*I
    deltaR=gamma*I-mu(date)*R
    deltaN=-mu(date)*N
    deltaD=d*gamma*I-lambdaa*D
    deltaC=sigma*E
    S+=deltaS
    E+=deltaE
    I+=deltaI
    R+=deltaR
    N+=deltaN
    D+=deltaD
    C+=deltaC
    print("I",I,"E",E,"S",S,"daily new",deltaI)
    daily_new.append(deltaI)
    infected.append(I)

import matplotlib.pyplot as plt
plt.plot(datelist,infected,color="green",alpha=0.5,linestyle="--")

import pandas as pd
df=pd.read_excel("DATA\\各省数据totalby0504.xlsx")
df=df[df["省份"]=="湖北"]
df["现有确诊"]=df["现有确诊"].map(lambda x:0.8*x)
print(df)
plt.plot(df["日期"],df["现有确诊"],marker=".",color="grey",alpha=0.7)
plt.yscale("log")
####################close down school###########################

N=14000000
S=N*0.9
C=0
E=0
D=0
I=5
R=0
kappa=0
sigma=1/3
gamma=1/5
d=0.2
lambdaa=1/11.2
daily_new=[]
datelist=[]
infected=[]
def beta(i):
    if (i < datetime.datetime(2020, 2,5)):
        return  0.5944  #1.68
    else:
        return 0.56*0.5
for i in range(155):
    date=begintime+delta*i
    datelist.append(date)
    print(date)
    deltaS=-((beta_t(beta(date),alpha(date),D,kappa))*S*I/N+mu(date)*S+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N)
    deltaE=beta_t(beta(date),alpha(date),D,kappa)*S*I/N-(sigma+mu(date))*E+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N
    deltaI=sigma*E-(gamma+mu(date))*I
    deltaR=gamma*I-mu(date)*R
    deltaN=-mu(date)*N
    deltaD=d*gamma*I-lambdaa*D
    deltaC=sigma*E
    S+=deltaS
    E+=deltaE
    I+=deltaI
    R+=deltaR
    N+=deltaN
    D+=deltaD
    C+=deltaC
    print("I",I,"E",E,"S",S,"daily new",deltaI)
    daily_new.append(deltaI)
    infected.append(I)

import matplotlib.pyplot as plt
plt.plot(datelist,infected,color="red",alpha=0.5,linestyle="--")
###################====kappa=110==========================
N=14000000
S=N*0.9
C=0
E=0
D=0
I=5
R=0
kappa=110
sigma=1/3
gamma=1/5
d=0.2
lambdaa=1/11.2
datelist=[]
daily_new=[]
infected=[]
for i in range(155):
    date=begintime+delta*i
    datelist.append(date)
    print(date)
    deltaS=-((beta_t(beta(date),alpha(date),D,kappa))*S*I/N+mu(date)*S+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N)
    deltaE=beta_t(beta(date),alpha(date),D,kappa)*S*I/N-(sigma+mu(date))*E+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N
    deltaI=sigma*E-(gamma+mu(date))*I
    deltaR=gamma*I-mu(date)*R
    deltaN=-mu(date)*N
    deltaD=d*gamma*I-lambdaa*D
    deltaC=sigma*E
    S+=deltaS
    E+=deltaE
    I+=deltaI
    R+=deltaR
    N+=deltaN
    D+=deltaD
    C+=deltaC
    print("I",I,"E",E,"S",S,"daily new",deltaI)
    daily_new.append(deltaI)
    infected.append(I)
plt.plot(datelist,infected,color="CornFlowerBlue",alpha=0.5,linestyle="--")
#=======================with government========================
N=14000000
S=N*0.9
C=0
E=0
D=0
I=5
R=0
kappa=110
sigma=1/3
gamma=1/5
d=0.2
lambdaa=1/11.2
datelist=[]
daily_new=[]
infected=[]
def alpha(i):
    if(i<datetime.datetime(2020,2,7)):
        return 0
    if(datetime.datetime(2020,2,7)<i and i<datetime.datetime(2020,2,19)):  #1.23-2.1
        return 0.4249
    if(datetime.datetime(2020,2,19)<i and i<datetime.datetime(2020,4,8)):
        return 0.8
    else: return 0.8
for i in range(155):
    date=begintime+delta*i
    datelist.append(date)
    print(date)
    deltaS=-((beta_t(beta(date),alpha(date),D,kappa))*S*I/N+mu(date)*S+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N)
    deltaE=beta_t(beta(date),alpha(date),D,kappa)*S*I/N-(sigma+mu(date))*E+F(date)*S*beta_t(beta(date),alpha(date),D,kappa)/N
    deltaI=sigma*E-(gamma+mu(date))*I
    deltaR=gamma*I-mu(date)*R
    deltaN=-mu(date)*N
    deltaD=d*gamma*I-lambdaa*D
    deltaC=sigma*E
    S+=deltaS
    E+=deltaE
    I+=deltaI
    R+=deltaR
    N+=deltaN
    D+=deltaD
    C+=deltaC
    print("I",I,"E",E,"S",S,"daily new",deltaI)
    daily_new.append(deltaI)
    infected.append(I)
plt.plot(datelist,infected,color="orange",alpha=0.5,linestyle="-.")
plt.legend(["naive","reported","close down schools only","individual react","individual react+governmental react"])
plt.xlabel("Date")
plt.ylabel("Infected Population")
plt.savefig("schooleffect")
