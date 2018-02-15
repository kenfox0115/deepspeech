import os
directory = '/mnt/hgfs/shared'


for filename in os.listdir('/mnt/hgfs/shared'):
    if filename.endswith(".mov") or filename.endswith(".py"): 
        print("Converting "+os.path.join(directory, filename))
        continue
    else:
        continue
