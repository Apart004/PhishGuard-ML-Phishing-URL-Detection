# PhishGuard — ML-Based Phishing URL Detection System

PhishGuard is a college mini project that provides a web interface for analyzing potentially suspicious URLs.

Users enter a URL, and the application displays the detector's verdict, estimated phishing probability, and explanatory reasons.

**Project type:** Academic mini project  
**Frontend:** HTML, CSS  
**Backend:** Python, Flask  
**Detection engine:** `fraudurl` pretrained ML-based URL detector

> **Important:** This project integrates an existing pretrained detection model. Our application does not train a new ML model. Predictions are estimates and are not guarantees that a URL is safe or malicious.

---

## 1. What You Need Before Starting

You need:

- A Windows, macOS, or Linux computer.
- An internet connection for the initial setup.
- Python installed on your computer.
- Git installed on your computer.
- A terminal application.
- A web browser such as Chrome, Firefox, Safari, or Edge.

You do not need a GPU, database, or paid software.

## 2. Download the Project

Open the terminal application for your operating system.

**Windows:** Open PowerShell or Windows Terminal.

**macOS:** Open Terminal using Spotlight Search.

**Linux:** Open your usual terminal application.

Check whether Git is installed:

```bash
git --version
```

If a version number appears, Git is installed.

If Git is missing:

- **Windows:** Install Git from https://git-scm.com/downloads/win
- **macOS:** Install Apple's command-line tools by running `xcode-select --install`, or install Git from https://git-scm.com/downloads/mac
- **Linux:** Install Git using your distribution's package manager.

Now download the project:

```bash
git clone https://github.com/Apart004/PhishGuard-ML-Phishing-URL-Detection.git
```

Enter the downloaded project folder:

```bash
cd PhishGuard-ML-Phishing-URL-Detection
```

You should see files and folders including:

```text
PhishGuard-ML-Phishing-URL-Detection/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── .gitignore
```

If you already downloaded the repository, do not clone it again. Open a terminal in the existing project folder.

---

## 3. Install Python

Check whether Python is already installed.

### Windows

Open PowerShell and run:

```powershell
py --version
```

If that command is unavailable, try:

```powershell
python --version
```

If neither works, install Python from:

https://www.python.org/downloads/windows/

During installation, enable **Add Python to PATH** if the installer offers that option.

Close and reopen PowerShell after installation.

### macOS

Run:

```bash
python3 --version
```

If Python is missing, install it from:

https://www.python.org/downloads/macos/

Alternatively, macOS users who already use Homebrew can install Python with:

```bash
brew install python
```

### Linux

Run:

```bash
python3 --version
```

If Python or its virtual-environment support is missing, install it using your Linux distribution's package manager.

**Recommendation:** Python 3.11 or 3.12 is a reasonable starting choice for this project. Use a supported Python version if a dependency does not work with your existing installation.

---

## 4. Create a Virtual Environment

A virtual environment keeps the project's Python packages separate from other applications on your computer.

Make sure your terminal is inside the project folder before continuing.

### Windows — PowerShell

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

Alternatively, use this in PowerShell for the current terminal session if permitted by your system:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Arch Linux, if creating the virtual environment fails, install the appropriate Python and virtual-environment packages through `pacman`.

### Verify activation

Your terminal prompt will usually display `(.venv)` after activation.

You must activate the environment again whenever you open a new terminal to work on the project.

---

## 5. Install the Project Requirements

With the virtual environment activated, run:

### Windows

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS and Linux

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The `requirements.txt` file installs the dependencies needed by the project:

- **Flask:** Runs the web application and handles requests.
- **fraudurl:** Provides the pretrained URL detection engine and its command-line interface.

Wait for installation to finish. An internet connection is required to download the packages.

Verify that the detector is available:

```bash
fraudurl --version
```

If the version command is unsupported by your installed package, check the command's availability instead:

**Windows:**

```powershell
Get-Command fraudurl
```

**macOS and Linux:**

```bash
fraudurl --help
```

If the detector cannot be found, confirm that the virtual environment is activated and rerun the requirements installation command.

---

## 6. Run PhishGuard

Keep the virtual environment activated and make sure you are inside the project folder.

Run:

```bash
python app.py
```

The terminal should report that the Flask development server is running at:

```text
http://127.0.0.1:5000
```

Open that address in your browser:

**http://127.0.0.1:5000**

You should see the PhishGuard interface.

1. Enter a complete URL starting with `http://` or `https://`.
2. Click **Analyze URL**.
3. Wait for the detector to finish.
4. Review the verdict, estimated probability, and explanatory reasons.

Keep the terminal open while using the application. Closing it stops the server.

To stop the application, return to the terminal and press **Ctrl+C**.

---

## 7. Test the Application

You can try the following demonstration URLs:

| URL | Purpose |
|---|---|
| `https://github.com` | Example of a familiar website |
| `https://wikipedia.org` | Another familiar website |
| `http://paypal.com.secure-login.test/webscr/login.php` | Deliberately suspicious example for testing |

The suspicious example imitates a brand name in its subdomain and includes login-related terms.

The detector's verdicts can vary by input and model version. Do not assume that every legitimate URL will be marked `LEGITIMATE` or that every malicious URL will be detected.

**Safety note:** PhishGuard analyzes the submitted URL text in its default offline mode. It does not need to open the destination website. Do not visit suspicious URLs just to test them.

---

## 8. Run Detection Directly in the Terminal

You can also use the detector without opening the web interface.

With the virtual environment activated, run:

```bash
fraudurl --url "https://wikipedia.org"
```

For structured JSON output:

```bash
fraudurl --url "https://wikipedia.org" --quiet
```

To test the suspicious demonstration URL:

```bash
fraudurl --url "http://paypal.com.secure-login.test/webscr/login.php" --quiet
```

The output includes the detector's verdict, reported probability, and reasons.

---

## 9. Troubleshooting

### Error: `python` or `python3` is not recognized

Python may not be installed or available in your PATH.

Install Python using the instructions in Section 3, then open a new terminal.

### Error: `No module named flask`

Activate the virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

### Error: `fraudurl` command not found

Activate the virtual environment and reinstall the dependencies:

```bash
python -m pip install -r requirements.txt
```

Check that the detector is available:

```bash
fraudurl --help
```

If the command still cannot be found, ask your AI assistant to help diagnose the operating system, virtual environment, and package installation. Include the full error message.

### Error: PowerShell cannot activate `.venv`

Use Command Prompt and run:

```cmd
.venv\Scripts\activate.bat
```

Then install the requirements and start the app as described above.

### Error: Port 5000 is already in use

Another process may already be using the port. Stop the other application or ask your AI assistant for operating-system-specific steps to identify the process safely.

### The webpage opens, but URL analysis fails

The Flask interface and detection engine are separate components. Check that:

1. The virtual environment is active.
2. `fraudurl --help` works in the same terminal.
3. The dependencies installed without errors.
4. The terminal output does not contain a detector error.

Copy the full error message into your AI assistant for help.

---

## 10. How the Project Works

1. The user enters a URL in the HTML interface.
2. Flask receives the submitted URL and checks its basic format.
3. Flask invokes the `fraudurl` command-line detector.
4. The pretrained detector analyzes URL characteristics and produces a result.
5. Flask passes the result to the HTML template.
6. The browser displays the verdict, estimated probability, and explanatory reasons.

The project has three main parts:

- **Frontend:** HTML and CSS provide the interface.
- **Backend:** Python and Flask process requests and invoke the detector.
- **Detection engine:** The existing pretrained ML-based package performs URL analysis.

The detector's underlying model was trained by its original developer. Our project integrates it into a web interface; it does not train a new model.

---

## 11. Common Questions

**Do I need to download a dataset?**

No. The current application uses the pretrained detector and does not train a model from a dataset on your computer.

**Does it work on Windows and macOS?**

The project is designed to run locally with Python and its dependencies. Installation commands differ by operating system. If a dependency or command behaves differently on your system, troubleshoot that specific issue before presenting.

**Do I need to keep the internet connected?**

You need internet access to clone the repository and install dependencies. The default detection mode analyzes URL text offline, so the detector does not need to visit the submitted website.

**Does the project guarantee that a URL is safe?**

No. Its verdict is a screening signal. A prediction can be incorrect, and a `REVIEW` result means the detector is uncertain under its decision rules.

**Can I use it as a public website?**

This project is configured for a local demonstration. The Flask development server is not intended to be exposed directly to the public internet.

---

## 12. Official Project Links

- **GitHub repository:** https://github.com/Apart004/PhishGuard-ML-Phishing-URL-Detection
- **Python downloads:** https://www.python.org/downloads/
- **Git downloads:** https://git-scm.com/downloads
- **Flask documentation:** https://flask.palletsprojects.com/
- **Pretrained detector documentation:** https://github.com/amruth112/fraudurl-detector

## 13. Need Help Installing It?

If you get stuck, copy the prompt below into ChatGPT or another AI assistant.

> I am trying to install and run the PhishGuard ML-Based Phishing URL Detection System from this GitHub repository:
>
> https://github.com/Apart004/PhishGuard-ML-Phishing-URL-Detection
>
> I am a beginner. Please guide me one step at a time for my operating system: Windows, macOS, or Linux.
>
> The project uses Python, Flask, and the `fraudurl` package. It has `app.py`, `requirements.txt`, `templates/`, and `static/`.
>
> Help me install the required software, clone the repository, create and activate a virtual environment, install dependencies, verify that the detector command works, start the Flask application, and open `http://127.0.0.1:5000`.
>
> Do not assume I have prior terminal or programming knowledge. Give me the exact commands for my operating system, explain briefly where to run each command, and wait for my output before moving to the next step. If something fails, troubleshoot the actual error rather than restarting the entire installation.
>
> Do not claim that this project trains a new ML model; it integrates an existing pretrained detector.

---

**End of README**
