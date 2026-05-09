# minecraft-username-checker
Bulk Minecraft username availability checker using the Mojang API
# Minecraft Username Checker

A lightweight Python tool for checking Minecraft username availability using the Mojang API.

The script reads usernames from a text file, checks whether they are taken, and saves all available usernames to an output file.

---

## Features

- Bulk username checking
- Fast and lightweight
- Saves available usernames automatically
- Simple setup and usage

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/minecraft-username-checker.git
cd minecraft-username-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Add usernames to `usernames.txt`:

```text
example1
example2
example3
```

Run the script:

```bash
python main.py
```

---

## Output

Available usernames will be written to:

```text
output.txt
```

Example console output:

```text
steve is a taken username.
coolname123 is not a taken username.
```

---

## Project Structure

```text
minecraft-username-checker/
│
├── main.py
├── usernames.txt
├── output.txt
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Requirements

- Python 3.10+
- Internet connection
- Mojang Python package

---

## Disclaimer

This project is unofficial and is not affiliated with Mojang Studios or Microsoft.
