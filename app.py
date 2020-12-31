import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
@app.route('/', methods=["GET"])
def display3D_line():
    json_data = request.json
    theme = "none"
    if 'theme' in json_data:
        theme = json_data['theme']
    df = pd.DataFrame({
        json_data['x']['label']: json_data['x']['values'], 
        json_data['y']['label']: json_data['y']['values'], 
        json_data['z']['label']: json_data['z']['values']
    })
    config = {
        # Customizing Download Plot Button Options
        'toImageButtonOptions':{
            'width': 1000,
            'height': 1000,
            'format': 'svg', 
            'filename': 'line3D'
        }, 
        'displaylogo': False, 
        }
    fig = go.Figure()
    fig = px.line_3d(
            df, 
            x=json_data['x']['label'], # [2108.944355, 2487.365989, 3336.585802, 3429.864357, 4985.711467], 
            y=json_data['y']['label'], # [56602560, 65551171, 76039390, 88049823, 100840058], 
            z=json_data['z']['label'], # [1952, 1957, 1962, 1967, 1972],  
            template=theme,
            
        )
    fig.update_layout(
        #config=config, show_link=False
        margin=dict(t=0,r=0,b=0,l=0)
    )
    plot(fig, filename='./templates/line3D.html', config=config, show_link=False, auto_open=False)
    
    return render_template('line3D.html')


@app.route('/show-latest', methods=["GET"])
def show_latest():
    return send_from_directory('./templates/','line3D.html')
    #return render_template('line3D.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33508))
    app.run(host='0.0.0.0', port=port, debug=True)