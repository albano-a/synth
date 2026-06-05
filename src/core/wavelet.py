import numpy as np


def ricker(peak_freq: float, n_samples: int, dt: float) -> np.ndarray:
    t = (np.arange(n_samples) - n_samples // 2) * dt
    pi2 = (np.pi * peak_freq * t) ** 2
    return (1.0 - 2.0 * pi2) * np.exp(-pi2)


def ormsby(f1: float, f2: float, f3: float, f4: float, n_samples: int, dt: float) -> np.ndarray:
    t = (np.arange(n_samples) - n_samples // 2) * dt

    def _term(fa, fb):
        return (np.pi * fa * np.sinc(fa * t)) ** 2 / (fa - fb)

    w = _term(f4, f3) - _term(f3, f4) - _term(f2, f1) + _term(f1, f2)
    peak = np.max(np.abs(w))
    return w / peak if peak != 0 else w


def from_file(path: str, skiprows: int = 0, delimiter: str | None = None) -> np.ndarray:
    data = np.loadtxt(path, skiprows=skiprows, delimiter=delimiter)
    if data.ndim > 1:
        data = data[:, -1]
    return data
