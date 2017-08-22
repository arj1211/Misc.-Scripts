import os
from time import strftime, gmtime

t = open(strftime("%Y%m%d_%H%M%S.txt",gmtime()),'w')

for filestr in os.listdir():
	if filestr.endswith('.txt') and filestr!=t.name:
		f = open(filestr,'r')
		#t.writelines(f.readlines())
		for i in f.readlines():
			t.write(i)
		f.close()
		t.write("\n~:\n")
		#os.remove(filestr)
t.close()
