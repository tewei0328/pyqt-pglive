import pglive.examples_pyside2 as examples
import signal
from threading import Thread

from pglive.sources.data_connector import DataConnector
from pglive.sources.live_plot import LiveScatterPlot
from pglive.sources.live_plot_widget import LivePlotWidget

"""
Scatter plot is displayed in this example.
"""
win = LivePlotWidget(title="Scatter Plot @ 100Hz")
plot = LiveScatterPlot()
win.addItem(plot)

data_connector = DataConnector(plot, max_points=600)

win.show()

Thread(target=examples.sin_wave_generator, args=(data_connector,)).start()
signal.signal(signal.SIGINT, lambda sig, frame: examples.stop())
examples.app.exec_()
examples.stop()
