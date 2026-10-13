# Prodigy Infotech CS Internship — Task 04
## Simple Keylogger (Consent-Based Demonstration)

### Objective
Demonstrate keyboard event handling and writing captured key events to a local text file.

### Features
- Captures keys typed only in the application's test input field.
- Labels common special keys, including Space, Enter, Backspace, Tab, Shift, Ctrl, and Alt.
- Adds a timestamp to each recorded event.
- Saves logs to `keylog.txt` beside the Python script.
- Provides a visible interface and a log-location message.

### Requirements
- Python 3
- Tkinter (usually included with Python; on Arch Linux install it with `sudo pacman -S tk`)

### Run on Linux
```bash
python3 --version
python3 keylogger_lab.py
```

Type non-sensitive sample text into the input box. Close the app when finished.
Then inspect the log:
```bash
cat keylog.txt
```

### Example log
```text
2026-10-13 14:20:01 IST - H
2026-10-13 14:20:01 IST - i
2026-10-13 14:20:02 IST - [SPACE]
2026-10-13 14:20:03 IST - [ENTER]
```

### How it works
1. Tkinter creates a visible test input field.
2. The `<KeyPress>` event binding calls `log_key()` when a key is pressed in that field.
3. `format_key()` turns the event into a readable character or special-key label.
4. Python appends the timestamp and key label to `keylog.txt`.

### Ethical considerations
- Obtain explicit permission before any monitoring experiment.
- This demonstration monitors only its own test field; it does not capture system-wide input.
- Never enter passwords, payment details, or other sensitive information.
- Keep the log private and delete it when it is no longer needed.
- Do not deploy keyloggers on another person's device without clear authorization.

### Limitations
This is a controlled demonstration, not a system-wide monitoring tool. Key names and keyboard layout behavior can vary by platform.
