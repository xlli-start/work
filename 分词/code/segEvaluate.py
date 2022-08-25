#!/usr/bin/env python3
from unittest import result
from config import para
import argparse


def loadDict():
    wordsDict = set()
    with open(para["dict"], "r", encoding="utf-8") as fp:
        for word in fp:
            wordsDict.add(word.strip())
    return wordsDict

#正向分词
def forwardSeg(sens, sen, wordsDict):
    # sen = sen.strip()
    endIndex = para["wordlen"]
    beginIndex = 0
    words = list()
    while beginIndex < len(sen):
        word = sen[beginIndex:endIndex]
        if word in wordsDict:
            words.append(word)
            beginIndex += len(word)
            endIndex = beginIndex + para["wordlen"]
        elif len(word) == 1:
            words.append(word)
            beginIndex += 1
            endIndex = beginIndex + para["wordlen"]
        else:
            endIndex -= 1
    sens.append(" ".join(words))

# 逆向分词
def backwardSeg(sens, sen, wordsDict):
    beginIndex = len(sen) - para["wordlen"]
    endIndex = len(sen)
    words = list()
    while beginIndex < endIndex:
        word = sen[beginIndex:endIndex]
        if word in wordsDict:
            words.append(word)
            endIndex = beginIndex
            beginIndex -= para["wordlen"]
            beginIndex if beginIndex > 0 else 0
        elif len(word) == 1:
            words.append(word)
            endIndex = beginIndex
            beginIndex -= para["wordlen"]
            beginIndex if beginIndex > 0 else 0
        else:
            beginIndex += 1
    words.reverse()
    sens.append(" ".join(words))

def segSentence(args):
    wordsDict = loadDict()
    sens = list()
    with open(para["sentence"], "r", encoding="utf-8") as fs:
        for sen in fs:
            if args.options:
                forwardSeg(sens, sen, wordsDict)
            else:
                backwardSeg(sens, sen, wordsDict)
            # return
    resultSegSens(args.output, sens)

def resultSegSens(outPath, sens):
    with open(outPath, "w", encoding="utf-8") as fw:
        for sen in sens:
            fw.write(sen)

def main(args):
    segSentence(args)


if __name__ == "__main__":
    parse = argparse.ArgumentParser("input sentence file and seg sentence using blank")
    parse.add_argument("--output", "-o", default="../result/corpus.result.txt")
    # 带store_true时为真 -p 为真 不带为假
    parse.add_argument("--options", "-p", help="choose forward or backward", action='store_true')
    args = parse.parse_args()
    main(args)
