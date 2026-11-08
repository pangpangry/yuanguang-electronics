from pathlib import Path

from flask import Flask, render_template, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"

app = Flask(
    __name__,
    static_folder=str(PUBLIC_DIR / "static"),
    static_url_path="/static",
    template_folder=str(PUBLIC_DIR),
)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/robots.txt")
def robots():
    return send_from_directory(PUBLIC_DIR, "robots.txt", mimetype="text/plain")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
