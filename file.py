filename=open('text.txt','r')
print(filename.read(25))
print(filename.readline())
print(filename.readlines())
filename.close()

file_to_write=open('newtext.txt','w+')
msg='filehandling 1ec 1'
file_to_write.write(msg)
print(file_to_write.read(25))
file_to_write.close()

file_to_append=open('newtext.txt','a')
msg='appending file data'
file_to_append.write(msg)
file_to_append.close()