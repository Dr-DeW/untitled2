

from pandas import read_csv, DataFrame, Series
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import roc_curve, auc
import pylab as pl







data = read_csv('train.csv')
fig, axes = plt.subplots(ncols=2)
# data.pivot_table('PassengerId',['SibSp'],'Survived','count').\
#     plot(ax=axes[0], title='SibSp')
# data.pivot_table('PassengerId',['Parch'],'Survived','count').\
#     plot(ax=axes[1], title='Parch')
# plt.show()
#print(data.PassengerId[data.Cabin.notnull()].count())
#print(data.PassengerId[data.Age.notnull()].count())
data.Age = data.Age.median()
maxPassEmb = data.groupby('Embarked').count()['PassengerId']
data.Embarked[data.Embarked.isnull()] = maxPassEmb[maxPassEmb == maxPassEmb.max()].index[0]
#print(data[data.Embarked.isnull()])
#print(data.PassengerId[data.Fare.isnull()])
data = data.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)

label = LabelEncoder()
dicts = {}

label.fit(data.Sex.drop_duplicates())
dicts['Sex'] = list(label.classes_)
data.Sex = label.transform(data.Sex)

label.fit(data.Embarked.drop_duplicates())
dicts['Embarked'] = list(label.classes_)
data.Embarked = label.transform(data.Embarked)


test = read_csv('test.csv')
test.Age = test.Age.median()
test.Fare[test.Fare.isnull()] = test.Fare.median()
maxPassEmb = test.groupby('Embarked').count()['PassengerId']
test.Embarked[test.Embarked.isnull()] = maxPassEmb[maxPassEmb == maxPassEmb.max()].index[0]
result = DataFrame(test.PassengerId)
test = test.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)
label = LabelEncoder()
dicts = {}
label.fit(test.Sex.drop_duplicates())
dicts['Sex'] = list(label.classes_)
test.Sex = label.transform(test.Sex)
label.fit(test.Embarked.drop_duplicates())
dicts['Embarked'] = list(label.classes_)
test.Embarked = label.transform(test.Embarked)

target = data.Survived
train = data.drop(['Survived'], axis=1)
kfold = 5
itog_val = {}

ROCtrainTRN,ROCtestTRN, ROCtrainTRG,ROCtestTRG = train_test_split(train,target,test_size=0.25)

model_rkc = RandomForestClassifier(n_estimators=70)
model_knc = KNeighborsClassifier(n_neighbors=18)
model_lr = LogisticRegression(penalty='l2',tol=0.01)
model_svc = svm.SVC()

score = cross_val_score(model_rkc, train, target, cv=kfold)
itog_val['RondForestC'] = score.mean()
score = cross_val_score(model_knc, train, target, cv=kfold)
itog_val['KNeigBC'] = score.mean()
score = cross_val_score(model_lr, train, target, cv=kfold)
itog_val['LR'] = score.mean()
score = cross_val_score(model_svc, train, target, cv=kfold)
itog_val['SVC'] = score.mean()

# DataFrame.from_dict(data = itog_val,orient='index').plot(kind='bar',legend=False)
# plt.show()

pl.clf()
plt.figure(figsize=(8,6))
#SVC
model_svc.probability = True
probas = model_svc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('SVC', roc_auc))
#RandomForestClassifier
probas = model_rkc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('RandonForest',roc_auc))
#KNeighborsClassifier
probas = model_knc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('KNeighborsClassifier',roc_auc))
#LogisticRegression
probas = model_lr.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('LogisticRegression',roc_auc))
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')
#pl.show()

model_rkc.fit(train, target)
result.insert(1,'Survived', model_rkc.predict(test))
result.to_csv('test.csv', index=False)
print(result)