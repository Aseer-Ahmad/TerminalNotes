import os

base_path = os.getcwd()
file_path = base_path + "/notes.py"
_path = '/'.join(base_path.split('/')[:3]) + "/bin"
os.mkdir(_path)
s = '#! /bin/sh\npython {}'.format(file_path)
with open(_path+"/note", 'w') as f:
	f.write(s)
