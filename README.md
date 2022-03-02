# Autokey Scripts for macOS Keyboard Shortcuts

If you regular switch between macOS and Linux you know the pain of your
muscle memory for common keyboard shortcuts not working. This is a
collection of scripts for Autokey that emulate macOS style keyboard
shortcuts in the Gnome and KDE desktop environment.

## Things That Don't Work

Copy and paste in terminals is particularly troublesome. We've added
workarounds for Gnome Terminal and Konsole, but other terminals like Tilix would
need exclusions added to work properly. Also if you use a tool with
a built-in terminal like VS Code, it is difficult to detect if you are
in the editor or in the terminal so copy/paste will currently work
only in the editor, not in the terminal.

In KDE some of the default shortcuts clash with these. You'll need to disable them in the KDE system settings.

At time of writing in Jan 2022 you need to be in a X11 session for autokey-gtk to work,  it doesn't yet support Wayland.

## Installation

First install Autokey `sudo apt install autokey-gtk` or `sudo dnf install autokey-gtk`. Then point your config to the git repo with `ln -s autokey-macos ~/.config/autokey/data/autokey-macos`.  If your autokey is not using `~/.config` it might be under `~/.local`.
