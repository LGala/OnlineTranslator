from flask import Flask, render_template, request
from google_trans_new import google_translator

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")
    

@app.route("/translate_sentence",methods=["POST","GET"])
def translate_sentence():
    return google_translator().translate(request.form.get("sentence"),lang_tgt='en')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)