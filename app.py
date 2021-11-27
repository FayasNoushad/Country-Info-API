from flask import Flask, redirect, render_template, request, jsonify, json
from countryinfo import CountryInfo


app = Flask(__name__, template_folder="public")


@app.route("/")
def main():
    if request.args.get('query'):
        query = request.args.get('query')
    else:
        return render_template("index.html")
    country = CountryInfo(query)
    info = country.info()
    if info is not None:
        return jsonify(info)
    else:
        return "Something wrong"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
