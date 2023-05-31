# ODMR Analysis

```{admonition} Prerequisites
- Beginner lessons
- A local copy of this lesson's assets, found [here][odmr]

[odmr]: https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/odmr/
```

```{topic} Objectives
- Improve upon a plotting analysis pipeline
- Learn about plotting Pandas arrays
```

This lesson provides sample data and an accompanying Jupyter notebook. You may
follow along with the `ODMR_Analysis.ipynb` as a supplement to this lesson.


## Introduction

Optically detected magnetic resonance (ODMR) spectroscopy is a way to detect
materials that have a singlet-state to triplet-state transition. When such a
material is excited, some relaxation pathways occur through the emission of
photons, which can be characterized with a spectrometer. The
majority of emission occurs at a predominant spectral line known as the _Zero
Phonon Line_ (ZPL), but intersystem crossing allows for less-stable and more
sparsely-occurring radiative pathways at longer wavelengths.

The difference in energy between a singlet-state and a triplet-state is
associated with photons of microwave frequencies (GHz). When the system is pumped
with a microwave signal that matches this transition, the relaxation pathway
associated with intersystem crossing is temporarily enhanced and competes with
the relaxation pathway responsible for ZPL emission. Sweeping the microwave
field through a range of frequencies results in characteristic dips in the
observed fluorescence of the ZPL. At larger magnetic fields, the separation of
these dips becomes more prominent due to the Zeeman splitting of the triplet
states.

## Initial Analysis

Our colleague gathered some ODMR spectra and handed it to us for
analysis. Specifically, he wants to identify the frequencies for which the ZPL
signal is reduced.

The measurement consists of a ZPL signal continuously excited by a laser source
in the presence of various driving microwave frequencies (delivered as
microwave pulses). The ZPL signal is represented by counts in a photon detector
collected for a given amount of time, measured both before and after the
microwave pulse is applied (labeled _Reference_ and _Signal_, respectively). By
comparing the photoluminescence (PL) signal before and during the microwave
pulse, one can determine the relative dip in PL signal. By repeating this
measurement for a range of microwave frequencies, one can identify where the
ZPL signal is most reduced.

Our colleague kept track of user-specific parameters like the number of
microwave pulses over which the PL signal was integrated, the excitation laser
power, and the time delay between when the pulse was applied compared to when
the photoluminescence measurement began. You will find these in the `data/`
folder with names like `ODMR_500kBurst_350uW_50nsdelay.csv`. In reality, there
might be many such iterations to inspect, but a only a down-selected number of
files is presented for this lesson.

Files with similar acquisition parameters may be combined in one analysis. The
number of microwave pulses in each acquisition is largely irrelevant except for
if you want to evaluate the efficiency of the reduction in PL. The purpose of
probing multiple microwave pulses is to help resolve contrast between a faint
signal and background noise. Integrating over more pulses takes longer to
acquire, but typically results in higher signal-to-noise ratio.

If after one ODMR spectral acquisition the contrast in PL is unclear, we can
repeat the measurement and combine with the previous acquisition to effectively
increase the number of pulses over which we integrate.

### Understanding our colleague's initial analysis

Our colleague investigated his ODMR contrast after each acquisition. He found
that after one acquisition, the ODMR contrast did not show up well in a graph,
so he repeated the same acquisition a number of times. He copied the results of
subsequent acquisitions into an Excel file and accumulated the _Reference_ and
_Signal_ values from all identical acquisitions before determining a composite
ODMR contrast. This analysis appears in an Excel file alongside the first
acquisition, but was later converted to a `.csv` for better compatibility with
Dropbox.

This approach has several problems:

- Data and analysis are not logically separated
- It is not clear by filename alone which acquisition houses the analysis
- All equations in the original `.xlsx` file are lost during the conversion to `.csv`
- Inclusion of further measurements means recreating the original `.xlsx`
  equations and updating the corresponding analysis.

The analysis in Excel is simple enough to recreate, but let's practice framing
this in Python.

## Refined Analysis

We'll set out with the following objectives:

- Leave original data alone
- Generate and save our ODMR contrast figure to a specified directory

We'll also specify some assumptions about what we should expect from our end
user and what we promise to do in return.

### Guidelines

The user is expected to provide a list of files of ODMR spectra collected at the same
location and with identical power settings. The filenames can differ in number of microwave
bursts, but currently the number of integrations is not tracked in the dataframe. The ODMR
data is concatenated for all files in this list, so extending the integration is as simple
as adding another file to the list.

#### Data requirements

- Files in list have identical structure \[Frequency, Ref, Sig\]
- Frequency values in each file have an overlapping subset
- Frequency values are between 0 and 65e3 (uint16)
- APD counts from all accumulated runs do not total more than 4.2e9 (uint32) in either channel

#### Usage

- Adjust the filename list to point to the directory where your ODMR files are located
- If analysis is needed on only one file, pass in a list of one element.
- Select appropriate filtering in `glob` to pick out a subset of files if desired
- Adjust threshold and distance parameters for cleaning via `scipy.signal.find_peaks`
    - Sensible defaults have been provided for this particular dataset
- Run All Cells (if in Jupyter Lab)
    - Inspect cleaning results, adjust threshold as necessary
- Grab figures as necessary for publication
    - Adjust graph style with rcParams instead of in plot
