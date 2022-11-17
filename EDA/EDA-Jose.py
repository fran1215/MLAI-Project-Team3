import pandas as pd
import matplotlib.pyplot as plt


testcsv = pd.read_csv('./airplane-dataset/test.csv')

testcsv.loc[testcsv.satisfaction == 'satisfied', 'satisfaction'] = 1
testcsv.loc[testcsv.satisfaction == 'neutral or dissatisfied', 'satisfaction'] = 0

testcsv.loc[testcsv['Type of Travel'] == 'Business travel', 'Type of Travel'] = 1
testcsv.loc[testcsv['Type of Travel'] == 'Personal Travel', 'Type of Travel'] = 0

testcsv.loc[testcsv['Customer Type'] == 'Loyal Customer', 'Customer Type'] = 1
testcsv.loc[testcsv['Customer Type'] == 'disloyal Customer', 'Customer Type'] = 0

testcsv.loc[testcsv['Gender'] == 'Female', 'Gender'] = 1
testcsv.loc[testcsv['Gender'] == 'Male', 'Gender'] = 0

testcsv.loc[testcsv['Class'] == 'Business', 'Class'] = 2
testcsv.loc[testcsv['Class'] == 'Eco Plus', 'Class'] = 1
testcsv.loc[testcsv['Class'] == 'Eco', 'Class'] = 0


print(testcsv['Customer Type'].value_counts())
print(testcsv['Type of Travel'].value_counts())
print(testcsv['Class'].value_counts())
print(testcsv['Gender'].value_counts())

print(testcsv[0:20])


# print(testcsv['Customer Type'].value_counts())
# print(testcsv['Customer Type'].value_counts())
# print(testcsv['Customer Type'].value_counts())
# print(testcsv['Customer Type'].value_counts())


# print(testcsv.columns)


# testcsv.Age[0:100].plot()

# plt.show()
# testcsv.plot()
# plt.close('all')

# Index(['Unnamed: 0', 'id', 'Gender', 'Customer Type', 'Age', 'Type of Travel',
#        'Class', 'Flight Distance', 'Inflight wifi service',
#        'Departure/Arrival time convenient', 'Ease of Online booking',
#        'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
#        'Inflight entertainment', 'On-board service', 'Leg room service',
#        'Baggage handling', 'Checkin service', 'Inflight service',
#        'Cleanliness', 'Departure Delay in Minutes', 'Arrival Delay in Minutes',
#        'satisfaction'],
#       dtype='object')
