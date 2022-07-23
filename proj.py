import pandas as pd
import plotly.express as px
import numpy as np
# make sure the modules are installed if not install
#  for example pip install pandas

df = pd.read_csv("main.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.show()

m = 1
c = 0
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
# Step 1 : Uncomment the code out of the 4 options given below : 

# fig.update_layout(shapes=[
#     dict(
#       type= 'circle',
#       y0= min(y), y1= max(y),
#       x0= min(TOEFL_Score), x1= max(TOEFL_Score)
#     )
# ])


# fig.update_layout(shapes=[
#     dict(
#       type= 'line',
#       x0= min(y), x1= max(y),
#       x2= min(TOEFL_Score), x3= max(TOEFL_Score)
#     )
# ])


# fig.update_layout(shapes=[
#     dict(
#       type= 'line',
#       y0= min(y), y1= max(y),
#       x0= min(TOEFL_Score), x1= max(TOEFL_Score)
#     )
# ])


# fig.update(shapes=[
#     dict(
#       type= 'line',
#       y0= min(y), y1= max(y),
#       x0= min(TOEFL_Score), x1= max(TOEFL_Score)
#     )
# ])
fig.show()


m = 0.018
c = -1.27
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()


x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")



TOEFL_array = np.array(TOEFL_Score)
Chances_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy

# Step 2 : Uncomment the code out of the 4 options given below : 

# m, c = np.polyfit(TOEFL_array, Chances_array, 0)
# m, c = np.poly(TOEFL_array, Chances_array, 1)
# m, c = np.polyfit(TOEFL_array, Chances_array, 1)
# m = np.polyfit(TOEFL_array, Chances_array, 1)

y = []
for x in TOEFL_array:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_array, y=Chances_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_array), x1= max(TOEFL_array)
    )
])
fig.show()


x = 250
# Step 3 : Uncomment the code out of the 4 options given below : Formula of slope- intercept on the line

# y = m + x + c
# y = m * x 
# y = m  + c
# y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")