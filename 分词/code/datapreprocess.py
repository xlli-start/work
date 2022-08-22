#!/usr/bin/env python3
import argparse


def main(args):
    dictSet = set()
    sen = list()
    with open(args.indata, "r", encoding="utf-8") as fp, open(args.outsentence, "w", encoding="utf-8") as fs:
        for line in fp:
            word = line.strip().split()
            if not word:
                fs.write("".join(sen) + "\n")
                sen.clear()
                continue
            sen.append(word[1])
            dictSet.add(word[1])
    wordlen, dictlines= 0, 0
    with open(args.outdict, "w", encoding="utf-8") as fd:
        for word in dictSet:
            fd.write(word + "\n")
            wordlen = max(len(word), wordlen)
            dictlines += 1
    print("字典行数: %d, 字典集中最大词长:%d" % (dictlines, wordlen))

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="make dict and sentence files,example. corpus.dict.txt corpus.sentence.txt")
    parse.add_argument("--indata", "-i", default="./data.conll", help="input origin data.conll")
    parse.add_argument("--outdict", "-d", default="./corpus.dict.txt", help="output result dict.txt")
    parse.add_argument("--outsentence", "-s", default="./corpus.sentence.txt", help="output result sentence.txt")
    args = parse.parse_args()
    main(args)
