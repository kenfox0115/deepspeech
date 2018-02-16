import os
directory = '/mnt/hgfs/shared'


for filename in os.listdir('/mnt/hgfs/shared'):
    if filename.endswith(".mov") or filename.endswith(".py"): 
        file_name = os.path.join(directory, filename)
	print("Converting "+file_name)
        continue
    else:
        continue
