import numpy as np


def acoustic_impedance(vp: np.ndarray, rhob: np.ndarray) -> np.ndarray:
    return vp * rhob


def reflectivity(ai: np.ndarray) -> np.ndarray:
    return np.diff(ai) / (ai[1:] + ai[:-1])


def synthetic(refl: np.ndarray, wav: np.ndarray) -> np.ndarray:
    return np.convolve(refl, wav, mode="same")
