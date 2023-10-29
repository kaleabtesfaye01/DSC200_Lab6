import pandas as pd

hourly_rates_df = pd.read_csv('./data/Hourly_Rates_of_Pay_by_Classification_and_Step.csv')
employee_demo_df = pd.read_csv('./data/Employee+Demographics.csv')
average_weekly_hours_df = pd.read_csv('./data/Average_weekly_hours_of_all_employees.csv', index_col=0)

merged_df = pd.merge(hourly_rates_df, employee_demo_df, right_on='JobTitle', left_on='Title', how='inner')
average_weekly_hours_df = average_weekly_hours_df.T
merged_df['Average_Weekly_Hours'] = 0

print(merged_df.columns)