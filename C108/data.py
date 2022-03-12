import csv 
import plotly.express as pl
import pandas as pa
import plotly.figure_factory as plf
df = pa.read_csv("data.csv")
figure = plf.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist=False)
figure.show()