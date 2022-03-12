import csv
import plotly.express as pl
import pandas as ps
import plotly.figure_factory as plf
df = ps.read_csv("data.csv")
figure = plf.create_distplot([df["Weight(Pounds)"].to_list()],["weight"],show_hist=False)
figure.show()