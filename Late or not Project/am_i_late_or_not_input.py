# Project on Late or not for Bus

import pandas as pd
# from sklearn.linear_model import LinearRegression

t=int(input('Enter no. of inputs = '))
Day, Temp, Wakeup_Time, Dep_Home_Time, Metro_Aboard, Metro_Travel, Metro_Deboard, Bus_Stop_Time, Late = [],[],[],[],[],[],[],[],[]

for i in range(t):
    Day.append(input())
    Temp.append(int(input()))
    Wakeup_Time.append(int(input()))
    Dep_Home_Time.append(int(input()))
    Metro_Aboard.append(int(input()))
    Metro_Travel.append(int(input()))
    Metro_Deboard.append(int(input()))
    Bus_Stop_Time.append(int(input()))
    Late.append(input())

data_set = list(zip(Day, Temp, Wakeup_Time, Dep_Home_Time,
                    Metro_Aboard, Metro_Travel, Metro_Deboard,
                    Bus_Stop_Time, Late))

df = pd.DataFrame(data = data_set, columns = ['Day', 'Temp', 'Wakeup_Time', 'Dep_Home_Time','Metro_Aboard_Time', 'Metro_Travel_Time', 'Metro_Deboard_Time','Bus_Stop_Time','Late'])

df.to_csv('late_project_data.csv', index = False, header = False)

