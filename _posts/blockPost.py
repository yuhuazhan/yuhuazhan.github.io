import os
import sys

filepath=''
try:
    filepath = sys.argv[1]

except:
    print("please add filepath at arg")
    exit(1)

print(filepath)

try:
    os.listdir(filepath)
except:
    print('file path is not exist')

cnt = 0
for fname in os.listdir(filepath):
    if fname.endswith('.md'):
        filemd = open(fname,'r')
        filestr = filemd.read()
        if filestr.find('published') > 0 :
            continue
        filemd.close()
        filestr = filestr.replace('---','published : false\n---',2)
        filestr = filestr.replace('published : false\n','',1)
        filemd = open(fname, 'w')
        filemd.write(filestr)
        filemd.close()
        cnt += 1
        print('Covert ',fname,' file ')
print(cnt,' files convert done !')
print('all md are block success')


