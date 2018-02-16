import os
import ffmpy

directory = '/mnt/hgfs/shared'


for filename in os.listdir('/mnt/hgfs/shared'):
    if filename.endswith(".mov") or filename.endswith(".mp4"): 
        file_name = os.path.join(directory, filename)
	print("Converting "+file_name)
	ff = ffmpy.FFmpeg(
		inputs={file_name: None},
		outputs={'output.avi': None}
	)
	ff.run()
	continue
    else:
        continue
