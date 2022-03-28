import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib_inline.backend_inline import FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100, x=None, y=None, f=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        if all(x):
            self.x = np.array(x)
        if all(y):
            self.y = np.array(y)
        if all(f):
            self.f = np.array(f)

        print("Canvas: type(self.x, type(self.y), type(self.f)=", type(self.x), type(self.y), type(self.f))

        self.fig, self.ax = plt.subplots()

        FigureCanvas.__init__(self, fig)

        # self.setParent(parent)

        self.plot()

    def plot(self):
        # print("mpl_canvas, x, x.shape, y, y.shape: ", self.x, self.x.shape, self.y, self.y.shape)
        print("mpl_canvas, f.shape: ", self.f.shape)

        line1, = self.ax.plot(self.x, self.y, 'or', linewidth=2,
                              label='position')

        # line2, = self.ax.plot(self.x, self.calc_values, dashes=[30, 5, 10, 5],
        #                       label='Regression')

        plt.grid(True)
        self.ax.legend(loc='lower right')
        plt.show()
