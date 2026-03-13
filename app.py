from flask import Flask,render_template,request
import os
import analyzer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def upload():
    file=request.files["file"]
    path=os.path.join("uploads","data.csv")
    file.save(path)
    result=analyzer.analyze_csv(path)
    return render_template("result.html",result=result)


if __name__ == "__main__":
    app.run(debug=True)