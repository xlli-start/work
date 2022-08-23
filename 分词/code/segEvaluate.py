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

def segSentence():
    wordsDict = loadDict()
    sens = list()
    with open(para["sentence"], "r", encoding="utf-8") as fs:
        for sen in fs:
            sen = sen.strip()
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
            sens.append(words)
                

def main(args):
    segSentence()


if __name__ == "__main__":
    parse = argparse.ArgumentParser("input sentence file and seg sentence using blank")
    parse.add_argument("--output", "-o", default="../result/corpus.result.txt")
    args = parse.parse_args()
    main(args)
