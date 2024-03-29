from pathlib import Path
from typing import Dict, List, Tuple

from flask import url_for

from app.config import Config
from app.utils import NoteConverter


def generate_search_index(config: Config) -> List[Dict]:
    notes_dir = Path(config.notes_dir)
    notes = []

    for file_path in notes_dir.glob("*.md"):
        with open(file_path, "r") as file:
            file_content = file.read()
            note = NoteConverter(file_path, file_content)

            # Convert tags to list of strings in order to index them
            tags = [tag["label"] for tag in note.tags]

            notes.append(
                {
                    "id": note.id,
                    "title": note.title,
                    "href": note.href,
                    "tags": tags,
                }
            )

    return notes


def generate_diagram(config: Config) -> Tuple[List[Dict], List[Dict]]:
    notes_dir = Path(config.notes_dir)
    file_list = list(notes_dir.glob("*.md"))
    edges = []
    nodes = []

    for file_path in file_list:
        with open(file_path, "r") as file:
            file_content = file.read()
            note = NoteConverter(file_path, file_content)

            # Add current note to nodes list
            nodes.append(
                {
                    "id": note.id,
                    "label": note.title,
                    "href": note.href,
                }
            )

            # Find other notes that are linked in current note
            for file_path in file_list:
                other_note_id = file_path.stem
                other_note_href = url_for("pages.note", note=other_note_id)

                if other_note_href in note.content:
                    edges.append(
                        {
                            "source": note.id,
                            "target": other_note_id,
                        }
                    )

    return edges, nodes


def generate_all_notes(config: Config) -> List[Dict]:
    notes_dir = Path(config.notes_dir)
    notes = []

    for file_path in notes_dir.glob("*.md"):
        with open(file_path, "r") as file:
            file_content = file.read()
            note = NoteConverter(file_path, file_content)

            notes.append(
                {
                    "id": note.id,
                    "label": note.title,
                    "href": note.href,
                    "tags": note.tags,
                }
            )

    # Sort notes by title
    notes.sort(key=lambda note: note["label"])

    return notes


def generate_notes_by_tag(tag: str, config: Config) -> List[Dict]:
    notes = generate_all_notes(config)
    notes = [
        note
        for note in notes
        if any(note_tag["label"] == tag for note_tag in note["tags"])
    ]

    return notes


def generate_note(note: str, config: Config) -> NoteConverter:
    notes_dir = Path(config.notes_dir)
    file_name = f"{note}.md"
    file_path = notes_dir / file_name

    with open(file_path, "r") as file:
        file_content = file.read()

        return NoteConverter(file_path, file_content)
