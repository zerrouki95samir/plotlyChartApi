# Simple Flask App

This is a flask application to create 3d line chart based on the data/series sent with body request. 

### Prerequisites

if you want to run this app locally on your machine you need to have [python 3.*](https://www.python.org/downloads/release/python-379/) pre-installed on your OS.

### Run This project locally on your machine

After installing Python, you can follow this steps:

Clone this Repository on your machine, on your terminal/cmd.. :

```
git clone https://github.com/zerrouki95samir/plotlyChartApi.git
```
cd to plotlyChartApi directory:

```
cd plotlyChartApi
```

Install all the requirements packages:

```
pip install -r requirements.txt
```

Run the app:
```
flask run 
```

Or: 
```
python app.py
```

If everything goes well, you will see this line at the end of your command line!:  

```
Running on http://127.0.0.1:portxxxx/ (Press CTRL+C to quit)
```

## Running the tests

Now that our server is up and running, we need to do some testing, so we need to send a GET requests and send some data (x, y and x) series with the body to the root url of this app, I've already prepared some data for testing:
```
{
    "theme": "plotly_dark",
    "x": {
        "label": "This is X axis",
        "values": [2108.944355, 2487.365989, 3336.585802, 3429.864357, 4985.711467]
    },
    "y": {
        "label": "This is Y axis",
        "values": [56602560, 65551171, 76039390, 88049823, 100840058]
    }, 
    "z": {
        "label": "This is Z axis", 
        "values": [1952, 1957, 1962, 1967, 1972]
    }
}
```

### Break down into end to end tests

After requesting the app with the data above, you'll get an html response containing the required 3D line chart showing your data.
Or if you open your browser with the root link, you will see the chart that displayed your data.

## Built With

* [flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [plotly](https://plotly.com/) - is a python package whose purpose is to provide 3D line chart.

## Author

* **ZERROUKI SAMIR** - [zerrouki95samir](https://github.com/zerrouki95samir)
