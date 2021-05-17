from flask import Flask,render_template
import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pandas import Series
import numpy as np
import json
from datetime import datetime

app = Flask(__name__)

df=pd.read_csv('python_lib.csv')
foretell = df
foretell['month']=pd.to_datetime(foretell['month'])
df_java = df.iloc[:96,[0,2]]
df_java.set_index('month',inplace=True)

def create_plot():
    fig = go.Figure()
    print(df_java.head(10))
    fig.add_trace(go.Scatter(x= df_java.index, y= df_java['java'],
                        mode='lines+markers',
                        name='lines'))
    fig.update_xaxes(type='category')
    #fig.update_yaxes(tick0=200, dtick=100)
    fig.update_layout(title_text= 'JAVA')
    fig.update_xaxes(title_text= 'month')
    fig.update_yaxes(title_text= 'java')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/')
def index():
    bar = create_plot()

    return render_template('graphs_plot.html',plot1 = bar)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True)