# PhishGuard — ML-Based Phishing URL Detection System

A small academic demonstration interface that calls the installed `fraudurl` command-line detector. It displays the returned verdict, reported phishing probability, and reasons.

## Requirements

- Python 3.9+
- `pipx`-installed `fraudurl` command
- Flask (installed in a project virtual environment)

## Run on Arch Linux

```bash
cd phishing_url_detection
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

If Flask cannot find the detector, specify its path:

```bash
FRAUDURL_BIN=/home/Ansh/.local/bin/fraudurl python app.py
```

## How it works

1. The user enters a complete `http://` or `https://` URL.
2. Flask validates the basic URL format.
3. Flask calls `fraudurl --url <URL> --quiet` as a subprocess.
4. The interface displays the JSON result returned by the detector.

The application does not itself visit or fetch the submitted URL. The default detector mode analyzes URL text offline.

## Important project note

This is a frontend/integration project using the existing pretrained `fraudurl` model. It does not train a new model. Describe this accurately in the college report. The verdict is a screening signal, not a guarantee that a URL is safe or malicious.

## Run locally only

The Flask development server binds to `127.0.0.1`. Do not expose it to the public internet as-is.
