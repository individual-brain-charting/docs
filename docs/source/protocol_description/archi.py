"""
Pictural description of  Archi protocols
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pd_dir = os.path.join(
#    '../../../../..',
#    '/home/analu/ibc_repos/analysis_pipeline/IBC_Y1/neurospin_data/info')
# pd_dir = os.path.join('/home/bertrand/mygit/hbp-brain-charting/analysis_pipeline/IBC_Y1/neurospin_data/info')
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
          '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
          '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
          '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5'][::2]

BLACK_LIST = ['question', 'response', 'false_belief_video_pourquoi',
              'mechanistic_audio_pourquoi', 'mechanistic_video_pourquoi',
              'false_belief_audio_pourquoi', 'probe', 'right_hand_cue',
              'left_hand_cue', 'right_foot_cue', 'left_foot_cue', 'tongue_cue',
              'dummy']


def make_fig(events, protocol_duration, title, name, text_offset=150):
    df = pd.DataFrame().from_csv(events, sep='\t')
    for key in ['complex_sentence_objclef', 'complex_sentence_subjrel',
                'complex_sentence_objrel']:
        df = df.replace(key, 'complex_sentence')

    for key in ['simple_sentence_coord', 'simple_sentence_adj',
                'simple_sentence_cvp']:
        df = df.replace(key, 'simple_sentence')

    keys = df.trial_type.unique()
    keys = [key for key in keys if key not in BLACK_LIST]

    sampling = protocol_duration * 10 + 10
    x = np.linspace(-10, protocol_duration, sampling)

    #fig = plt.figure(figsize=(12, 5))
    fig, ax = plt.subplots(figsize=(12, 5))
    for i, key in enumerate(keys):
        onset = df.index[df.trial_type == key]
        duration = df.duration[df.trial_type == key]
        offset = onset + duration
        idx_on = np.searchsorted(x, onset)
        idx_off = np.searchsorted(x, offset)
        y = np.zeros(sampling)
        y[idx_on] += 1
        y[idx_off] -= 1
        y = np.cumsum(y)
        y_pos = .1 + i * 1.08
        plt.fill(x, y + y_pos, color=colors[i], linewidth=1, label=key)
        label = key.replace('_', ' ')
        plt.text(protocol_duration, y_pos + .3, label, color=colors[i],
                 weight='bold', fontsize=16)

    xticks = np.linspace(0, 100 * np.trunc(protocol_duration / 100),
                         np.trunc(protocol_duration / 100) + 1).astype(np.int)

    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(width=1.5, length=2.5, labelsize=15)
    plt.xlabel('Time (s)', fontweight="bold", fontsize=16)
    plt.xlim((0, protocol_duration + text_offset))
    plt.yticks([], [])
    plt.xticks(xticks, xticks)
    # plt.title('Block-design of the %s task' % title, fontweight="bold", fontsize=20)
    plt.tight_layout()
    plt.savefig('blocks_%s.pdf' % name)

events = os.path.join('inputs', 'archi_social.tsv')
# events = os.path.join(pd_dir, 'localizer_social',
#                      'paradigm_descriptors_social_01_run1.csv')
# 'paradigm_descriptors_localizer_social_001_block1.csv')
protocol_duration = 516
title = 'ARCHI Social'
name = 'archi_social'
make_fig(events, protocol_duration, title, name)

events = os.path.join('inputs', 'archi_spatial.tsv')
protocol_duration = 489
title = 'ARCHI Spatial'
name = 'archi_spatial'
make_fig(events, protocol_duration, title, name)

events = os.path.join('inputs', 'archi_standard.tsv')
protocol_duration = 307
title = 'ARCHI Standard'
name = 'archi_standard'
make_fig(events, protocol_duration, title, name, text_offset=70)

events = os.path.join('inputs', 'archi_emotional.tsv')
# 'paradigm_descriptors_localizer_emotionnel_001_block1.csv')
protocol_duration = 456
title = 'ARCHI Emotional'
name = 'archi_emotional'
make_fig(events, protocol_duration, title, name, text_offset=180)

events = os.path.join('inputs/paradigm_descriptors_sub-01_run0.tsv')
protocol_duration = 630
title = 'RSVP-Language'
name = 'rsvp_language'
make_fig(events, protocol_duration, title, name, text_offset=200)

events = os.path.join('inputs',
    'paradigm_descriptors_emotion_sub-01_run1.tsv')
protocol_duration = 270
title = 'HCP Emotion'
name = 'hcp_emotion'
make_fig(events, protocol_duration, title, name, text_offset=40)

events = os.path.join('inputs',
    'paradigm_descriptors_gambling_sub-01_run1.tsv')
protocol_duration = 360
title = 'HCP Gambling'
name = 'hcp_gambling'
make_fig(events, protocol_duration, title, name, text_offset=80)

events = os.path.join('inputs',
    'paradigm_descriptors_language_sub-01_run1.tsv')
protocol_duration = 450
title = 'HCP Language'
name = 'hcp_language'
make_fig(events, protocol_duration, title, name, text_offset=40)

events = os.path.join('inputs',
    'paradigm_descriptors_motor_sub-01_run1.tsv')
protocol_duration = 400
title = 'HCP Motor'
name = 'hcp_motor'
make_fig(events, protocol_duration, title, name, text_offset=60)

events = os.path.join('inputs',
    'paradigm_descriptors_relational_sub-01_run1.tsv')
protocol_duration = 620
title = 'HCP Relational'
name = 'hcp_relational'
make_fig(events, protocol_duration, title, name, text_offset=120)

events = os.path.join('inputs',
    'paradigm_descriptors_social_sub-01_run1.tsv')
protocol_duration = 400
title = 'HCP Social'
name = 'hcp_social'
make_fig(events, protocol_duration, title, name, text_offset=60)

events = os.path.join('inputs',
    'paradigm_descriptors_wm_sub-01_run1.tsv')
protocol_duration = 600
title = 'HCP Working Memory'
name = 'hcp_wm'
make_fig(events, protocol_duration, title, name, text_offset=120)



#plt.show()
