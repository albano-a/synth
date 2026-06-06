"""
Build script for Synth.

Usage:
    python build.py           standard build (clean + compile + PyInstaller)
    python build.py --clean   remove dist/ and build/ only
    python build.py --onefile single-file executable (slower startup)
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
BUILD = ROOT / "build"
SPEC = ROOT / "synth.spec"
OUTPUT = DIST / "Synth"

_UI_SRC = SRC / "gui" / "qt" / "SynthMainWindow.ui"
_UI_DST = SRC / "gui" / "qt" / "ui_SynthMainWindow.py"
_RC_SRC = SRC / "gui" / "resources" / "main.qrc"
_RC_DST = SRC / "gui" / "resources" / "main_rc.py"
_LOGO_PNG = SRC / "gui" / "resources" / "icons" / "logo.png"
_LOGO_ICO = SRC / "gui" / "resources" / "icons" / "logo.ico"


def clean():
    for d in (DIST, BUILD):
        if d.exists():
            shutil.rmtree(d)
            print(f"Removed {d.relative_to(ROOT)}/")


def compile_ui():
    print("Compiling UI...")
    subprocess.run(["pyside6-uic", str(_UI_SRC), "-o", str(_UI_DST)], check=True)
    print(f"  {_UI_DST.relative_to(ROOT)}")


def compile_rc():
    print("Compiling resources...")
    subprocess.run(["pyside6-rcc", str(_RC_SRC), "-o", str(_RC_DST)], check=True)
    print(f"  {_RC_DST.relative_to(ROOT)}")


def make_icon():
    if _LOGO_ICO.exists():
        return
    try:
        from PIL import Image
    except ImportError:
        print(
            "Pillow not found — icon will not be embedded in the .exe.\n"
            "  Install with: pip install Pillow"
        )
        return
    img = Image.open(_LOGO_PNG).convert("RGBA")
    img.save(
        _LOGO_ICO,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (256, 256)],
    )
    print(f"Created {_LOGO_ICO.relative_to(ROOT)}")


def ensure_pyinstaller():
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("PyInstaller not found — installing...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyinstaller"],
            check=True,
        )


def build(onefile: bool = False):
    ensure_pyinstaller()
    compile_ui()
    compile_rc()
    make_icon()
    clean()

    cmd = [sys.executable, "-m", "PyInstaller", str(SPEC), "--noconfirm"]
    if onefile:
        cmd += ["--onefile"]

    print(f"\nRunning PyInstaller...")
    subprocess.run(cmd, cwd=ROOT, check=True)

    exe = OUTPUT / "Synth.exe"
    print(f"\nBuild complete.")
    print(f"  Output : {OUTPUT}")
    print(f"  Launch : {exe}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--clean" in args:
        clean()
    else:
        build(onefile="--onefile" in args)
