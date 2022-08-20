#!/usr/bin/env python3
from os import ctermid
from pickletools import pylist
from pydoc import cli


def segWord():
    fw = open("pysegSentence.txt", "w")
    """
        首行出现的“\ufeff” 叫BOM("ByteOrder Mark") 用来声明该文件的编码信息
        utf-8 是以字节为编码单元,它的字节顺序在所有系统中都一样,没有字节序问题,因此不需要BOM,所以当用
        utf-8编码方式读取带有BOM的文件时,它会把BOM 当作文件内容来处理，也就会在首行出现"\ufeff"
        utf-8-sig(signature) 意为带有签名的utf-8,因此utf-8-sig读取带有BOM的utf-8文件时会把BOM单独
        处理 与文本内容隔离开
    """
    with open("../origin/Sentence.txt", encoding='utf-8-sig') as fr:
        for line in fr:
            array = [word for word in line.strip()]
            words = ' '.join(array)
            fw.write(words + "\n")
        fw.close()

def checkEqualPyCText():
    totalLine = 0
    correctLine = 0
    with open("../result/pysegSentence.txt", "r") as pyText, open("../result/c++segSentence.txt", "r") as cText:
        for i, j in zip(pyText, cText):
            if list(i) == list(j):
                correctLine += 1
            else:
                print(i)
                print(j)
            totalLine += 1
    """
    while pyLine or cLine:
        pyLine = pyText.readline()
        cLine = cText.readline()
        if list(pyLine) == list(cLine):
            correctLine += 1
        totalLine += 1
        print(totalLine)
        print(pyLine)
        # break
    """
    print("c++ 分字 和 python 分字 按行比对结果：", correctLine/totalLine * 100)


if __name__ == "__main__":
    segWord()
    checkEqualPyCText()
