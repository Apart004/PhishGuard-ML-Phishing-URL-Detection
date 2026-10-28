import json
import os
import shutil
import subprocess
from urllib.parse import urlparse

from flask import Flask, render_template, request

app = Flask(__name__)

# pipx normally places the executable here. Override with FRAUDURL_BIN if needed.
FRAUDURL_BIN = os.environ.get("FRAUDURL_BIN") or shutil.which("fraudurl") or os.path.expanduser("~/.local/bin/fraudurl")


def validate_url(value: str):
    value = (value or "").strip()
    if not value:
        return None, "Enter a URL to check."
    if len(value) > 2048:
        return None, "The URL is too long."
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return None, "Enter a complete URL starting with http:// or https://."
    return value, None


def analyze_url(url: str):
    if not os.path.isfile(FRAUDURL_BIN) and not shutil.which(FRAUDURL_BIN):
        raise RuntimeError(
            "Could not find the fraudurl executable. Check that pipx installed it "
            "and set FRAUDURL_BIN to its full path if necessary."
        )

    completed = subprocess.run(
        [FRAUDURL_BIN, "--url", url, "--quiet"],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if completed.returncode != 0:
        message = (completed.stderr or completed.stdout or "Detector failed.").strip()
        raise RuntimeError(message[:500])

    # fraudurl emits one JSON object for a single --url check.
    try:
        result = json.loads(completed.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        raise RuntimeError("The detector returned an unexpected response.")

    if result.get("error"):
        raise RuntimeError(str(result["error"]))
    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    submitted_url = ""

    if request.method == "POST":
        submitted_url = request.form.get("url", "").strip()
        validated_url, error = validate_url(submitted_url)
        if not error:
            try:
                result = analyze_url(validated_url)
            except (RuntimeError, subprocess.TimeoutExpired, OSError) as exc:
                error = f"Detection could not be completed: {exc}"

    return render_template(
        "index.html",
        result=result,
        error=error,
        submitted_url=submitted_url,
    )


if __name__ == "__main__":
    # Local demonstration server only. Do not expose the Flask development server publicly.
    app.run(host="127.0.0.1", port=5000, debug=False)
