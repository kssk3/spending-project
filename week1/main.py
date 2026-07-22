import os
import sys

import pandas as pd
import numpy as np


def load_date(file_path : str) -> pd.DataFrame:
    has_file = os.path.exists(file_path)
    if not has_file:
        print(f"파일을 찾을 수 없습니다 : {file_path}")
        sys.exit(1)

    df = pd.read_csv(file_path, encoding="utf-8-sig")
    rows, cols = df.shape
    print(f"데이터 로드 완료 : {rows}행 x {cols}열")
    return df

def explore_structure(df : pd.DataFrame) :
    pass

    
result = load_date("data/spending.csv")



