import os
import ffmpy

directory = '/mnt/hgfs/shared'


for filename in os.listdir('/mnt/hgfs/shared'):
    if filename.endswith(".mov") or filename.endswith(".mp4"): 
        file_name = os.path.join(directory, filename)
	stripped_name = os.path.basename(file_name).split('.')[0]
	output_name = stripped_name+".wav"
	print("Converting "+filename)
	print("to "+output_name)
	os.system('ffmpeg -i %s -ar 16000 -ac 1 %s'%(file_name, output_name))
	#ff = ffmpy.FFmpeg(
	#	inputs={file_name: None},
	#	outputs={output_name: '-ar 16000, -ac 1'}
	#)
	#ff.run()
	continue
    else:
        continue
