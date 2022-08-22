#!/usr/bin/env python3
from config import para
import argparse


def loaddict():
    wordsdict = set()
    with open(para["dict"], "r", encoding="utf-8") as fp:
        for word in fp:
            wordsdict.add(word.strip())
    return wordsdict


def main(args):


if __name__ == "__main__":
    parse = argparse.ArgumentParser("input sentence file and seg sentence using blank")
    parse.add_argument("--output", "-o", default="../result/corpus.result.txt")
    args = parse.parse_args()
    main(args)
