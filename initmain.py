#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Project: Symmetry
# Version: 1.0
# Copyright: (C) 2024 Dr.Sc.KAWAMOTO,Takuji (Ext)
# Create: 2024/06/11 22:07:25 JST
#
'''プログラム要約

プログラム詳細
'''

import os
import sys
import re
import argparse
# import csv
# import itertools
# import math
# import subprocess
# import shutil

import numpy as np

usage_message = '''%(prog)s [-h] [--peaks PEAKS] [--line-profile]
                       dist-featuremaps*/<NN名>/<学習サンプル名>/<観測空間名>
                       [<テストサンプル名>]'''
help_message = '''(クラス,峰数) 毎の代表モデル選別

    ./do1-dist-featuremaps.zsh から ./do5-collect-models.zsh
    で dist-featuremaps フォルダ内に生成した学習サンプルに関する分析結果を使っ
    て (クラス,峰数) 毎に代表モデルを選別する。
    引数で指定した学習サンプルフォルダ以下に selected-preds フォルダを作成し、
    この中に出力データを格納する。
'''

parser = argparse.ArgumentParser(
    description=help_message, usage=usage_message,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--peaks', default=None,
                    help='峰数リスト(例: --peaks 1,2,3,4,5,6,7,8,9,10)。models'
                    ' を指定した場合は学習サンプルフォルダ以下の models.csv に'
                    '列挙された全ての峰数リストを使用する。')
parser.add_argument('--line-profile', action='store_true',
                    help='GaussianMixtureModel の重い部分のプロファイリングを画'
                    '面出力する。')
flags, fileargs = parser.parse_known_args()



def main():
    '''メイン関数要約

    メイン関数詳細
    '''
    pass


if __name__ == '__main__':
    main()

