"""
測試 streamlit_extras.grid
    可以在sidebar中建立元件列表，然後在元件中點選，就可以在主畫面中顯示出來



"""

import numpy as np
import streamlit as st
from streamlit_extras.grid import grid
import pandas as pd


def example():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")
    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)

random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
def example2():

    my_grid = grid(1,1, vertical_align="bottom")
    # Row 1:
    my_grid.markdown("[Section 1](#section-1)")
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.divider()
    # Row 2:
    my_grid.markdown("[Section 2](#section-2)")
    my_grid.line_chart(random_df, use_container_width=True)
    my_grid.divider()
    # Row 3:
    my_grid.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    my_grid.divider()
    # Row 4:
    my_grid.dataframe(random_df, use_container_width=True)


# ---------------------------------- sidebar --------------------------------- #
# Add the filters. Every widget goes in here
with st.sidebar:
    example2()

st.header("Section 1")
st.dataframe(random_df, use_container_width=True)

st.header("Section 2")
st.line_chart(random_df, use_container_width=True)