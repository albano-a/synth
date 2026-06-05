# Synth

A lightweight synthetic seismogram generator for geophysicists.

## Overview

Synth takes a well log (LAS file) and a wavelet as inputs and produces a synthetic seismogram through acoustic impedance and reflectivity computation. It is designed as a fast, standalone alternative to heavy interpretation platforms for well-to-seismic tie workflows.

## Workflow

```
LAS file (Vp + RHOB) → Acoustic Impedance → Reflectivity → Convolution → Synthetic
                                                               ↑
                                                          Wavelet input
                                                    (Ricker, Ormsby, or file)
```

## Features

- Load LAS files and select Vp and density curves
- Built-in wavelets: Ricker (peak frequency) and Ormsby (frequency band)
- Load wavelet from CSV or text file
- Interactive well log and synthetic display side by side
- Export synthetic as CSV

## Stack

- **GUI:** PyQt5 + pyqtgraph
- **Plotting:** matplotlib
- **Well logs:** lasio
- **Computation:** numpy

## Installation

```bash
pip install -e ".[dev]"
```

## Running

```bash
python src/main.py
```

## Development

```bash
# Run tests
pytest

# Run a specific test file
pytest src/tests/test_core.py
```

## Project Structure

```
synth/
├── pyproject.toml
├── README.md
└── src/
    ├── main.py         # Entry point
    ├── core/           # Computation: AI, reflectivity, convolution, wavelets
    ├── gui/            # PyQt5 windows, widgets, dialogs
    └── tests/          # pytest + pytest-qt test suite
```
