'''
File Handling:
    files 
    create -> software -> output device/system
    text editor -> python -> terminal/console

    normal text


program memory
Files -> locally store on a system, used by system owner.
Cloud/Server -> multiple users can access at the same time


    normal text
        A -> 65
        a -> 97

    excel, word, images, video, csv, json, pdf


    open(filename.ext,access_mode)
    Access_mode:
    r -> read
    w -> write
    a -> append
    r+ -> read and write
    rb -> read binary data
'''

# a = 20
# b = 30
# c = a + b # 20 + 30
# print(c)


file = open('example.txt','a')
for i in range(11,21):
    file.write(f"Line number {i}\n")
file.close()

with open('example.txt','r') as rf:
    # data = rf.read()
    # data = rf.readline()
    data = rf.readlines()
    print(data)
    print(len(data))
    print(data[0])
