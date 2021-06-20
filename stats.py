import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import statistics 
import random
import plotly.graph_objects as go

rolls = []
count = []
diceResults = []

df = pd.read_csv("bmi.csv")

heightList = df["Height(Inches)"].to_list()

weightList = df["Weight(Pounds)"].to_list()

# for number in range(0,1000):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     diceResults.append(dice1 + dice2)

heightMean = sum(heightList) / len(heightList)

weightMean = sum(weightList) / len(weightList)

heightMedian = statistics.median(heightList)

weightMedian = statistics.median(weightList)

heightMode = statistics.mode(heightList)

weightMode = statistics.mode(weightList)

hstd_deviation = statistics.stdev(heightList)

wstd_deviation = statistics.stdev(weightList)

first_std_deviation_start, first_std_deviation_end = heightMean-hstd_deviation, heightMean+hstd_deviation
second_std_deviation_start, second_std_deviation_end = heightMean-(2*hstd_deviation), heightMean+(2*hstd_deviation)
third_std_deviation_start, third_std_deviation_end = heightMean-(3*hstd_deviation), heightMean+(3*hstd_deviation)

list_of_data_within_1_std_deviation = [result for result in heightList if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in heightList if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in heightList if result > third_std_deviation_start and result < third_std_deviation_end]

print("heightMean of this data is {}".format(heightMean))
print("Median of this data is {}".format(heightMedian))
print("Mode of this data is {}".format(heightMode))
print("Standard deviation of this data is {}".format(hstd_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(heightList)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(heightList)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(heightList)))

fig = ff.create_distplot([heightList],["Results"],show_hist=False)
fig.add_trace(go.Scatter(x=[heightMean, heightMean], y=[0, 0.17], mode="lines", name="heightMean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()
