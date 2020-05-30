import datetime
beta1=0.3917
beta2=0.6661
eta1=0.1
eta2=0.05
N1=10000000
N2=5*N1
d=1
a=4
gamma1=0.0509
lambdaa1=0.0018
gamma2=0.116
lambdaa2=0.0006
S1=0.9*N1  #易感者
S2=0.9*N2
I1=1  #感染
I2=1
E1=0  #暴露
E2=0
R1=0  #康复
R2=0
D1=0  #死者
D2=0
suscept1=[]
infected1=[]
expose1=[]
recover1=[]
dead1=[]
suscept2=[]
infected2=[]
expose2=[]
recover2=[]
dead2=[]
datelist=[]
alpha=0.14
begintime=datetime.datetime(2019,1,1)
day1=datetime.timedelta(days=1)
for i in range(155):
    date=begintime+day1*i
    datelist.append(date)
    deltaS1=-beta1/N1*((1-eta1)*I1+eta2*I2+(1-eta1)*E1+eta2*E2)*((1-eta1)*S1+eta2*S2)
    deltaE1=beta1/N1*((1-eta1)*I1+eta2*I2+(1-eta1)*E1+eta2*E2)*((1-eta1)*S1+eta2*S2)-alpha*((1-eta1)*E1+eta2*E2)
    deltaI1=alpha*((1-eta1)*E1+eta2*E2)-(lambdaa1+gamma1)*((1-eta1)*I1+eta2*I2)
    deltaR1=gamma1*((1-eta1)*I1+eta2*I2)
    deltaD1=lambdaa1*((1-eta1)*I1+eta2*I2)
    deltaS2 = -beta2 / N2 * ((1 - eta2) * I2 + eta1 * I1 + (1 - eta2) * E2 + eta1 * E1) * ((1 - eta2) * S2 + eta1 * S1)
    deltaE2 = beta2 / N2 * ((1 - eta2) * I2 + eta1 * I1 + (1 - eta2) * E2 + eta1 * E1) * (
                (1 - eta2) * S2 + eta1 * S1) - alpha * ((1 - eta2) * E2 + eta1 * E1)
    deltaI2 = alpha * ((1 - eta2) * E2 + eta1 * E1) - (lambdaa2 + gamma2) * ((1 - eta2) * I2 + eta1 * I1)
    deltaR2 = gamma2 * ((1 - eta2) * I2 + eta1 * I1)
    deltaD2 = lambdaa2 * ((1 - eta2) * I2 + eta1 * I1)
    S1+=deltaS1
    E1+=deltaE1
    I1+=deltaI1
    R1+=deltaR1
    D1+=deltaD1
    S2+=deltaS2
    E2+=deltaE2
    I2+=deltaI2
    R2+=deltaR2
    D2+=deltaD2
    suscept1.append(S1)
    suscept2.append(S2)
    expose1.append(E1)
    expose2.append(E2)
    infected1.append(I1)
    infected2.append(I2)
    dead1.append(D1)
    dead2.append(D2)
    recover1.append(R1)
    recover2.append(R2)

    print(date,I1)
import matplotlib.pyplot as plt
plt.subplots(figsize=(14,6))
plt.subplot(121)
plt.plot(datelist,infected1,color="darkred",alpha=0.5)
plt.plot(datelist,recover1,color="green",alpha=0.5,linestyle="--")
plt.plot(datelist,dead1,color="grey",alpha=0.7)
plt.plot(datelist,expose1,color="purple",alpha=0.5)
plt.plot(datelist,suscept1,color="orange",alpha=0.5)
plt.title("Trend of City 1 (without lockdown)")
plt.ylabel("Population")
plt.legend(["infected","recovered","died","exposed","susceptible"])
plt.xlabel("Date")
plt.xticks(rotation=90)
plt.subplot(122)
plt.plot(datelist,infected2,color="darkred",alpha=0.5)
plt.plot(datelist,recover2,color="green",alpha=0.5,linestyle="--")
plt.plot(datelist,dead2,color="grey",alpha=0.7)
plt.plot(datelist,expose2,color="purple",alpha=0.5)
plt.plot(datelist,suscept2,color="orange",alpha=0.5)
plt.title("Trend of City 2 (without lockdown)")
plt.ylabel("Population")
plt.legend(["infected","recovered","died","exposed","susceptible"])
plt.xlabel("Date")
plt.xticks(rotation=90)
plt.savefig("without-lockdown")
'''
##########lockdown############
##reduce the inflow into Wuhan by 76.64%, outflow from Wuhan by 56.35%
beta1=0.3917
beta2=0.6661*(1-0.5635)
eta1=0.0
eta2=0.00
N1=10000000
N2=5*N1
d=1
a=4
gamma1=0.0509
lambdaa1=0.0018
gamma2=0.116
lambdaa2=0.0006
S1=0.9*N1  #易感者
S2=0.9*N2
I1=1  #感染
I2=1
E1=0  #暴露
E2=0
R1=0  #康复
R2=0
D1=0  #死者
D2=0
suscept1=[]
infected1=[]
expose1=[]
recover1=[]
dead1=[]
suscept2=[]
infected2=[]
expose2=[]
recover2=[]
dead2=[]
datelist=[]
alpha=0.14
begintime=datetime.datetime(2019,1,1)
day1=datetime.timedelta(days=1)
for i in range(300):
    date=begintime+day1*i
    datelist.append(date)
    deltaS1=-beta1/N1*((1-eta1)*I1+eta2*I2+(1-eta1)*E1+eta2*E2)*((1-eta1)*S1+eta2*S2)
    deltaE1=beta1/N1*((1-eta1)*I1+eta2*I2+(1-eta1)*E1+eta2*E2)*((1-eta1)*S1+eta2*S2)-alpha*((1-eta1)*E1+eta2*E2)
    deltaI1=alpha*((1-eta1)*E1+eta2*E2)-(lambdaa1+gamma1)*((1-eta1)*I1+eta2*I2)
    deltaR1=gamma1*((1-eta1)*I1+eta2*I2)
    deltaD1=lambdaa1*((1-eta1)*I1+eta2*I2)
    deltaS2 = -beta2 / N2 * ((1 - eta2) * I2 + eta1 * I1 + (1 - eta2) * E2 + eta1 * E1) * ((1 - eta2) * S2 + eta1 * S1)
    deltaE2 = beta2 / N2 * ((1 - eta2) * I2 + eta1 * I1 + (1 - eta2) * E2 + eta1 * E1) * (
                (1 - eta2) * S2 + eta1 * S1) - alpha * ((1 - eta2) * E2 + eta1 * E1)
    deltaI2 = alpha * ((1 - eta2) * E2 + eta1 * E1) - (lambdaa2 + gamma2) * ((1 - eta2) * I2 + eta1 * I1)
    deltaR2 = gamma2 * ((1 - eta2) * I2 + eta1 * I1)
    deltaD2 = lambdaa2 * ((1 - eta2) * I2 + eta1 * I1)
    S1+=deltaS1
    E1+=deltaE1
    I1+=deltaI1
    R1+=deltaR1
    D1+=deltaD1
    S2+=deltaS2
    E2+=deltaE2
    I2+=deltaI2
    R2+=deltaR2
    D2+=deltaD2
    suscept1.append(S1)
    suscept2.append(S2)
    expose1.append(E1)
    expose2.append(E2)
    infected1.append(I1)
    infected2.append(I2)
    dead1.append(D1)
    dead2.append(D2)
    recover1.append(R1)
    recover2.append(R2)

    print(date,I1)
import matplotlib.pyplot as plt
plt.subplots(figsize=(14,6))
plt.subplot(121)
plt.plot(datelist,infected1,color="darkred",alpha=0.5)
plt.plot(datelist,recover1,color="green",alpha=0.5,linestyle="--")
plt.plot(datelist,dead1,color="grey",alpha=0.7)
plt.plot(datelist,expose1,color="purple",alpha=0.5)
plt.plot(datelist,suscept1,color="orange",alpha=0.5)
plt.ylabel("Population")
plt.legend(["infected","recovered","died","exposed","susceptible"])
plt.xlabel("Date")
plt.xticks(rotation=90)
plt.title("Trend of City 1 (with lockdown)")
plt.subplot(122)
plt.plot(datelist,infected2,color="darkred",alpha=0.5)
plt.plot(datelist,recover2,color="green",alpha=0.5,linestyle="--")
plt.plot(datelist,dead2,color="grey",alpha=0.7)
plt.plot(datelist,expose2,color="purple",alpha=0.5)
plt.plot(datelist,suscept2,color="orange",alpha=0.5)
plt.title("Trend of City 2 (with lockdown)")
plt.ylabel("Population")
plt.legend(["infected","recovered","died","exposed","susceptible"])
plt.xlabel("Date")
plt.xticks(rotation=90)
plt.savefig("lockdown")
'''