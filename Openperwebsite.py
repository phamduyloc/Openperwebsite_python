import sys
import os
import webbrowser
import requests

pathfile = sys.argv[1]
numPageOpen = int(sys.argv[2])

#Open new tab firefox voi url la url
def openwebsite(url):
	#webbrowser.get('firefox').open_new_tab(url)
	webbrowser.get('google-chrome').open_new_tab(url)


if not os.path.isfile(pathfile):
	print("File path {} does not exist. Exiting ...".format(pathfile))
	sys.exit()

try:
	strArt = '''
       	                                                                               $$$$$      
    	                                                                               $:::$      
	555555555555555555      000000000          000000000          000000000        $$$$$:::$$$$$$ 
	5::::::::::::::::5    00:::::::::00      00:::::::::00      00:::::::::00    $$::::::::::::::$
	5::::::::::::::::5  00:::::::::::::00  00:::::::::::::00  00:::::::::::::00 $:::::$$$$$$$::::$
	5:::::555555555555 0:::::::000:::::::00:::::::000:::::::00:::::::000:::::::0$::::$       $$$$$
	5:::::5            0::::::0   0::::::00::::::0   0::::::00::::::0   0::::::0$::::$            
	5:::::5            0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0$::::$            
	5:::::5555555555   0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0$:::::$$$$$$$$$   
	5:::::::::::::::5  0:::::0 000 0:::::00:::::0 000 0:::::00:::::0 000 0:::::0 $$::::::::::::$$ 
	555555555555:::::5 0:::::0 000 0:::::00:::::0 000 0:::::00:::::0 000 0:::::0   $$$$$$$$$:::::$
	            5:::::50:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0            $::::$
	            5:::::50:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0            $::::$
	5555555     5:::::50::::::0   0::::::00::::::0   0::::::00::::::0   0::::::0$$$$$       $::::$
	5::::::55555::::::50:::::::000:::::::00:::::::000:::::::00:::::::000:::::::0$::::$$$$$$$:::::$
	 55:::::::::::::55  00:::::::::::::00  00:::::::::::::00  00:::::::::::::00 $::::::::::::::$$ 
	   55:::::::::55      00:::::::::00      00:::::::::00      00:::::::::00    $$$$$$:::$$$$$   
	     555555555          000000000          000000000          000000000           $:::$       
	                                                                                  $$$$$       
	'''

	print(strArt)
	print("\n\n")
	countLine = 0
	fp = open(pathfile,'r')
	numPageOpened = 0

	for line in fp:		
		countLine=countLine+1
		if (numPageOpened == numPageOpen):
			numPageOpened = 0
			print("\n\n\n")
			#print("Opened: " + str(opened))
			programPause = raw_input("Press the <ENTER> key to continue...")
			os.system("clear")
			print(strArt)			
		else:			
			try:
				url = 'http://' + line.rstrip('\n')
				r = requests.get(url,timeout=5)        
				if(r.status_code==200):
					openwebsite(line)
					numPageOpened = numPageOpened + 1												
				else:
					print(line.rstrip('\n') + ' --- ' + str(countLine));			
			except:
				print(line.rstrip('\n') + ' --- ' + str(countLine));
finally:
	fp.close()

