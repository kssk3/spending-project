import os
import stat
import sys

import pandas as pd
import numpy as np


def load_data(file_path : str) -> pd.DataFrame:
    has_file = os.path.exists(file_path)
    if not has_file:
        print(f"파일을 찾을 수 없습니다 : {file_path}")
        sys.exit(1)

    df = pd.read_csv(file_path, encoding="utf-8-sig")
    rows, cols = df.shape
    print(f"데이터 로드 완료 : {rows}행 x {cols}열")
    _end_space()
    return df

def explore_structure(df : pd.DataFrame) :
    rows, cols = df.shape
    print(f"전체 행 수와 열 수를 출력합니다 : {rows}행 x {cols}열")
    _end_space()

    print("컬렴명과 자료형을 출력합니다.")
    for col , row in df.dtypes.items():
        print(f" {col} : {row}")
    _end_space()
    
    head_result = df.head(5)
    print("상위 5행을 출력합니다.")
    print(head_result)
    _end_space()

    show_distribution(df)

def show_distribution(df : pd.DataFrame): 
    category_status = {}

    total_count = len(df)

    for cat in df["category"].unique():
        category_df = df[df["category"] == cat] 

        count = len(category_df)
        ratio = count / total_count * 100

        category_status[cat] = {
            "count": count,
            "ratio" : ratio
        }

    for cat, stats in category_status.items():
        print(f"{cat}: {stats['count']}건, {stats['ratio']:.1f}%")


def _end_space():
    print("=============")

result = load_data("data/spending.csv")
explore_structure(result)




