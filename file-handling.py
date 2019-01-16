"""
mode:
    r: reading
    r+: reading & writing
    rb: binary read
    w:  writing. caution: overwrites existing file
    w+: write & read. caution: overwrites existing file
    wb: writing binary
    a: append
    a+: append & read
"""
filename = open('text.txt','r')
print(filename.read(25)) #reads character by character
print(filename.readline()) #read per line
print(filename.readlines())
filename.close()

file_to_write = open('newText.txt','w+')
msg = 'file handing lec 1'
file_to_write.write(msg)
print(file_to_write.read(25))
file_to_write.close()

file_to_append = open('newText.txt','a')
msg = 'appending file data'
file_to_append.write(msg)
file_to_append.close()