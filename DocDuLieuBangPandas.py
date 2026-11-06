# Đọc file Excel
import pandas as pd

# Đường dẫn tới file cần đọc
data_file_path = ""

# Đọc data
df = pd.read_excel(data_file_path)

# In ra dòng S

df.head(S)

df.iloc[:, :9]

# Lọc ra 2 cột MSSV và điểm số
df.loc[:, ['Username', 'Grade/10.00']]

high_grade_df = df.loc[df['Grade/10.00'] >=9, ['Username', 'Grade/10.00']]

