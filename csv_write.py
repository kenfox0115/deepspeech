import csv
import os

directory = ('/home/ken/deepspeech')
outfile = open('output.csv', 'wb')
writer = csv.writer(outfile, delimiter=',', quotechar='"', escapechar='\\', quoting=csv.QUOTE_NONE)


for filename in os.listdir(directory):
	myfile = os.path.join(directory, filename)
	filename = str(myfile)
	filesize = os.path.getsize(myfile)
	str_filesize = str(filesize)
	row = [filename, str_filesize]
	writer.writerow(row)
	print('Wrote'+str(row))
	continue
