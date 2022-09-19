import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
import joblib
import dataSample as ds
from sklearn.utils import shuffle as sf
import os

# mbti type
mbti_type = {
    "A" : "대식가",
    "B" : "소식좌",
    "C" : "애주가",
    "D" : "개척자",
    "E" : "분석가",
    "F" : "인스타",
    "G" : "내신1등",
    "H" : "푸드슈타인",
    "I" : "위장 월세형",
    "J" : "위부장님",
    "K" : "앙드레 푸드",
    "L" : "스틸 통규씨",
    "N" : "헨젤이 그랬대",
    "M" : "포세이돈",
    "O" : "배달VVIP",
}

# 유형별 데이터 수 입력
sample_count = 200

# mbti 유형 네임들
group_count = mbti_type.keys()
sample = []
for i in group_count :
    globals()['a_'+i] = ds.create_sample(sample_count, i) # 변수명 바꾸면서 할당
    sample.append(globals()['a_'+i]) # 리스트에 데이터 붙이기

total = np.concatenate(sample, 0) # numpy array로 바꾸기 # 원래는 여러 numpy array 합침(np..concatenate)는 array 합침, axis=0(y축)
data = total[:,1:]
columns=["Category", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20" , "Q21", "Q22", "Q23", "Q24", "Q25", "Q26", "Q27", "Q28", "Q29", "Q30", "Q31", "Q32", "Q33", "Q34", "Q35", "Q36", "Q37", "Q38", "Q39", "Q40"]
df = pd.DataFrame(data=data, columns=columns)
print(df.shape)

# 전처리
from sklearn.model_selection import train_test_split

# 모델
# from sklearn.neighbors import KNeighborsClassifier # KNN
# from sklearn.tree import DecisionTreeRegressor # 의사결정나무
from sklearn.ensemble import RandomForestClassifier # 앙상블

print(df['Category'].unique()) # 값 확인

# 정답 제거된 컬럼명 집합
x_columns = df.drop("Category", axis=1).columns
# 정답 컬럼명
y_columns = 'Category'

X = df[x_columns]
y = df[y_columns]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=23)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
df = sf(df)

# 학습
model = RandomForestClassifier(n_estimators=3, random_state=23)
model.fit(X_train, y_train)

print(mbti_type[model.predict(X_test[:1])[0]])
# 저장
print(os.getcwd())
joblib.dump(model, '/forest.pkl')


#loaded_model = joblib.load("./test.pkl")
#y_pred= loaded_model.predict(data[0])

#print(y_pred)