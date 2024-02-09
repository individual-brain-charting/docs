# %%
# This script generates ./ibc_data/descriptions.json
# which contains descriptions for all tasks, conditions and
# contrasts of the IBC dataset.
# These descriptions are initially documented in other files
# of the repo.

# %%
import warnings

from pathlib import Path

import numpy as np
import pandas as pd

# %%
# Initialise output structure
d = {"tasks": {}}

# %%
# Add descriptions for all tasks
df_tasks = pd.read_csv("ibc_tasks.tsv", delimiter="\t")

for _, row in df_tasks.iterrows():
    d["tasks"][row["task"]] = {
        "description": str(row["description"]),
        "software": str(row["software"]),
        "response_device": str(row["response_device"]),
        "audio_device": str(row["audio_device"]),
        "screen_res": str(row["screen_res"]),
        "youtube": str(row["youtube"]),
        "repo": str(row["repo"]),
        "extras": str(row["extras"]),
        "tags": [],
        "conditions": {},
        "contrasts": {},
    }

# Add little note for Raiders about lags
d["tasks"]["Raiders"]["description"] += (
    " **Note:** there was some lag between the onset of each run and "
    "the initiation  of the stimuli (movie), which might vary between runs "
    "and subjects. This lag should probably be considered when analyzing the data. "
    "Find more details in the section :ref:`Lags in Raiders movie`."
)

# Add little note for GoodBadUgly about lags
d["tasks"]["GoodBadUgly"]["description"] += (
    " **Note:** there was some lag between the onset of each run and "
    "the initiation  of the stimuli (movie), which might vary between runs "
    "and subjects. This lag should probably be considered when analyzing the data. "
    "Find more details in the section :ref:`Lags in GoodBadUgly movie`."
)

# Add little note for MonkeyKingdom about lags
d["tasks"]["MonkeyKingdom"]["description"] += (
    " **Note:** there was some lag between the onset of each run and "
    "the initiation  of the stimuli (movie), which might vary between runs "
    "and subjects. This lag should probably be considered when analyzing the data. "
    "Find more details in the section :ref:`Lags in MonkeyKingdom movie`."
)

# %%
# Add descriptions for all conditions
df_conditions = pd.read_csv(
    "ibc_conditions.tsv", delimiter="\t", na_filter=False
)

missing_task = []
for _, row in df_conditions.iterrows():
    if row["task"] in d["tasks"]:
        d["tasks"][row["task"]]["conditions"][row["contrast"]] = {
            "description": str(row["description"])
        }
        d["tasks"][row["task"]]["conditions"] = dict(sorted(
            d["tasks"][row["task"]]["conditions"].items()
        ))
    else:
        missing_task.append(row["task"])

missing_task = set(missing_task)

# %%
warnings.warn(
    "The following tasks are missing a description "
    "(task names possibly don't match between files for these tasks):\n"
    f"{missing_task}"
)

# %%
# Add descriptions for all contrasts.
# This includes contrast string description
# but also a list of all conditions used to compute this contrast
df_all_contrasts = pd.read_csv(
    "all_contrasts.tsv", delimiter="\t", na_filter=False
)

missing_contrasts = []

for task in d["tasks"].keys():
    task_contrasts_filename = Path(f"ibc_data/contrasts/{task}.csv")
    all_tags = []
    if task_contrasts_filename.exists():
        df_contrasts = pd.read_csv(
            task_contrasts_filename, delimiter=",", index_col="condition"
        )
        df_contrasts = df_contrasts.T
        conditions = list(df_contrasts.columns)
        matrix_available = True
    else:
        warnings.warn(
            "The contrast matrix files have not been fetched.\n\n"
            "The algebraic information for the contrasts is hence missing."
        )
        df_contrasts = df_all_contrasts[df_all_contrasts["task"] == task]
        matrix_available = False
    for index, row in df_contrasts.iterrows():
        if matrix_available:
            contrast = row.name
        else:
            contrast = row.contrast
        description = None
        tags = []
        selected_descriptions = df_all_contrasts[
            (df_all_contrasts["task"] == task)
            & (df_all_contrasts["contrast"] == contrast)
        ]
        if len(selected_descriptions) > 0:
            description = selected_descriptions.iloc[0]["pretty name"]
            try:
                tags = eval(selected_descriptions.iloc[0]["tags"])
            except SyntaxError:
                tags = []
            assert isinstance(tags, list) or tags is None
            tags = list(map(lambda x: str(x), tags))
        else:
            missing_contrasts.append((task, contrast))
        d["tasks"][task]["contrasts"][contrast] = {
            "description": str(description),
            "tags": tags,
            "conditions": {},
        }
        d["tasks"][task]["contrasts"] = dict(sorted(
            d["tasks"][task]["contrasts"].items()
        ))
        if matrix_available:
            for i, condition in enumerate(conditions):
                weight = row[i]
                weight = float(str(weight).replace(",", "."))
                if not np.isnan(weight):
                    d["tasks"][task]["contrasts"][contrast]["conditions"][
                        condition
                    ] = weight
        all_tags += tags
    d["tasks"][task]["tags"] = list(set(all_tags))

missing_contrasts = set(missing_contrasts)

# %%
warnings.warn(
    "The following contrasts are missing a description "
    "(task / contrast names possibly don't match between files "
    "for these contrasts):\n"
    f"{missing_contrasts}"
)

# %%
# Save dictionary as json file
# with open("./ibc_data/descriptions.json", "w") as f:
#     json.dump(d, f)


# %%
# Create a tasks.rst from the dictionary
def write_section(
    rst,
    name,
    description,
    tags,
    software,
    response_device,
    audio_device,
    screen_res,
    youtube,
    repo,
    extras,
    conditions,
    contrasts,
):
    """
    Helper function to write a section to the RST file
    """
    description = description.replace(":raw-html:`<br />` ", "\n\n")
    rst.write(f"{name}\n")
    rst.write("-" * len(name) + "\n\n")
    
    rst.write(".. container:: tags\n\n")
    rst.write("   ")
    tag_count = 0
    for tag in tags:
        if tag_count <= 4:
            domains = tag.split("_")
            if not set(["response", "task"]).isdisjoint(domains):
                if name == "HcpMotor":
                    rst.write(f":bdg-warning:`{tag}` ")
                else:
                    continue
            elif not set(
                ["auditory", "sound", "listening", "voice", "speech", "music"]
            ).isdisjoint(domains):
                rst.write(f":bdg-success:`{tag}` ")
            elif not set(
                [
                    "motor",
                    "motion",
                    "grasping",
                    "saccade",
                    "saccadic",
                    "movement",
                ]
            ).isdisjoint(domains):
                rst.write(f":bdg-warning:`{tag}` ")
            elif "memory" in domains:
                rst.write(f":bdg-info:`{tag}` ")
            elif not set(
                ["visual", "vision", "face", "facial", "checkerboard", "shape"]
            ).isdisjoint(domains):
                rst.write(f":bdg-primary:`{tag}` ")
            elif not set(
                ["emotion", "emotional", "empathy", "pain"]
            ).isdisjoint(domains):
                rst.write(f":bdg-danger:`{tag}` ")
            elif not set(
                [
                    "language",
                    "reading",
                    "writing",
                    "comprehension",
                    "word",
                    "semantic",
                    "syntactic",
                    "sentence",
                    "semantics",
                ]
            ).isdisjoint(domains):
                rst.write(f":bdg-secondary:`{tag}` ")
            elif not set(
                [
                    "reward",
                    "risk",
                    "loss",
                    "decision",
                    "valuation",
                    "punishment",
                    "incentive",
                    "judgement",
                    "confidence",
                    "surprise",
                    "judgment",
                ]
            ).isdisjoint(domains):
                rst.write(f":bdg-dark:`{tag}` ")
            else:
                rst.write(f":bdg-light:`{tag}` ")
            tag_count += 1
    rst.write(f"\n\n")

    proprietary_software = ["E-Prime", "Presentation", "Vizard"]
    software_ = software.split(" ")
    if not set(software_).isdisjoint(proprietary_software):
        rst.write(".. admonition:: Implemented using proprietary software\n")
        rst.write("   :class: seealso\n\n")
        rst.write(f"   - Software: {software}\n")
    else:
        rst.write(".. admonition:: Implementation \n")
        rst.write("   :class: seealso\n\n")
        rst.write(f"   - Software: {software}\n")
    
    # Check if the task uses response device and add it
    if response_device != 'nan':
        rst.write(f"   - Response device: {response_device}\n\n")
    if audio_device != 'nan':
        rst.write(f"   - Audio device: {audio_device}\n\n")
    if repo != 'nan':
        rst.write(f"   - :octicon:`mark-github;1em;` {repo}\n\n")
    if youtube != 'nan':
        rst.write(f"   - :octicon:`video;1em;` {youtube}\n\n")
    if extras != 'nan':
        rst.write(f"   - {extras}\n\n")

    rst.write(f"{description}\n\n")

    if len(conditions) != 0:
        rst.write(
            f"The conditions for this task are described in"
            f" `this table <cond{name}_>`__"
        )
        if len(contrasts) != 0:
            rst.write(
                f" and the main contrasts derived from those conditions are"
                f" described in `this table <cont{name}_>`__.\n\n"
            )
        else:
            rst.write(".\n\n")
        rst.write(f".. dropdown:: Conditions for {name}\n")
        rst.write(f"   :name: cond{name}\n\n")
        rst.write(f"   .. list-table::\n")
        rst.write("      :header-rows: 1\n")
        rst.write("      :widths: 25 75\n\n")
        rst.write("      * - Condition\n")
        rst.write("        - Description\n")
        for key, value in conditions.items():
            rst.write(f"      * - {key}\n")
            rst.write(f"        - {value['description']}\n")
    if len(contrasts) != 0:
        rst.write("\n")
        rst.write(f".. dropdown:: Contrasts for {name}\n")
        rst.write(f"   :name: cont{name}\n\n")
        rst.write(f"   .. list-table::\n")
        rst.write("      :header-rows: 1\n")
        rst.write("      :widths: 25 75\n\n")
        rst.write("      * - Contrast\n")
        rst.write("        - Description\n")
        for key, value in contrasts.items():
            rst.write(f"      * - {key}\n")
            rst.write(f"        - {value['description']}\n")
    rst.write("\n")


# read tasks_intro.rst and write it to tasks.rst
with open("docs/tasks_intro.rst", "r") as intro:
    tasks_intro = intro.read()
# close the file
intro.close()

with open("docs/source/tasks.rst", "w") as rst:
    rst.write("All tasks\n")
    rst.write("=" * 5 + "\n\n")
    rst.write(tasks_intro)
    for task in d["tasks"].keys():
        write_section(
            rst,
            task,
            d["tasks"][task]["description"],
            d["tasks"][task]["tags"],
            d["tasks"][task]["software"],
            d["tasks"][task]["response_device"],
            d["tasks"][task]["audio_device"],
            d["tasks"][task]["screen_res"],
            d["tasks"][task]["youtube"],
            d["tasks"][task]["repo"],
            d["tasks"][task]["extras"],
            d["tasks"][task]["conditions"],
            d["tasks"][task]["contrasts"],
        )
rst.close()
