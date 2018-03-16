import os

directory = '/mnt/hgfs/shared/training_data/mov/MP4'


for filename in os.listdir(directory):
    if filename.endswith(".mov") or filename.endswith(".mp4"):
        file_name = os.path.join(directory, filename)
	stripped_name = os.path.basename(file_name).split('.')[0]
	output_name = directory+"/"+stripped_name+".wav"
	print("Converting "+filename)
	print("to "+output_name)
	os.system('ffmpeg -i %s -ar 16000 -ac 1 %s'%(file_name, output_name))
	continue
    else:
        continue
