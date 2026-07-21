from flask import Flask, render_template, request, send_file
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
        return "No URL provided"

    # Downloader logic will be added here

    return f"Download request received: {url}"


if __name__ == "__main__":
    app.run(debug=True)
