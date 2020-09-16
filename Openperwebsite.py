import sys
import requests
import webbrowser


webbrowser.register('chrome', None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

pathFile=sys.argv[1]
numPageOpen=sys.argv[2]
numPageOpened=0

fh = open(pathFile,'r')
for line in fh:
    try:
        url = 'https://' + line.rstrip('\n')
        print(url + '---' + str(len(url)));
        r = requests.get(url,timeout=5)        
        if(r.status_code==200):
            #open chrome with location
            numPageOpened++
            webbrowser.get('chrome').open_new(url)
        else:
            print(line)
    except requests.ConnectionError:
        print(line + " --- failed to connect")
fh.close()

        
