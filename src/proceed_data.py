from pandas import read_excel
from io import BytesIO


def proceed(data: bytes) -> dict[str: str]:
    df = read_excel(BytesIO(data))
    df = df.to_dict()

    data = {
        'title': [x for x in df['title'].values()],
        'url': [x for x in df['url'].values()],
        'xpath': [x for x in df['xpath'].values()]
    }

    return df
