#!/usr/bin/env python3
import argparse
from operator import index, truediv
from re import I

def main(args):
    # 使用正向分词 得出的评价指标
    with open(args.forward, "r", encoding="utf-8") as fseg, open(args.answer, "r", encoding="utf-8-sig") as fs:
        oriTotal = 0
        segTotal = 0
        correct = 0
        while True:
            senSeg = fseg.readline()
            senOri = fs.readline()
            if not senSeg or not senOri:
                break
            senSeg = senSeg.strip().split()
            senOri = senOri.strip().split()
            oriTotal += len(senOri)
            segTotal += len(senSeg)
            index = 0
            segIndex = 0
            while index < len(senOri) or segIndex < len(senSeg):
                if senOri[index] == senSeg[segIndex]:
                    correct += 1
                    index += 1
                    segIndex += 1
                else:
                    word = [senOri[index]]
                    segWord = [senSeg[segIndex]]
                    while True:
                        if "".join(word) > "".join(segWord):
                            segIndex += 1
                            segWord.append(senSeg[segIndex])
                        elif "".join(word) < "".join(segWord):
                            index += 1
                            word.append(senOri[index])
                        else:
                            segIndex += 1
                            index += 1
                            break
    print("corpus.answer.txt word count: %d, result seg word count: %d, result seg correct count: %d" % (oriTotal, segTotal, correct))
    # 召回率
    recall = float(correct / oriTotal * 100)
    # 正确率
    precision = float(correct / segTotal * 100)
    # F 传值
    F = recall * precision * 2 / (recall + precision)
    print("分词结果. 召回率: %f 正确率: %f F值: %f" % (recall, precision, F))

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="evaluate segWord result")
    parse.add_argument("--forward", "-f", help="forward seg corpus.answer", default="../result/corpus.forward.result.txt")
    parse.add_argument("--backward", "-b", help="backward seg corpus.answer", default="../result/corpus.backward.result.txt")
    parse.add_argument("--answer", "-i", help="origin corpus.answer", default="../origin/corpus.answer.txt")
    args = parse.parse_args()
    main(args)