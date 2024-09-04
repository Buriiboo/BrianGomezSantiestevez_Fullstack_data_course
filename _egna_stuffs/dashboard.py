from pathlib import Path
import pandas as pd
import streamlit as st

def read_data():
    data_path = Path(__file__).parents[0]
    df = pd.read_csv(data_path / "cleaned_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df

print(read_data)

def layout():
    df = read_data()
    st.markdown("#YH dashboard")
    st.dataframe(df)
#dunder name = __is a special variable, which is equal to '__main__' when we run this script
#when we import this script from, elsewhere, __name__ is the scripts name
if __name__ == '__main__':
    layout()
