#coding: utf8

def make_header(width, height, charsets, name):
    tmp = """info face="微软雅黑" size={height} bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=2 padding=0,0,0,0 spacing=1,1 outline=0
common lineHeight={height} base=26 scaleW={width} scaleH={height} pages=1 packed=0 alphaChnl=1 redChnl=0 greenChnl=0 blueChnl=0
page id=0 file="{name}.png"
chars count={count}
"""
    header = tmp.format(tmp, count=len(charsets), name=name, width=width, height=height)
    return header
    
def make_body(width, height, charsets, name):
    tmp = """char id={ord}   x={x}     y={y}     width={w}    height={h}    xoffset=0     yoffset=0     xadvance={w}    page=0  chnl=15"""
    cnt = len(charsets)
    w = int(width/cnt)
    h = int(height)
    index = 0
    ret = []
    for i in charsets:
        c = ord(i)
        info = tmp.format(ord=c, w=w, h=h, y=0, x=index*w)
        index= index+1
        ret.append(info)
    return ret

def getImageSize(image):
    from PyQt4 import QtCore, QtGui
    ret = dict()
    original = QtGui.QImage(image)
    if not original:
        ret["width"] = 0
        ret["height"] = 0
        return ret
    ret["width"] = original.size().width()
    ret["height"] = original.size().height()
    return ret
    
def make_fnt(fullpath, chars):
    size = getImageSize(fullpath)
    if size["width"] ==0 or size["height"] ==0:
        print("图片文件地址不合法, " + fullpath)
        return
    width = size["width"]
    height = size["height"]
    import os.path    
    fname, ext = os.path.splitext(fullpath)
    path, name = os.path.split(fname)
    fnt_name = fname + ".fnt"
    fp = open(fnt_name, "w")
    if not fp:
        print(fnt_name, "cannot opened.")
        return
    header = make_header(width, height, chars, name)
    body = make_body(width, height, chars, name)
    fp.write(header)
    fp.write("\n".join(body))
    fp.write("\n")
    fp.close()
    
def main():
    make_fnt("Fonts/SignLayer/num1.png", "0123456789")
    make_fnt("Fonts/SignLayer/num2.png", "0123456789")
    make_fnt("Fonts/SignLayer/num3.png", "X0123456789")
    make_fnt("Fonts/SignLayer/num4.png", "X0123456789")
    make_fnt("Fonts/SignLayer/num5.png", "X0123456789")
    
    make_fnt("Fonts/HallUILayerNew/number_money.png", "0123456789")
    make_fnt("Fonts/HallUILayerNew/number_vip.png", "0123456789")
    
if __name__ == "__main__":
    main()
