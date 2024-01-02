from pathlib import Path


class Config:
    base_dir = Path()
    notes_dir = base_dir / "app/notes"
    output_dir = base_dir / "output"
