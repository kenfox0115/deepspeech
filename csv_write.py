import csv
import os

directory = ('/home/ken/deepspeech')
outfile = open('output.csv', 'wb')
writer = csv.writer(outfile)


for filename in os.listdir(directory):
	myfile = os.path.join(directory, filename)
	filesize = os.path.getsize(myfile)
	str_filesize = str(filesize)
	writer.writerow([("%s,%s"%(myfile, str_filesize))])
	continue
