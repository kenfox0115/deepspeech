import csv
import os

directory = ('/mnt/hgfs/shared/training_data/wav')
outfile = open('dts_traning.csv', 'wb')
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
