#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sum midi track lengths"""


import datetime
from mido import MidiFile
from pathlib import Path
from tqdm import tqdm


files_path = Path(r"path to files")
midi_list = list(files_path.glob("*.mid"))

# customize progress bar
pbar = tqdm(
    total=len(midi_list), 
    desc="Progress", 
    colour="green", 
    bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed} elapsed]"
)

with pbar:
    sum_time = []
    for file in midi_list:
        track = MidiFile(file.absolute())
        sum_time.append(round(track.length))
        pbar.update(1)

print(f"Total length: {datetime.timedelta(seconds=sum(sum_time))}")