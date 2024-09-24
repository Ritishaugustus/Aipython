import pandas as p
import matplotlib.pyplot as plt
data=p.read_csv(r"C:\Users\ritish\Downloads\Titanic-Dataset.csv")
df=p.DataFrame(data)
print(data)
survivedage=data[data['Survived']==1]['Age']
notsurvived=data[data['Survived']==0]['Age']
plt.hist(survivedage,color='g',label='survived')
plt.hist(notsurvived,color='r',alpha=0.5,label='not survived')
plt.xlabel('age')
plt.ylabel('frequency')
plt.legend()
plt.show()
