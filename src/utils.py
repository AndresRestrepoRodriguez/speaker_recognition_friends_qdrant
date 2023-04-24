import numpy as np
import glob as glob
import os
import streamlit as st
from typing import List


def tensor_to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()


def get_audios_folder(path_folder: str):
    return glob.glob(os.path.join(path_folder, '*.wav'))


def generate_payload_list(audios_list: List):
    payload = [{'name': os.path.basename(audio).replace('.wav', '')} for audio in audios_list]
    return payload


def divide_chunks(list_data: List, chunk_size: int):
    for i in range(0, len(list_data), chunk_size):
        yield list_data[i:i + chunk_size]

    
def make_grid(cols: int, rows: int):
    grid = [0]*rows
    for i in range(rows):
        with st.container():
            grid[i] = st.columns(cols)
    return grid