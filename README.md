# PATCH
## Visualization Complexity Science Workshop 2024
This project contains the code to produce, analyze and plot the networks created by `PATCH`, a network model of [P]referential [A]ttachment, [T]riadic [C]losure and [H]omophily.
This is an interface that simplifies the interaction with the [NetIn software package](https://cshvienna.github.io/NetworkInequalities/) for the participants of [Visualizing Complexity Science Workshop 2024](https://vis.csh.ac.at/vis-workshop-2024/) hosted at the [Complexity Science Hub](https://csh.ac.at).

## Requirements
To run the code in this repository, install the packages in `requirements.txt`.
It is advisable to create a virtual environment to not interfere with other local python installations.
For instance, you can setup a virtual environment using [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) as follows:
```bash
conda create --name patch
```
Activate this environment by running ```conda activate patch``` and then install the packages by executing:
```bash
pip install -r requirements.txt
```
You should now be able to run the local code.
Running
```bash
python -c "import patch_workshop; print(patch_workshop.__version__)"
```
should terminate without an error and print the local package version.

## The project
We explain the code structure by the folder tree
```
├── README.md  # this file
├── data  # folder containing data
│   └── graphs  # folder containing raw graphs if present
├── notebooks  # jupyter notebooks
│   └── plot_line_plots.ipynb  # create line plots of presentation
│   └── visualize_graph.ipynb  # creates or loads and visualizes a graph
├── patch_workshop  # local project containing helper functions
│   ├── constants.py  # constant strings and values
│   ├── homophily_metrics.py  # function to compute EI index
│   ├── inequality_metrics.py  # inequality metrics
│   ├── stats.py # function to compute CDFs
│   └── utils.py  # helpful functions to load/store and create graphs
├── plots  # folder that contains output plots
├── requirements.txt  # software packages
├── scripts  # scripts to compute and transform aggregate statistics
│   ├── generate_graphs_and_statistics.py # creates graphs and its statistics
│   └── transform_aggregate_statistics.py
└── setup.py
```

### notebooks
Contains useful notebooks that create the plots shown in the presentation and highlight how to create networks using `PATCH`.
You can run a local jupyter server by running ```jupyter notebook``` in your terminal and the open the presented weblink in your browser to run the notebooks (see [documentation](https://docs.jupyter.org/en/latest/) for details).

### patch_workshop
This folder has general functions that simplify the interaction with the created data and the [NetIn package](https://cshvienna.github.io/NetworkInequalities/).
They can be imported in an arbirtrary Python script as (see [notebooks](#notebooks) for examples):
```python
from patch_workshop.utils import create_graph
```

### scripts
Contains Python scripts to simulate many networks, as well as code to compute and translate the aggregate statistics required to produces the presented plots.
The aggregated statistics will also be provided as a `.csv`-file to the participants of the workshop.
A small subset of 30 simulated networks will also be provided.

## Advanced usage
The scripts in the `scripts/`-folder show how the graphs are created internally.
Users who want to create networks beyond the definition of `PATCH` presented here, should have a look at the documentation of the parent [NetIn package](https://cshvienna.github.io/NetworkInequalities/).

As this is work in progress, we are working with a preliminary version of [NetIn](https://github.com/CSHVienna/NetworkInequalities/tree/erpatch).
Similar to the present repository (see the version of `netin` in [`requirements.txt`](requirements.txt)), one needs to install a specific version to have access to `PATCH`.

## Contact
In case of questions or bugs, open an issue in [github](https://github.com/mannbach/2024_visualizing_complexity_patch/issues) or contact me directly at `bachmann \at csh.ac.at`.
