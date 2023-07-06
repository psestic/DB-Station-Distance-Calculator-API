# DB Station Distance Calculator API

### Description
This is a simple API that calculates the distance (as the crow flies) between any two stations in the Deutsche Bahn railway network and returns a JSON file of the form:

```
{
"from": <start_station>, 
"to": <end_station>,
"distance": <calculated_distance>,
"unit": "km"
}
```

At its core it uses a haversine algorithm. 
The haversine algorithm finds the great circle (i.e. a circle where the radius equals the earth radius) passing through any given start and end point. 
It then calculates the length that one needs to travel on the great circle from start to end.

### How to use it?

You can run this API locally as follows.

Assuming you have a current Python installation, first, make sure you have installed Pandas and Flask. 

1. ```python3 -m pip install pandas```
2. ```python3 -m pip install flask```

Then, while in the repository folder simply run the main.py.

3. ```python3 main.py```

Now, switch to your internet browser and go to ```localhost:50000```.
Here you will find further instructions as well as a table containing all available stations.

Try the following URL to get the distance between Frankfurt (Main) Hbf and Berlin Hbf.

```localhost:5000/api/v1/distance/FF/BLS```


### Technology used in this Project
- Python 3.11
- Pandas (for data processing)
- Flask (for API)
