import datetime
import re
import os

def writeNote(basepath):
	print('\nBEGIN NOTES HERE [Write \'done\' to SAVE / \'discard\' to delete]\nTo save with filename [WRITE done<space>filename]\n=============================================================')
	t = datetime.datetime.now()
	s = ''
	while True:
		print("> ", end = "")
		temp = str(input())
		
		if temp == 'done':
			saveNote(basepath, s, t)
			break
		elif len(temp) > 4 and temp[:5] == 'done ':
			reg = r'\[.*\]'
			try:
				t = temp[5: ]#re.search(reg, temp).group()[1:-1]
				t = t.lstrip()
				if t == '':
					t = None
				saveNote(basepath, s, t)
				break
			except:
				t = None
				saveNote(basepath, s, t)
				break	
		elif temp == 'discard' and len(temp) == 7:
			print('\nNote Discarded!\n')
			break
			
		s += temp + '\n'	
	
def saveNote(basepath, s, t):
	_path = basepath + "/Notes/"+str(t) + ".txt"
	_path = _path.replace(' ', '_') 
	if t == None:
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
	Add infinite loop for reading whole content
	
	Also previewing memo, give option to append to it
	Take note but unlike an individual one , take it in a group
	'''
	_path = basepath + "/Notes/"
	sl, f, c = 'Sl.', 'FILENAME', 'CONTENT'
	print(f'{sl: <4}| {f: <35}| {c}')
	print('-'*90)
	for i, f in enumerate(os.listdir(_path), 1):
		with open(_path + f, 'r') as _file:
			content = _file.read()[:50].replace('\n', '')
		print(f'{str(i): <4} {f : <35} {content}')		
	
	flag = True
	file_name_to_delete = ''
	while flag:	
		print(f"\nWrite Sl no. to read a MEMO, 0 for main menu >>> ", end = "")
		n = eval(input())
		for i, f in enumerate(os.listdir(_path), 1):
			if n == i:
				file_name_to_delete = f
				print(f'Reading from [{f}]\n')
				readFile(_path + f)	
		if n > i:
			print('Invalid serial no.')
		if n == 0:
			flag = False
			
def readFile(_path):
	with open(_path, 'r') as f:
		print(f.read().strip())
	
if __name__ == '__main__':
	#by FILENAME <- display file names with the search keyword
	#by CONTENT <- give option to search content for [links/ all]
	# to delete
	base_path = '/'.join(os.getcwd().split('/')[:3]) 
	flag = True
	while flag:
		print('1. TAKE NOTE\n2. SHOW ALL \n3. SEARCH by CONTENT\n4. SEARCH by KEYWORD\n5. DELETE\n6. EXIT\n>>> ', end = "")
		try:
			n = int(input())
			if n == 1:
				writeNote(base_path)
			elif n == 2:
				showAll(base_path)
			else:
				flag = False
		except ValueError as e:
			print(e.__class__, "ENTER CORRECT No. or EXIT!\n")			
			
					
