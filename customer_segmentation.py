import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
df=pd.read_csv("Mall_Customers.csv")
df.head()
plt.figure(figsize=(5, 3))
sns.set(style = 'whitegrid')
sns.distplot(df['Annual Income (k$)'])
plt.title('Distribution of Annual Income (k$)', fontsize = 20)
plt.xlabel('Range of Annual Income (k$)')
plt.ylabel('Count')
plt.figure(figsize=(5, 3))
sns.set(style = 'whitegrid')
sns.distplot(df['Age'])
plt.title('Distribution of Age', fontsize = 20)
plt.xlabel('Range of Age')
plt.ylabel('Count')
plt.figure(figsize=(5, 3))
sns.set(style = 'whitegrid')
sns.distplot(df['Spending Score (1-100)'])
plt.title('Distribution of Spending Score (1-100)', fontsize = 20)
plt.xlabel('Range of Spending Score (1-100)')
plt.ylabel('Count')
plt.figure(figsize=(10,5))
sns.countplot(y='Gender',data=df)
plt.show()
plt.figure(1,figsize=(15,8))
m=0
for colm in ['Age' , 'Annual Income (k$)' , 'Spending Score (1-100)']:
    m+=1
    plt.subplot(1 , 3 , m)
    sns.set(style='whitegrid')
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.violinplot(x = colm , y= 'Gender' , data=df)
    plt.ylabel('Gender' if m == 1 else '')
    plt.title('violinplot')
plt.show()

age_18_25= df.Age[(df.Age >= 18) & (df.Age <= 25)]
age_26_40= df.Age[(df.Age >= 26) & (df.Age <= 40)]
age_41_55= df.Age[(df.Age >= 41) & (df.Age <= 55)]
age_above55= df.Age[(df.Age >= 56)]
agex = ["18-25","26-40","41-55","55+"]
agey = [len(age_18_25.values),len(age_26_40.values),len(age_41_55.values),len(age_above5
5.values)]
plt.figure(figsize=(15,8))
sns.barplot(x=agex, y=agey , palette="mako")
plt.title("Majority of people from Age")
plt.xlabel("Age")
plt.ylabel("Number Of People")
plt.show()
sns.relplot(x="Annual Income (k$)" , y="Spending Score (1-100)" , data=df)
ss_1_20=df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 1) & (df["Spendin
g Score (1-100)"] <= 20)]
ss_21_40=df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 21) & (df["Spend
ing Score (1-100)"] <= 40)]
ss_41_60=df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 41) & (df["Spend
ing Score (1-100)"] <= 60)]
ss_61_80=df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 61) & (df["Spend
ing Score (1-100)"] <= 80)]
ss_81_100=df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 81) & (df["Spen
ding Score (1-100)"] <= 100)]
ssx = ["1-20","21-40","41-60","61-80","81-100"]
ssy = [len(ss_1_20.values),len(ss_21_40.values),len(ss_41_60.values),len(ss_61_80.values),l
en(ss_81_100.values)]
plt.figure(figsize=(15,10))
sns.barplot(x = ssx , y = ssy , palette="rocket")
plt.title("Spending Socre")
plt.xlabel("Score")
plt.ylabel("Numner Of Customers")
plt.show()
ai0_30=df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 0) & (df["Annual Income (
k$)"] <= 30)]
ai31_60=df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 31) & (df["Annual Incom
e (k$)"] <= 60)]
ai61_90=df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 61) & (df["Annual Incom
e (k$)"] <= 90)]
ai91_120=df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 91) & (df["Annual Inco
me (k$)"] <= 120)]
ai121_150=df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 121) & (df["Annual Inc
ome (k$)"] <= 150)]
aix = ["0 - 30,000","30,001 - 60,000","60,001 - 90,000","90,001 - 120,000","120,001 - 150,0
00"]
aiy = [len(ai0_30.values),len(ai31_60.values),len(ai61_90.values),len(ai91_120.values),len(ai
121_150.values)]
plt.figure(figsize=(15,10))
sns.barplot(x = aix , y = aiy , palette="Spectral")
plt.title("Annual Income")
plt.xlabel("Income")
plt.ylabel("Numner Of Customers")
plt.show()
x1=df.loc[:,["Age","Spending Score (1-100)"]].values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
km=KMeans(n_clusters=i)
km.fit(x1)
wcss.append(km.inertia_)
plt.figure(figsize=(12,6))
plt.plot(range(1,11),wcss)
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()
kmeans = KMeans(n_clusters=5)
label = kmeans.fit_predict(x1)
print(label)
print(kmeans.cluster_centers_)
plt.scatter(x1[:,0],x1[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.title("Customer's Clustering")
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()
x2=df.loc[:,["Annual Income (k$)","Spending Score (1-100)"]].values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
km=KMeans(n_clusters=i)
km.fit(x2)
wcss.append(km.inertia_)
plt.figure(figsize=(12,6))
plt.plot(range(1,11),wcss)
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")

plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()
kmeans = KMeans(n_clusters=5)
label = kmeans.fit_predict(x2)
print(label)
print(kmeans.cluster_centers_)
plt.scatter(x2[:,0],x2[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.title("Customer's Clustering")
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()
x3=df.iloc[:,1:]
wcss=[]
for i in range(1,11):
km=KMeans(n_clusters=i)
km.fit(x2)
wcss.append(km.inertia_)
plt.figure(figsize=(12,6))
plt.plot(range(1,11),wcss)
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()
kmeans = KMeans(n_clusters = 5)
label = kmeans.fit_predict(x3)
print(label)
print(kmeans.cluster_centers_)
clusters = kmeans.fit_predict(x3)
df["label"] = clusters
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.Age[df.label == 0], df["Annual Income (k$)"][df.label == 0], df["Spending Scor
e (1-100)"][df.label == 0], c='purple', s=60)
ax.scatter(df.Age[df.label == 1], df["Annual Income (k$)"][df.label == 1], df["Spending Scor
e (1-100)"][df.label == 1], c='red', s=60)
ax.scatter(df.Age[df.label == 2], df["Annual Income (k$)"][df.label == 2], df["Spending Scor
e (1-100)"][df.label == 2], c='blue', s=60)
ax.scatter(df.Age[df.label == 3], df["Annual Income (k$)"][df.label == 3], df["Spending Scor
e (1-100)"][df.label == 3], c='green', s=60)
ax.scatter(df.Age[df.label == 4], df["Annual Income (k$)"][df.label == 4], df["Spending Scor
e (1-100)"][df.label == 4], c='yellow', s=60)
ax.view_init(35, 185)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.show()