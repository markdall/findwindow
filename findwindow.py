"""Locate a Window by title."""
import ctypes
from ctypes import wintypes
import time

FindWindow = ctypes.windll.user32.FindWindowW
AppActivate = ctypes.windll.user32.SetForegroundWindow

FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindow.restype = wintypes.HWND


def find_window(title):
    """Find a window by title, returns hwnd."""
    return FindWindow(None, title)


def app_activate(title):
    """Bring window to foreground."""
    hwnd = find_window(title)
    if hwnd:
        AppActivate(hwnd)
        return True
    else:
        print("Couldn't find " + title + ".")
        return False


def close_window():
    """Close the current top-most window."""
    alt_key = 0x12  # See readme.md.
    f4_key = 0x73  # See readme.md.
    key_down(alt_key)
    key_down(f4_key)
    key_up(f4_key)
    key_up(alt_key)


def key_down(virtual_key_code):
    """Simulate pressing a key down."""
    ctypes.windll.user32.keybd_event(virtual_key_code, 0, 0, 0)


def key_up(virtual_key_code):
    """Simulate releasing a key."""
    ctypes.windll.user32.keybd_event(virtual_key_code, 0, 0x0002, 0)

if __name__ == "__main__":
    app_activate("blah")
    time.sleep(1)
    close_window()
    pass
