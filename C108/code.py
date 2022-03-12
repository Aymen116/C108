import random 
import plotly.express as pl
import plotly.figure_factory as plf
dice_result = []
count = []
for i in range (0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
figure = pl.bar(x = dice_result, y = count)
figure = plf.create_distplot([dice_result],["result"],show_hist=False)
figure.show()