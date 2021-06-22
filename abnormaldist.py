import statistics
import plotly.figure_factory as ff
import plotly_express as px
import pandas as pd
import random
import csv
import plotly.graph_objects as go

df = pd.read_csv("temp.csv")

data = df["temp"].to_list()

# mean = sum(data) / len(data)

# median = statistics.median(data)

# mode = statistics.mode(data)

# print("Mean: ",mean)

# print("Median: ",median)

# print("Mode: ",mode)

# fig = ff.create_distplot([data],["Temperature"],show_hist=False)
# fig.show()

def randomExtractor(counter):
    dataset = []
    for num in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFig(mean_list):
    de = mean_list
    mean = statistics.mean(de)
    print("Mean of Sampling Distribution: ",mean)
    fig = ff.create_distplot([de],["Temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 1], mode="lines", name="Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        setOfMeans = randomExtractor(100)
        mean_list.append(setOfMeans)
    showFig(mean_list)

setup()