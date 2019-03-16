# Machine Learning

## 1. Label 유무에 따른 분류
- 1.1. Label(정답)이 있으면 Supervised Learning (지도학습)
- 1.2. Label(정답)이 없으면 Unsupervised Learning (비지도학습)

---
# Machine Learning
## 2. Label 종류에 따른 분류
- 2.1. Regression (회귀) : 종속변수(y)가 수치형
	- 종속변수(Y)에 중요한 영향을 주는 주요 독립변수 선별
	- 회귀 모형이 학습되었을 때, 새로운 독립 변수의 값으로부터 종속 변수의 값을 예측할 수 있다.
	- ex) $y = \beta_0 + \beta_1\chi_1 + \beta_2\chi_2 + \beta_3\chi_3 +  ... + \varepsilon$

<br>

- 2.2. Classification (분류) : 종속변수(y)가 명목형
	- Supervised Learning의 일종으로 다양한 X 변수들과 미리 정의된 class 변수(Y)와의 관계를 밝히는 과정
	- Traning set으로 모델을 학습한 뒤, 새로운 data(Test set)가 주어졌을 때, data의 class를 밝혀내고 정확하게 분류하는 것


---
# Machine Learning Algorithms
## 2.1. Regression (회귀) - 종속변수(y)가 수치형
- Linear Regression
- Multiple Linear Regression
- Shrinkage Method
	- Ridge Regression
    - Lasso Regression
    - k-NN (k-Nearest Neighbors)
    - Regression Tree
    - ANN (Artificial Neural Network)
    - SVM (Support Vector Machine)

---
# Machine Learning Algorithms
## 2.2. Classification (분류) - 종속변수(y)가 명목형
- k-NN (k-Nearest Neighbors)
- Decision Tree
- ANN (Artificial Neural Network)
- SVM (Support Vector Machine)
- Logistic Regerssion

---
# Machine Learning Algorithms
## 3. Ensemble Learning(앙상블)
- Bagging
- Random Forest
- Boosting
	- light gbm, xgboost, catboost ...