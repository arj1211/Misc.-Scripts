def dank_space(s1,s2):
	s1=list(s1)
	s2=list(s2)
	# s1 spaces increase after each letter
	# s2 spaces decrease after each letter
	out1=''
	out2=''
	spaces1=0
	spaces2=(len(s2)-2)
	for c in s1:
		out1+=c+' '*spaces1
		spaces1+=1
	for d in s2:
		out2+=d+' '*spaces2
		spaces2-=1
	print(out1+' '*(len(s1)+len(s2))+out2)
while 1:
    s1,s2=input('two words seperated by whitespace:\n').split()
    dank_space(s1,s2)
