# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# data = {
#     'Temperature': [23, 22, 12, 32, 14, 20, 22, 22, 22, 21],
#     'Movement': [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
    
# }

# df = pd.DataFrame(data)
# print(df)

# plt.figure(figsize=(10,5))

# plt.subplot(2, 1, 1)
# plt.plot(df["Temperature"], label = "Temperature")
# plt.xlabel("Time")
# plt.ylabel("Temperature")
# plt.legend()

# plt.subplot(2, 1, 2)
# plt.plot(df["Movement"], label = "Movement")
# plt.xlabel("Time")
# plt.ylabel("Movement")
# plt.legend()
# plt.tight_layout()
# plt.show()

import turtle
# turtle.Screen()

# from turtle import Screen
# turtle_screen = turtle.Screen()

# from turtle import *
# turtle_screen = Screen()
sipi = turtle.Turtle() # luo uusi kilpikonna-olio
sipi.shape("turtle") # metodi
sipi.color("green") # metodi
sipi.forward(100) # metodi
sipi.right(90)
sipi.forward(100)
sipi.right(90)
sipi.forward(100)
sipi.right(90)
sipi.forward(100)


turtle_screen = turtle.Screen() # Luo ikkuna-olio
turtle_screen.exitonclick() # Metodi
