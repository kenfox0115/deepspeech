import os
import csv

directory = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(directory):
    if filename.endswith(".mov") or filename.endswith(".py"): 
        file_name = os.path.join(directory, filename)
	file_size = os.path.getsize(file_name)
        print("Converting "+file_name+str(file_size))
        #print("to "+output_name)
        #os.system('ffmpeg -i %s -ar 16000 -ac 1 %s'%(file_name, output_name))
        continue
    else:
        continue

