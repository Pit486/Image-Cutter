from PIL import Image
n = 0

with open('setup.txt', 'r', encoding='UTF-8') as f:
    files = ((f.readline())[12:]).replace('\n', '').split(',')
    xf = int(((f.readline())[16:]).replace('\n', ''))
    yf = int(((f.readline())[16:]).replace('\n', ''))
    xs = int(((f.readline())[8:]).replace('\n', ''))
    ys = int(((f.readline())[8:]).replace('\n', ''))
    column = int(((f.readline())[7:]).replace('\n', ''))
    line = int(((f.readline())[5:]).replace('\n', ''))
    p = column*line
    
def cutter(f):
    global n
    x = xs-xf
    y = ys-yf
    k = 0
    kol = Image.open(f)
    for i in range(p):
        k=k+1
        if k==line+1:
            y=y+yf
            x = xs-xf
            k = 1
        n=n+1
        card = kol.crop((x+xf,y+yf,x+xf+xf,y+yf+yf))
        card.save('c'+ str(n)+'.png')
        x=x+xf
    return 
for f in files:
    cutter(f)
print('Ok!')
