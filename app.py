from flask import Flask, render_template, request
from downloader import download_media
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    if not url:
        return "Please provide a URL"

    result = download_media(url)

    if result:
        return "Download completed successfully!"

    return "Download failed!"


if __name__ == "__main__":
    app.run(debug=True)
