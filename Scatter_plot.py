# Example: Load the studyhours dataset and plot to see the relationship between the study hours and scores.
import pandas as pd
import matplotlib.pyplot as plt

studyhours_df = pd.read_csv('Data/studyhours.csv')
print(studyhours_df.head())

studyhours_df.describe()

# make scatter plot of study hours vs. final grades
# init figure with a specific size 
plt.figure(figsize=(10,6))

study_hours = studyhours_df['StudyHours']
exam_score = studyhours_df['ExamScore']

plt.scatter(study_hours, exam_score,
            alpha=0.75,
            label="Study hours vs Exam score",)
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")