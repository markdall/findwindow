"""Locate a Window by title."""
import ctypes
from ctypes import wintypes

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

if __name__ == "__main__":
    app_activate("tabsvc")
    pass
