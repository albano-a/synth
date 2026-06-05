import lasio
import numpy as np


def load(path: str) -> lasio.LASFile:
    return lasio.read(path)


def curve_names(las: lasio.LASFile) -> list[str]:
    return [c.mnemonic for c in las.curves]


def get_curve(las: lasio.LASFile, mnemonic: str) -> np.ndarray:
    return las[mnemonic]


def depth(las: lasio.LASFile) -> np.ndarray:
    return las.index
