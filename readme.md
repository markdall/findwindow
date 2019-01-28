# Find Window

I needed a way to find a window before using sendkey(s). It wasn't working well with what I had been using previously, and the only solution I could find required adding modules to every machine which means that it's brittle.

This code solves the problem I had.

[Set foreground window](https://programtalk.com/python-examples/ctypes.windll.user32.SetForegroundWindow/)

[Find a window](https://programtalk.com/python-examples/ctypes.windll.user32.FindWindowA/)

[Key code list](https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes)

[Massive list of code for ctypes and providing input.](https://stackoverflow.com/a/11910555)
