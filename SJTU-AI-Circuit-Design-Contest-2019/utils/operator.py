import os

jpgs = os.getcwd() + '/JPEGImages'

txts = os.getcwd() + '/ImageSets/Main'

txtpath = []
for _, _, files in os.walk(txts):
    for filename in files:
        if filename[0] == '.':
            continue
        txtpath.append('./ImageSets/Main/%s' % filename)

useful_images = set()
for txtp in txtpath:
    with open(txtp, 'r') as f:
        s = f.readlines()
        for line in s:
            if line == '':
                continue
            tokens = line.replace('  ', ' ').split(' ')
            if len(tokens) != 2:
                print(tokens)
                print("this happens at %s, line: %s" % (txtp, line))
            assert(len(tokens) == 2)
            print("token[1]:", tokens[1])
            if int(tokens[1]) == 1:
                useful_images.add(tokens[0])

print("now, there are %d useful images" % len(useful_images))
input()
for _, _, files in os.walk(jpgs):
    for jpgname in files:
        if jpgname.replace('.jpg', '') in useful_images:
            print("留下来 %s" % jpgname)
            continue
        # print('removed file @ ./JPEGImages/%s' % jpgname)
        os.system('rm ./JPEGImages/%s' % jpgname)

