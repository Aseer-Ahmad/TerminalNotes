import datetime
import re
import os

def writeNote(basepath):
	print('\nBEGIN NOTES HERE [Write \'done\' to SAVE]\nTo save with filename [WRITE	\'done[_filename_]\'] \n=======================================')
	t = datetime.datetime.now()
	s = ''
	while True:
		print("> ", end = "")
		temp = str(input())
		if temp == 'done':
			break
		elif len(temp) > 4 and temp[:5] == 'done[':
			reg = r'\[.*\]'
			try:
				t = re.search(reg, temp).group()[1:-1]
				break
			except:
				t = None
				break			
		s += temp + '\n'
		
	_path = basepath + "/Notes/"+str(t) + ".txt"
	_path = _path.replace(' ', '_') 
	if t == None:
		#file name not found
		t = datetime.datetime.now()
		_path = basepath + "/Notes/"+str(t)+".txt"
		_path = _path.replace(' ', '_')
		print("\nSaving... at", _path, " {FILE_NAME NOT FOUND}\n")
	else:
		print("\nSaving... at", _path, "\n")

	with open( _path, 'w') as f:
		f.write(s)
		
def showAll(basepath):
	'''
	Improve later by filtering with time range(week, last month, last 3 months..etc)
	'''
	_path = basepath + "/Notes/"
	sl, f, c = 'SL', 'FILENAME', 'CONTENT'
	print(f'{sl: <4} {f: <35} {c}')
	for i, f in enumerate(os.listdir(_path), 1):
		with open(_path + f, 'r') as _file:
			content = _file.read()[:30].replace('\n', '')
		print(f'{str(i): <4} {f : <35} {content}')		
	print()
	
if __name__ == '__main__':
	#by KEYWORD <- display file names with the keyword
	#by CONTENT <- display file names along with a small excerpt from files
	#			   or display only a potion of file content 
	#by CONTENT <- give option to search content for [links/ all]
	base_path = '/'.join(os.getcwd().split('/')[:3]) 
	flag = True
	while flag:
		print('1. TAKE NOTE\n2. SHOW ALL \n3. SEARCH by CONTENT\n4. SEARCH by KEYWORD\n5. EXIT\n>>> ', end = "")
		try:
			n = int(input())
			if n == 1:
				writeNote(base_path)
			elif n == 2:
				showAll(base_path)
			else:
				flag = False
		except ValueError as e:
			print(e.__class__, "ENTER VALUE or EXIT!\n")			
			
			
			
			
