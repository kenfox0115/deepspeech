import csv
import os

directory = ('/home/ken/deepspeech')
outfile = open('output.csv', 'wb')
writer = csv.writer(outfile, delimiter=',', quotechar='"', escapechar='\\', quoting=csv.QUOTE_NONE)


for filename in os.listdir(directory):
	myfile = os.path.join(directory, filename)
	#print(myfile)
	filesize = os.path.getsize(myfile)
	#print(filesize)
	str_filesize = str(filesize)
	#print(str_filesize)
	writer.writerow([("%s,%s"%(myfile, str_filesize))])
	#print([("%s,%s"%(myfile, str_filesize))])
	continue
