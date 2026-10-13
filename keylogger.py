#!/usr/bin/env python3
"""
Task 04 — Simple Keystroke Logger Lab Demonstration
Demonstrates logging user input to a local file for educational purposes.
Supports both Tkinter GUI mode and a Terminal/CLI fallback mode.
"""

import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent / "keylog.txt"


def log_key_to_file(key_representation: str):
    """Append one event to the local log file."""
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    try:
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(f"{timestamp} - {key_representation}\n")
    except OSError as exc:
        print(f"[!] Error writing to log file: {exc}", file=sys.stderr)


# ==========================================
# Terminal / CLI Mode (Fallback)
# ==========================================
def run_cli_mode():
    """Interactive terminal mode when Tkinter is unavailable."""
    print("=" * 65)
    print("      Task 04 — Keystroke Logger (Terminal Mode)")
    print("=" * 65)
    print(f"[*] Log file location: {LOG_PATH}")
    print("[*] Type characters or words below to log them.")
    print("[*] Type ':quit' or press Ctrl+C to exit.\n")
    print("-" * 65)

    try:
        while True:
            user_input = input("Enter text > ")
            if user_input.strip() == ":quit":
                break
            for char in user_input:
                log_key_to_file(char if char != " " else "[SPACE]")
            log_key_to_file("[ENTER]")
            print(f"  [+] Logged {len(user_input)} character(s) + [ENTER] to keylog.txt")
    except (KeyboardInterrupt, EOFError):
        print("\n")

    print(f"\n[✓] Session ended. All logged entries saved to:\n    {LOG_PATH}\n")


# ==========================================
# Tkinter GUI Mode
# ==========================================
def run_gui_mode():
    """Runs the Tkinter GUI interface."""
    import tkinter as tk
    from tkinter import messagebox

    def format_key(event):
        """Convert Tkinter key events into readable log labels."""
        if event.keysym == "space":
            return "[SPACE]"
        if event.keysym == "Return":
            return "[ENTER]"
        if event.keysym == "BackSpace":
            return "[BACKSPACE]"
        if event.keysym == "Tab":
            return "[TAB]"
        if event.keysym == "Escape":
            return "[ESC]"
        if event.keysym in ("Shift_L", "Shift_R"):
            return "[SHIFT]"
        if event.keysym in ("Control_L", "Control_R"):
            return "[CTRL]"
        if event.keysym in ("Alt_L", "Alt_R"):
            return "[ALT]"
        if event.char and event.char.isprintable():
            return event.char
        return f"[{event.keysym.upper()}]"

    def log_key(event):
        """Handle Tkinter keypress events."""
        key = format_key(event)
        log_key_to_file(key)
        status_var.set(f"Recorded: {key}")

    def clear_test_field():
        test_entry.delete(0, tk.END)
        test_entry.focus_set()

    def show_log_location():
        messagebox.showinfo(
            "Log file",
            f"Keystroke log is saved locally at:\n{LOG_PATH}\n\n"
            "The log may contain whatever you type in the test field. "
            "Use test data only."
        )

    root = tk.Tk()
    root.title("Task 04 — Simple Keylogger Lab")
    root.geometry("650x360")
    root.minsize(560, 330)

    tk.Label(
        root,
        text="Simple Keylogger — Lab Demonstration",
        font=("Arial", 16, "bold")
    ).pack(pady=(18, 6))

    tk.Label(
        root,
        text="Type sample text in the box below. Only this field is monitored.",
        wraplength=560
    ).pack(pady=4)

    test_entry = tk.Entry(root, width=58, font=("Arial", 12))
    test_entry.pack(pady=12)
    test_entry.bind("<KeyPress>", log_key)

    status_var = tk.StringVar(value="Ready — logging starts when you type here.")
    tk.Label(root, textvariable=status_var, fg="navy").pack(pady=6)

    buttons = tk.Frame(root)
    buttons.pack(pady=10)

    tk.Button(buttons, text="Clear Test Field", command=clear_test_field).pack(
        side=tk.LEFT, padx=5
    )
    tk.Button(buttons, text="Show Log Location", command=show_log_location).pack(
        side=tk.LEFT, padx=5
    )
    tk.Button(buttons, text="Close", command=root.destroy).pack(
        side=tk.LEFT, padx=5
    )

    tk.Label(
        root,
        text="Ethics: use only with permission; never enter real passwords or private data.",
        wraplength=580,
        fg="darkred"
    ).pack(side=tk.BOTTOM, pady=14)

    test_entry.focus_set()
    root.mainloop()


def main():
    try:
        run_gui_mode()
    except (ImportError, ModuleNotFoundError) as err:
        print("\n" + "!" * 65)
        print("[!] Tkinter GUI could not be loaded:")
        print(f"    {err}")
        print("\n    On Arch Linux, Tkinter requires the 'tk' system package.")
        print("    To enable the GUI interface, install it with:")
        print("        sudo pacman -S tk")
        print("!" * 65 + "\n")
        print("[*] Launching Terminal/Console Mode instead...\n")
        run_cli_mode()


if __name__ == "__main__":
    main()
