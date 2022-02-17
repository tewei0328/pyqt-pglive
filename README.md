# Live pyqtgraph plot

Pglive package adds support for thread-safe live plotting to pyqtgraph.  
It supports PyQt5 and PyQt6.

# Description #

By default, pyqtgraph doesn't support live plotting. Aim of this package is to provide easy implementation of Line,
Scatter and Bar Live plot. Every plot is connected with it's DataConnector, which sole purpose is to consume data points
and manage data re-plotting. DataConnector interface provides Pause and Resume method, update rate and maximum number of
plotted points. Each time data point is collected, call `DataConnector.cb_set_data`
or `DataConnector.cb_append_data_point` callback. That's all You need to update plot with new data. Callbacks are Thread
safe, so it works nicely in applications with multiple data collection Threads.

**Focus on data collection and leave plotting to pglive.**

To make firsts steps easy, package comes with many examples implemented in PyQt5 or PyQt6.

# Code examples #

```python
import sys
from math import sin
from threading import Thread
from time import sleep

from PyQt6.QtWidgets import QApplication

from pglive.sources.data_connector import DataConnector
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.live_plot_widget import LivePlotWidget

"""
In this example Line plot is displayed.
"""
app = QApplication(sys.argv)
running = True

plot_widget = LivePlotWidget(title="Line Plot @ 100Hz")
plot_curve = LiveLinePlot()
plot_widget.addItem(plot_curve)
# DataConnector holding 600 points and plots @ 100Hz
data_connector = DataConnector(plot_curve, max_points=600, update_rate=100)


def sin_wave_generator(connector):
    """Sinus wave generator"""
    x = 0
    while running:
        x += 1
        data_point = sin(x * 0.01)
        # Callback to plot new data point
        connector.cb_append_data_point(data_point, x)

        sleep(0.01)


plot_widget.show()
Thread(target=sin_wave_generator, args=(data_connector,)).start()
app.exec()
running = False
```

Output:

![Plot example](https://i.postimg.cc/RFYGfNS6/pglive.gif)

To run built-in examples, use python3 -m parameter like:  
`python3 -m pglive.examples_pyqt6.all_plot_types`  
`python3 -m pglive.examples_pyqt6.crosshair`

# Available plot types #

Pglive supports four plot types: `LiveLinePlot`, `LiveScatterPlot`, `LiveHBarPlot` (horizontal bar plot)
and `LiveVBarPlot` (vertical bar plot).

![All plot types](https://i.postimg.cc/637CsKRC/pglive-allplots.gif)

# Crosshair #

Pglive comes with built-in Crosshair as well.

![Crosshair](https://i.postimg.cc/1z75GZLV/pglive-crosshair.gif)

# Axis #

To make life easier, pglive includes few axis improvements:

- Colored axis line using new `axisPen` attribute
- Time and DateTime tick format, converting timestamp into human readable format

![Crosshair](https://i.postimg.cc/8kr0L2YJ/pglive-axis.gif)

# Summary #

- With Pglive You've got easy Thread-safe implementation of fast Live plots.
- You can use all `kwargs` specified in pyqtgraph
- **Focus on Data Collection, not Data Plotting**