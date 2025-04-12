from pandas import read_excel
from io import BytesIO


def proceed(data: bytes) -> dict[str: str]:
    df = read_excel(BytesIO(data))
    df = df.to_dict()

    return df
