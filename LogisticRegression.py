import pandas as pd

data_path = "Data/student_performance_prediction.csv"
exam_df = pd.read_csv(data_path)

exam_df.head()


# Exploratory Data Analysis

# Show descriptive statistics
exam_df.describe()
print(len(exam_df))

# Check missing value
print(exam_df.isna().sum())

exam_df.dropna(inplace = True)

# Check again
exam_df.describe()

print(exam_df.columns)

# Get study hour per week as single input(X), Passed as output(y)
# Encoding passed/fail labels
exam_df['Label'] = exam_df.apply(lambda x:1 if x['Passed'] == 'Yes' else 0, axis=1)
exam_df.head()

import numpy as np

X = np.asarray(exam_df['Study Hours per Week'])
y = np.asarray(exam_df['Label'])
print(X.shape, y.shape)

X = X.reshape(-1,1)
# y = y.reshape(-1,1)

# Split the dataset into train set and test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.2,
                                                    stratify=y)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

y_test.shape

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
 
clf = make_pipeline(StandardScaler(),
                    LogisticRegression(max_iter=1000))
clf.fit(X_train, y_train)
print(f'Prediction on test set: {clf.score(X_test, y_test)}')          # 0.965
 
proba = clf.predict_proba(X_test[:5])[:, 1]
print(proba.round(3))      # [0.999 0.004 1.    0.    0.035]
print(y_test[:5])             # [1 0 1 0 0]


# Naive Bayes Classfication
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
 
emails = ["win free money now", "free prize claim now",
          "cheap money offer win", "meeting schedule for monday",
          "lunch with the team", "project report for monday"]
labels = [1, 1, 1, 0, 0, 0]                    # 1 = spam
vec = CountVectorizer()
nb = MultinomialNB(alpha=1).fit(vec.fit_transform(emails), labels)
 
for s in ["free money", "team meeting on monday",
          "free lunch with the team"]:
    print(s, nb.predict_proba(vec.transform([s]))[0, 1].round(3))
# free money 0.9
# team meeting on monday 0.077
# free lunch with the team 0.158   <- one spammy word is not enough


# Real example of spam email classification using Multinomial Naive Bayes
# Load the dataset

email_data_path = 'Data/spam_or_not_spam.csv'
email_df = pd.read_csv(email_data_path)

email_df.head()

email_df.describe()

print(email_df.isna().sum())

email_df.dropna(inplace=True)
print(email_df.isna().sum())

email_df.describe()


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Get email content from the dataset
emails = email_df['email']
labels = email_df['label']

# Init text feature extraction
vec = CountVectorizer()

# Fit the model from the data
nb = MultinomialNB(alpha=1).fit(vec.fit_transform(emails), labels)


# Make some prediction

for s in ["free money", "team meeting on monday",
          "free lunch with the team"]:
    print(s, nb.predict_proba(vec.transform([s]))[0, 1].round(3))


