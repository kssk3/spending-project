from inspect import cleandoc
import os
import sys

import pandas as pd
import numpy as np
from pandas.core.computation.parsing import clean_column_name


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

    total_rows = len(df)

    for cat in df["category"].unique():
        category_df = df[df["category"] == cat] 

        count = len(category_df)
        ratio = count / total_rows * 100

        category_status[cat] = {
            "count": count,
            "ratio" : ratio
        }

    for cat, stats in category_status.items():
        print(f"{cat}: {stats['count']}건, {stats['ratio']:.1f}%")
    _end_space()

    result = check_missing(df)
    numpy_amount_stats(df, result)


def check_missing(df : pd.DataFrame) -> dict:
    col_missing_value = df.isnull().sum()
    total_rows = len(df)

    result = {
        "missing_columns": {},
        "no_missing_columns" : []
    }

    for column, value in col_missing_value.items():
        ratio = value / total_rows * 100

        if  value >= 1:
            if ratio < 5:
                severity = "낮음"
            elif ratio < 20:
                severity = "중간"
            else:
                severity = "높음"

            result["missing_columns"][column] = {
                "missing_count" : value,
                "missing_ratio" : ratio,
                "severity" : severity
            }

        else:
            result["no_missing_columns"].append(column)
    
    print(f"결측치 없는 컬럼 목록 : {result['no_missing_columns']}")
    print(f"결측치 있는 컬럼 목록 : {result['missing_columns']}")
    _end_space()

    return result


def numpy_amount_stats(df : pd.DataFrame, data : dict):
    cleaned = df.filter(["amount"]).dropna()
    
    mean = np.mean(cleaned)
    std = np.std(cleaned, ddof=1)
    median = np.median(cleaned)
    minimum = np.min(cleaned)
    maximum = np.max(cleaned)

    over_amount = df[cleaned["amount"] > 50000]
    print(over_amount)
    _end_space()

    result = df["amount"].describe()

    comparisons = {
        "mean" : np.isclose(mean, result["mean"]),
        "std" : np.isclose(std, result["std"]),
        "median" : np.isclose(median, result["50%"]),
        "minimum" : np.isclose(minimum, result["min"]),
        "maximum" : np.isclose(maximum, result["max"])
    }

    for row, col in comparisons.items():
        print(f"{row}, {'v' if col else 'x'}")

    _end_space()

def _end_space():
    print("=============")

result = load_data("data/spending.csv")
explore_structure(result)




