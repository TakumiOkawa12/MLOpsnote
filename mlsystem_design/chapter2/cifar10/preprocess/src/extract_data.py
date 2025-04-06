import os
import pickle
from typing import List

import numpy as np
from PIL import Image


def unpickle(file):
    """
    指定されたpickleファイルを開き、データを辞書として読み込む
    Args:
        file(str)：読み込むpickleファイルのパス
    Returns:
        dict: pickleファイルから復元された辞書データ
        {
            b"filenames": [b"image1.png", b"image2.png", ...],  # ファイル名のリスト
            b"labels": [3, 7, 2, ...],  # 画像のクラスラベル
            b"data": [[R, G, B, ...], ...]  # 画像データ (数値のリスト)
        }
    """
    with open(file, "rb") as fo: # バイナリモードで開く
        dict = pickle.load(fo, encoding="bytes")
    return dict


def parse_pickle(rawdata, rootdir) -> List[List[str]]:
    """
    CIFAR-10 のデータ (pickle) を解析し、
    各画像をラベルごとのフォルダに保存する。
    画像のクラスラベルとファイル名の対応リストを作成。

    Args:
        rawdata (dict): pickle から復元された辞書データ。
        rootdir (str): 画像を保存するルートディレクトリのパス。

    Returns:
        List[List[str]]: クラスラベルと対応するファイル名のリスト。
    """
    # クラスごとのフォルダを作成
    for i in range(10):
        directory = f"{rootdir}/{i}"
        os.makedirs(directory, exist_ok=True)
    class_to_filename_list = []

    # 画像データを処理
    for i in range(len(rawdata[b"filenames"])):
        filename = rawdata[b"filenames"][i].decode("utf-8") # ファイル名
        label = rawdata[b"labels"][i] # クラスラベル（0〜9）
        data = rawdata[b"data"][i] # 画像データ

        # 画像データの形を変換 (CIFAR-10の形式をPIL画像に変換)
        data = data.reshape(3, 32, 32) # (3072,)→(3, 32, 32)
        data = np.swapaxes(data, 0, 2) # (3, 32, 32)→(32, 32, 3)
        data = np.swapaxes(data, 0, 1) # (32, 32, 3)

        # 画像を保存
        with Image.fromarray(data) as img: # Image.fromarray()でNumpy配列を画像に変換
            image_path = f"{rootdir}/{label}/{filename}"
            img.save(image_path)

        # クラス名とファイル名を記録
        class_to_filename_list.append([label, filename])

    return class_to_filename_list

