"""
Chapter 61: Webbrowser Module
Parameter                                           Details
webbrowser.open()
url                                     the URL to open in the web browser
new                                     0 opens the URL in the existing tab, 1 opens in a new window, 2 opens in new tab
autoraise                               if set to True, the window will be moved on top of the other windows
webbrowser.open_new()
url                                     the URL to open in the web browser
webbrowser.open_new_tab()
url                                     the URL to open in the web browser
webbrowser.get()
using                                   the browser to use
webbrowser.register()
url                                     browser name
constructor                             path to the executable browser (help)
instance                                An instance of a web browser returned from the webbrowser.get() method

According to Python's standard documentation, the webbrowser module provides a high-level interface to allow
displaying Web-based documents to users.

Section 61.1: Opening a URL with Default Browser

Section 61.2: Opening a URL with Dierent Browsers
The webbrowser module also supports different browsers using the register() and get() methods. The get
method is used to create a browser controller using a specific executable's path and the register method is used to
attach these executables to preset browser types for future use, commonly when multiple browser types are used.

"""

import webbrowser


#Section 61.1: Opening a URL with Default Browser
print("--------Section 61.1: Opening a URL with Default Browser-------")

webbrowser.open("http://stackoverflow.com")
webbrowser.open_new("http://stackoverflow.com")
webbrowser.open_new_tab("http://stackoverflow.com")

#Section 61.2: Opening a URL with Dierent Browsers
print("-------Section 61.2: Opening a URL with Different Browsers---------")
path = "C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe"
#ff_path = webbrowser.get("C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe")
#ff = webbrowser.get(ff_path)
webbrowser.register('iexplore', None, webbrowser.BackgroundBrowser(path),1)
webbrowser.get('iexplore').open_new_tab("http://stackoverflow.com/")
#ff.open("http://stackoverflow.com/")
