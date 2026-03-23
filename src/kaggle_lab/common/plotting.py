from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from kaggle_lab.common.io import ensure_dir


def save_current_figure(path: str | Path) -> Path:
    path = Path(path)
    ensure_dir(path.parent)
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    return path

