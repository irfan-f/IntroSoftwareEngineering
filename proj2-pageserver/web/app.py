from flask import Flask, render_template, request, abort
import os
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.route('/<loc>')
def doit(loc=None):
    fileloc = "./templates/" + loc
    if '..' in loc or '~' in loc:
        abort(403)
    else:
        if loc.endswith(".html") or loc.endswith(".css"):
            if os.path.isfile(fileloc):
                return render_template(loc), 200
            else:
                abort(404)
        else:
           abort(403)

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
