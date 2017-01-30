import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, neighbors
import numpy as np
from tkinter import *

Loc = r'C:\Users\Yashwant\Desktop\Late or not Project\late_project_data.csv'

df = pd.read_csv(Loc, names = ['Day', 'Temp', 'Wakeup_Time', 'Dep_Home_Time','Metro_Aboard_Time', 'Metro_Travel_Time', 'Metro_Deboard_Time','Bus_Stop_Time','Late'])

x = np.array(df.drop(['Late'],1))
y = np.array(df['Late'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)

# classification model
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)

acc = clf.score(x_test, y_test)

##5,713,740,746,800,14,814,815


def test(l):
    l2 = [];
    for i in range(len(l)):
        l[i].configure(state = 'disable')
        l2.append(int(l[i].get()))
    np.array(l2, dtype = 'int64');
    prediction = clf.predict(l2)
    r1 = Tk();
    if prediction[0] == 0:
        lb = Label(r1, text = 'Not Late').pack()
    else:
        lb = Label(r1, text = 'Late').pack()
    r1.mainloop();

r = Tk();
r.geometry('300x400')
l = [];

para= ['Day', 'Temp', 'Wakeup_Time', 'Dep_Home_Time','Metro_Aboard_Time', 'Metro_Travel_Time', 'Metro_Deboard_Time','Bus_Stop_Time'];

for i in range(len(para)):
    la = Label(text = para[i]).pack();
    e = Entry(r);
    l.append(e);
    e.pack();

b = Button(r, text = "Predict", command = lambda: test(l)).pack();
r.mainloop()
