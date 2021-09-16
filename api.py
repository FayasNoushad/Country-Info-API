# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Country-Info-API/blob/main/LICENSE

from flask import Flask, redirect, request, jsonify, json
from countryinfo import CountryInfo


app = Flask(__name__)


@app.route("/")
def main():
    if request.args.get('query'):
        query = request.args.get('query')
    else:
        return redirect("https://github.com/FayasNoushad/Country-Info-API")
    country = CountryInfo(query)
    info = country.info()
    if info is not None:
        info["google"] = "https://www.google.com/search?q=" + info["name"].replace(" ", "+")
        return jsonify(info)
    else:
        return "Something wrong"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)