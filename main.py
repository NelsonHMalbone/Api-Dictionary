from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def defination(word, definition):
    filename = "dictionary.csv"
    df = pd.read_csv(filename)
    dictionary_word = df.loc[word]
    dictionary = df.loc[definition]
    result_dictionary = {'Defination': dictionary,
                         'word': dictionary_word}
    return result_dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)
