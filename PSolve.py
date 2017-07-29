'''

Use the 'perm' function, the 'compare' one is internally used.

the one and only parameter you should give to 'perm' is a string to be permuted

'''
def compare(string,orig,length):
    #if ''.join(sorted(string)) == ''.join((sorted(orig))[:length]):
    if sorted(string) == sorted(orig)[:length]:
        return True
    return False

def perm(c_list=['a','b','c'],length=0,s='',counter=0):

    if length is 0:
        length=len(c_list)

    if counter>length:
        return
    if compare(s,c_list,length):
        print(s)
        return
    for i in c_list:
        perm(c_list,length,s+i,counter+1)

