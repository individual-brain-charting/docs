# -*- coding: utf-8 -*-
"""
Diagram of the IBC acquisitions

Author: Ana Luisa Pinho
e-mail: ana.pinho@inria.fr

Compatibility: Python 3.5

Last update: Feb 2021
"""

import os
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.patheffects as pe

# %%
# #############################################################################
#                    PARAMETERS TO BE CHANGED BY THE USER                     #
# #############################################################################

# ========================== IMAGE PROPERTIES =================================

resolution = 90
fsize = (80, 30)

# =============================== INPUTS ======================================

# Release number (for filename)
release = 5

seqtype_fname = 'sequence_type'
taskdurat_fname = 'task_duration'
protocols_folder = 'sessions'
# Order to load protocols' csv files and draw rectangles' sequence
protocol_order = ['screening', 'archi', 'hcp1', 'hcp2', 'language_nsp', 'mtt1',
                  'mtt2', 'preferences', 'tom', 'enumeration', 'self', 'clips',
                  'clips', 'clips', 'clips_retinotopy', 'raiders1', 'raiders2',
                  'lyon1', 'lyon2', 'audio1', 'audio2', 'stanford1',
                  'stanford2', 'stanford3', 'biomo', 'lpp1', 'lpp2', 'mathlang',
                  'spatial_navigation', 'bbt1', 'bbt2', 'bbt3', 'camcan1',
                  'camcan2', 'fbirn', 'vs_wm', 'reward_proc', 'scene_face_body',
                  'monkey_kingdom', 'color_motion', 'optimism_bias', 'aomic',
                  'abstraction_Theo']

# ============================ RECTANGLES =====================================

# Starting point of rectangle sequences
xo = 0.22
yo = 0.050
# Height distance between rectangle sequences
rectspace_coeff = 0.021
# Height of the rectangles sequence
hrect = 0.015

# ===================== LABELS OF THE SESSIONS = ==============================

# Starting point of labels
x_position = 0.21
y_position = 0.056
# Distance between labels
labelspace_coeff = 0.021
# Names of protocols' labels
labels = ['Screening', 'ARCHI', 'HCP 1', 'HCP 2', 'RSVP Language', 'MTT 1',
          'MTT 2', 'Preference', 'TOM', 'Enumeration', 'Self', 'Clips 1',
          'Clips 2', 'Clips 3', 'Clips 4', 'Raiders 1', 'Raiders 2', 'Lyon 1',
          'Lyon 2', 'Audio 1', 'Audio 2', 'Stanford 1', 'Stanford 2',
          'Stanford 3', 'Biological Motion', 'Le Petit Prince 1', 
          'Le Petit Prince 2', 'Mathlanguage', 'Spatial Navigation',
          'The Good, the Bad and the Ugly 1',
          'The Good, the Bad and the Ugly 2',
          'The Good, the Bad and the Ugly 3', 'CamCAN 1', 'CamCAN 2', 'FBIRN',
          'VS_WM', 'Reward Processing', 'Scene perception & Face-Body',
          'Monkey Kingdom', 'Color & Motion', 'Optimism Bias', 'AOMIC',
          'Abstraction']

# Size of the letters
font_size = 30

# ======================= TASKS PER SESSION ===================================

# Starting point of tasks' labels
x_pos = 0.8
y_pos = 0.08

# Distance between labels
taskspace_coeff = 0.0215

# Fontsize of the tasks labels
task_fontsize = 30

# Tasks included in each session
sessions = [['Standard x2, Spatial x2'],
            ['Standard x2, Spatial x2, Social x2, Emotional x2',],
            ['Emotion x2, Gambling x2, Motor x2, Language x2'],
            ['Relational x2, Social x2, Working Memory x2'],
            ['RSVP-Language x6'],
            ['Resting State x2, MTT-WE x3'],
            ['Resting State x2, MTT-SN x3'],
            ['Food x2, Paintings x2, Faces x2, Houses x2'],
            ['TOM Localizer x2, EP Localizer x2, MOV Localizer x2'],
            ['VSTM x4, Enumeration x2'],
            ['Self x4, "Bang" movie x1'],
            ['Clips x6'], ['Clips x6'], ['Clips x6'],
            ['Clips x3, Retinotopy x6'],
            ['Runs correspond to movie chapters of different lengths'],
            ['Runs correspond to movie chapters of different lengths'],
            ['MOTO x2, MCSE x2, MVEB x2, MVIS x2'],
            ['AUDI x2, LEC1 x2, LEC2 x2, VISU x2'],
            ['Realistic Sounds x6'], ['Realistic Sounds x6'],
            ['Stop Signal x2, Two by Two x2, Attention Network x2'],
            ['Motor Selective Stop Signal x2, Discount x2, Stroop x2'],
            ['Columbia Cards x2, Tower x2, Dot Pattern Expectancy x2'],
            ['Type 1 x4, Type 2 x4'],
            ['Story audio x5'],
            ['Story audio x4, Localizer x1'],
            ['Type A x4, Type B x3'],
            ['Spatial Navigation x8'],
            ['Movie viewing x7'],
            ['Movie viewing x7'],
            ['Movie viewing x7'],
            ['Emotional memory x2, Emotion recognition x2, Stop no go x2'],
            ['Oddball x2, VSTM x4, Finger tapping x2'],
            ['Breath hold x2, Checkboard react. x2, Fingertap x2, Item recogn. x2'],
            ['Visual and working memory search x4'],
            ['Reward processing x2, NARPS x4'],
            ['Scene perception x4, Face-body x4'],
            ['Monkey kingdom movie x5'],
            ['Color perception x4, Motion perception x4'],
            ['Optimism bias x4, AOMIC movie x1'],
            ['Localizer x1, Abstraction x4']]

# Task label offset (for aligning the labels with rectangles)
ytask_offset = [-.028 for i in range(len(sessions))]

# ============================= ARROW =========================================

# Arrow position
arrow_beginning = (0.22, 0.035)
arrow_ending = (0.73, 0.035)
# Arrow label position
x_time = 0.4
y_time = 0.015
# Arrow label name
arrow_label = 'Time'
# Fontsize
arrow_label_size = 45

# ============================ LEGEND =========================================

# Width of rectangles
rect_width = .053
# Height of rectangles
rect_height = .03
# Height distance between rectangles in the legend
lg_rectspace_coeff = 0.06
# Height distance between names of the sequences in the legend
lg_txtspace_coeff = 0.04
# Title of the legend
lg_title = "Legend:"
# y position of legend box frame
lg_height = 0.65
# x position of legend box frame
lg_width = 0.785
# x position of rectangles and title of the legend
x_pos_lg = 0.26
# y position of rectangles of the legend
y_rect = 0.96
# y position of title of the legend
y_pos_lg = 1
# x position of names of the sequences
x_pos_txtlg = 0.31
# y position of names of the sequences
y_pos_txtlg = 0.95
# Fontsize of title of the legend
legend_size = 35

# %%
# #############################################################################
#                           LOAD INPUTS                                       #
# #############################################################################

# Read csv file to generate data frame of sequence type
df_seqtype = pd.read_csv(seqtype_fname + '.csv')
# Read csv file to genetate data frame of task duration
df_taskduration = pd.read_csv(taskdurat_fname + '.csv')
# Define the pathway of the protocols directory
inputs_path = os.path.abspath(protocols_folder)

# %%
# #############################################################################
#                            GENERAL SETTINGS                                 #
# #############################################################################

# Create image object with axes
fig, ax = plt.subplots(figsize=fsize)
ax.axis('off')
# Remove space around the plotting area, i.e.
# axes coordinate system = figure coordinate system
plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
# Create background colour
fig.patch.set_facecolor('white')

# Transformation from display (pixels) to figure coordinate system
transf = fig.transFigure.inverted()
# Transformation from display (pixels) to axes coordinate system
inv = ax.transAxes.inverted()


def create_dict(seq_id, val):
    """
    Create a ordered-item dictionary from specific data-frame columns
    """
    df_keys = seq_id.values.tolist()
    df_values_raw = val.values.tolist()
    df_values = [float(df_value / 1e4)
                 if isinstance(df_value, str) is False else df_value
                 for df_value in df_values_raw]
    odict = OrderedDict((df_key, df_values[i])
                        for i, df_key in enumerate(df_keys))
    return odict


# %%
# #############################################################################
#                                PROTOCOLS                                    #
# #############################################################################

# ================= DICTIONARY WITH TYPES OF SEQUENCES ========================

seqtype = create_dict(df_seqtype['sequence_id'], df_seqtype['color_hex'])

# ================== DICTIONARIES WITH TASK DURATIONS =========================

taskduration = create_dict(df_taskduration['task_id'],
                           df_taskduration['duration_sec'])

# ============== COLORMAPS AND WIDTHMAPS OF THE PROTOCOLS =====================

# Generate list of dataframes containing sequence type and durations for each
# session
df_list = [pd.read_csv(inputs_path + '/' + protocol + '.csv')
           for protocol in protocol_order]

# Generate colormaps and widthmaps
clmaps = []
wmaps = []
for df, df_protocol in enumerate(df_list):
    clmap = [seqtype[df] for df in df_protocol['colormap'].values.tolist()]
    wmap = [taskduration[df] for df in df_protocol['widthmap'].values.tolist()]
    clmaps.append(clmap)
    wmaps.append(wmap)

# ====================== GENERATE THE RECTANGLES ==============================
for m, clmap_prot in enumerate(clmaps):
    y_offset = yo + m * rectspace_coeff
    for c, clmap in enumerate(clmap_prot):
        if c == 0:
            x_offset = xo
        else:
            x_offset = x_offset + wmaps[m][c - 1] + 0.003
        rect = plt.Rectangle((x_offset, y_offset), wmaps[m][c], hrect,
                             color=clmap)
        ax.add_patch(rect)


# %%
# #############################################################################
#                          LABELS OF THE PROTOCOLS                            #
# #############################################################################

# Generate labels
for lb, label in enumerate(labels):
    f = fig.text(0, 0, label, size=font_size,
                 bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(1., 1., 1.)))
    # Width of the text box in display (pixel) coordinates
    bb = f.get_window_extent(renderer=fig.canvas.get_renderer())
    # Transform width of the text box from display to figure coordinates system
    bb_figcoords = bb.transformed(transf)
    # Readjust the horizontal position using the width of the text box
    # previously generated
    f.set_position((x_position - bb_figcoords.width, y_position +
                    lb * labelspace_coeff))

# %%
# #############################################################################
#                        TASKS INCLUDED PER SESSION                           #
# #############################################################################

# Generate labels
for pt, tasks in enumerate(sessions):
    tasks.reverse()
    y_space = y_pos + ytask_offset[pt] + pt * taskspace_coeff
    for tk, task in enumerate(tasks):
        t = fig.text(0, 0, task, size=task_fontsize)
        # Width of the text box in display (pixel) coordinates
        tb = fig.get_window_extent(renderer=fig.canvas.get_renderer())
        # Transform width of the text box from display
        # to figure coordinates system
        tb_figcoords = tb.transformed(transf)
        # Readjust the horizontal position using the width of the text box
        # previously generated
        new_x = x_pos - tb_figcoords.width + 0.93
        new_y = y_space + tk * taskspace_coeff
        t.set_position((new_x, new_y))

# %%
# #############################################################################
#                              LEGEND BOX                                     #
# #############################################################################

# generate a list of sequences for legend
txt_lg = create_dict(df_seqtype['sequence_id'], df_seqtype['name'])

# Draw rectangles in the legend
for legend, text in zip(enumerate(seqtype.values()),txt_lg.values()):
    rect = plt.Rectangle((x_pos_lg + legend[0] * lg_rectspace_coeff, y_rect),
                         rect_width, rect_height, color=legend[1])
    ax.add_patch(rect)

    # calculate center of the rectangles
    cx = (x_pos_lg + legend[0] * lg_rectspace_coeff) + rect_width/2.0
    cy = y_rect + rect_height/2.0

    # Write name of the sequences in the center of the rectangles
    ax.annotate(text, (cx, cy), color='w', weight='bold', 
                fontsize=30, ha='center', va='center',
                path_effects=[pe.withStroke(linewidth=6, foreground="black")])

# Set title of the legend
fig.text(x_pos_lg-0.04, y_pos_lg-0.03, lg_title, size=legend_size, weight='semibold')

# Build the rectangular frame around the legend
# left, width = lg_width, 0.21
# bottom, height = 0.01, lg_height
# right = left + width
# top = bottom + height
# p = plt.Rectangle((left, bottom), width, height, fill=False)
# ax.add_patch(p)

# %% Add the time arrow
ax.annotate('', xytext=arrow_beginning, xy=arrow_ending,
            xycoords='axes fraction',
            arrowprops=dict(headlength=0.03, headwidth=10., width=1.7, color='k'))

# Arrow label
b = fig.text(x_time, y_time, arrow_label, size=arrow_label_size,
             weight='semibold')

# %%
# #############################################################################
#                               SAVE IMAGE                                    #
# #############################################################################

fig.savefig('acquisitions_diagram_release{}.pdf'.format(str(release)),
            dpi=resolution)
