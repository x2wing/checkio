if __name__ == '__main__':
    import pyqtgraph as pg
    import PyQt5
    import numpy as np
    from math import (sqrt, pi)

    import pyqtgraph.examples

    # t = np.linspace(0, 2*pi,120)
    # r = 5
    # print(t)
    # pg.plot(r*np.sin(t)+5, r*np.cos(t)+5, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50),
    #         title="Simplest possible plotting example")
    # pg.plot.showGrid(x=True, y=True)

    # data = np.random.normal(size=(500, 500))
    # pg.image(data, title="Simplest possible image example")

    ## Start Qt event loop unless running in interactive mode or using pyside.

    from pyqtgraph.Qt import QtGui, QtCore
    import numpy as np
    import pyqtgraph as pg

    # QtGui.QApplication.setGraphicsSystem('raster')
    app = QtGui.QApplication([])
    # mw = QtGui.QMainWindow()
    # mw.resize(800,800)

    win = pg.GraphicsWindow(title="Basic plotting examples")
    win.resize(600, 600)
    win.setWindowTitle('pyqtgraph example: Plotting')

    # Enable antialiasing for prettier plots
    pg.setConfigOptions(antialias=True)

    t = np.linspace(0, 2*pi,120)
    r = 5

    p1 = win.addPlot(x=r*np.sin(t)+5, y=r*np.cos(t)+5)
    p1.showGrid(x=True, y=True)

    if __name__ == '__main__':
        import sys

        if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
            pg.QtGui.QApplication.exec_()
