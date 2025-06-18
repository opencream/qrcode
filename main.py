from flask import Flask, request, render_template, redirect, url_for
import os
import json

app = Flask(__name__)
DATA_DIR = "box_data"
os.makedirs(DATA_DIR, exist_ok=True)
@app.route("/")
def home():
    return redirect(url_for('box', box_id="box001"))

@app.route("/box/<box_id>", methods=["GET", "POST"])
def box(box_id):
    filepath = os.path.join(DATA_DIR, f"{box_id}.json")

    if request.method == "POST":
        data = {
            "description": request.form["description"],
            "date": request.form["date"],
            "time": request.form["time"],
            "contents": request.form["contents"]
        }

        with open(filepath, "w") as f:
            json.dump(data, f)
        return redirect(url_for('box', box_id=box_id))

    if os.path.exists(filepath):
        with open(filepath) as f:
            data = json.load(f)
    else:
        data = {"description": "", "date": "", "contents": ""}

    return render_template("box.html", box_id=box_id, data=data)

app.run(host="0.0.0.0", port=3000)
