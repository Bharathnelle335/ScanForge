
import streamlit as st
from scanners import SCANNER_MAP
from main import run_selected_scanners

st.title('ScanForge GUI')
target = st.text_input('Target path or image')
selected = [flag for flag in SCANNER_MAP if st.checkbox(flag)]
if st.button('Run') and target:
    run_selected_scanners(target, selected)
    st.success('Done!')
