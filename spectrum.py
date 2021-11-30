import numpy as np
import plotly.express as px


alpha = 10
beta = 3


# Start frequency
# End frequency
f_start = 1000
f_end = 2000

x = np.linspace(f_start, f_end, 1000)
y = np.cos(alpha * np.exp(beta * (x - f_start) / (f_end - f_start)))
fig = px.line(x=x, y=y)
fig = fig.update_layout(height=200)
fig = fig.update_xaxes(title="Frequency (Hz)")
fig = fig.update_yaxes(visible=False)
fig.update_yaxes(range=[-2, 2])
