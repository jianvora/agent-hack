import streamlit as st
from pathlib import Path

path = (Path(__file__).parent.parent.parent / "./MLAgentBench/benchmarks/covid_data/env").resolve()
filenames = [file.name for file in path.glob("*")]
st.write(filenames)
                                             
