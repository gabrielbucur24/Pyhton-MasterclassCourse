import webbrowser as wb

# wb.open("https://python.org", new=1)
# controller = wb.get()
# print(controller)
# help(wb)

chrome = wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://python.org')
# chrome.open_new_tab('https://python.org')
