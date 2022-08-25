#!/usr/bin/env python3




from ast import main, parse
import argparse

def main(args):
    pass


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="evaluate segWord result")
    parse.add_argument("--forward", "-f", help="forward seg corpus.answer", default="../result/corpus.forward.result.txt")
    parse.add_argument("--backward", "-b", help="backward seg corpus.answer", default="../result/corpus.backward.result.txt")
    parse.add_argument("--answer", "-i", help="origin corpus.answer", default="../origin/corpus.answer.txt")
    args = parse.parse_args()
    main(args)