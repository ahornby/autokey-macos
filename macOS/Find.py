key = "f"
wcl = window.get_active_class()
if not (wcl == "gnome-terminal-server.Gnome-terminal" or wcl == "konsole.konsole"):
    keyboard.send_keys("<ctrl>+" + key)
else:
    keyboard.send_keys("<ctrl>+<shift>+" + key)
