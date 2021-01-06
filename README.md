# `Machine learning on electrophysiology EEG signals`

# Course at [AI4Health school 2021](https://ai4healthschool.org/)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agramfort/AI4Health_ml_eeg/)

In this course you will learn about state-of-the-art machine learning approaches for EEG and MEG signals. You will do so with [MNE-Python](https://mne.tools/) which has become a reference tool to process MEG/EEG/sEEG/ECoG data in Python, as well as the [scikit-learn library](https://scikit-learn.org/). You will learn to predict what people attend to given their brain activity or look at predicting sleep stages from clinical EEG data. The materials consist of slides in PDF and Jupyter notebooks using public datasets.

Inspiration for this tutorial was taken from the [MNE-Python](https://mne.tools/stable/auto_tutorials/sample-datasets/plot_sleep.html) and [braindecode](https://braindecode.org/auto_examples/plot_sleep_staging.html) sleep staging examples, as well as the [`mne-torch`](https://github.com/mne-tools/mne-torch) repository.

[**Open this tutorial in Google Colab**](https://colab.research.google.com/github/hubertjb/dl-eeg-tutorial/blob/main/sleep_staging_physionet.ipynb)

## Running locally

To run this tutorial locally, make sure the repo has been cloned on your machine, and that the required packages are installed in a Python environment (3.6 or above). The packages can be installed by running:
```
pip install -r requirements.txt
```

## Authors

  - [Alexandre Gramfort](http://alexandre.gramfort.net/), Inria
  - [Hubert Banville](https://hubertjb.github.io/), Inria & Interaxon
