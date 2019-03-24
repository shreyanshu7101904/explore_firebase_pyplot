import matplotlib.pyplot as plt


class Plotter:

    def __init__(self, name):
        self.plot_name = name


    def createBarPlot(self, x_coordinates, y_coordinates):
        plt.bar(x_coordinates, y_coordinates, width = 0.8, color = 'red')
        plt.show()