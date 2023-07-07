import pandas as pd
from flask import Flask, render_template, jsonify, json
from functions import haversine

# file with station data
FILEPATH = "D_Bahnhof_2020_alle.csv"

# pre-process the station data
stations = pd.read_csv(FILEPATH, decimal=',', sep=";")
stations = stations.loc[stations["Verkehr"] == "FV"]
stations = stations[["DS100", "NAME", "Laenge", "Breite"]]

# handle special characters (ä,ö,ü,ß) in JSON
json.provider.DefaultJSONProvider.ensure_ascii = False

# create Flask instance
app = Flask("__name__")


# create a documentation page
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


# create API
@app.route("/api/v1/distance/<start>/<end>")
def api(start: str, end: str):
    # get station names
    start_name = stations.loc[stations["DS100"] == start]["NAME"].squeeze()
    end_name = stations.loc[stations["DS100"] == end]["NAME"].squeeze()

    # get station coordinates
    lon_start = stations.loc[stations["DS100"] == start]["Laenge"].squeeze()
    lat_start = stations.loc[stations["DS100"] == start]["Breite"].squeeze()
    lon_end = stations.loc[stations["DS100"] == end]["Laenge"].squeeze()
    lat_end = stations.loc[stations["DS100"] == end]["Breite"].squeeze()

    # compute distance between stations
    distance = haversine(lon_start, lat_start, lon_end, lat_end)
    rounded_distance = round(distance)
    data = {
                "from": start_name,
                "to": end_name,
                "distance": rounded_distance,
                "unit": "km"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
