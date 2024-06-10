import os
from flask import Flask, request, render_template
from utils import plot


app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():

    file_path = os.path.join(app.root_path,'./data', "Data.xlsx")
    plot_data = plot.create_plot_data(file_path)

    return render_template("/pages/home.html", plot_data=plot_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
