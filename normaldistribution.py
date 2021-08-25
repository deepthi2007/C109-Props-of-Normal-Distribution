import pandas as pd 
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics as st

df = pd.read_csv("D:\deepthi projects\C109\StudentsPerformance.csv")
scores = df["writing score"].tolist()

print("{} is the mean of writing scores".format(st.mean(scores)))
print("{} is the median of the writing scores ".format(st.median(scores)))
print("{} is mode of the writing scores".format(st.mode(scores)))
print("{} is the St Deviation of writing scores.".format(st.stdev(scores)))

Mainmean = st.mean(scores)
MainStDev = st.stdev(scores)

firstStDevStart , firstStDevEnd = Mainmean-MainStDev , Mainmean+MainStDev
range1 = [i for i in scores if i > firstStDevStart and i < firstStDevEnd]
print("{}% of data lies between the 1st St Deviation".format((len(range1)/len(scores))*100))

secondStDevStart , secondStDevEnd = Mainmean-(MainStDev*2) , Mainmean+(MainStDev*2)
range2 = [i for i in scores if i > secondStDevStart and i < secondStDevEnd]
print("{}% of data lies between the 2nd St Deviation".format((len(range2)/len(scores))*100))

thridStDevStart , thridStDevEnd = Mainmean-(MainStDev*3) , Mainmean+(MainStDev*3)
range3 = [i for i in scores if i > thridStDevStart and i < thridStDevEnd]
print("{}% of data lies between the 3rd St Deviation".format((len(range3)/len(scores))*100))

fig = pf.create_distplot([scores],["Writing Scores"],show_hist=False)
fig.add_trace(pg.Scatter(x=[Mainmean,Mainmean],y=[0,1],mode="lines",name="Mean"))
fig.add_trace(pg.Scatter(x=[firstStDevStart,firstStDevStart],y=[0,1],mode="lines",name="St Deviation 1"))
fig.add_trace(pg.Scatter(x=[firstStDevEnd,firstStDevEnd],y=[0,1],mode="lines",name="St Deviation 1"))
fig.add_trace(pg.Scatter(x=[secondStDevStart,secondStDevStart],y=[0,1],mode="lines",name="St Deviation 2"))
fig.add_trace(pg.Scatter(x=[secondStDevEnd,secondStDevEnd],y=[0,1],mode="lines",name="St Deviation 2"))
fig.add_trace(pg.Scatter(x=[thridStDevStart,thridStDevStart],y=[0,1],mode="lines",name="St Deviation 3"))
fig.add_trace(pg.Scatter(x=[thridStDevEnd,thridStDevEnd],y=[0,1],mode="lines",name="St Deviation 3"))
fig.show()