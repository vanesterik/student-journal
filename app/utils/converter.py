from pathlib import Path

import markdown
from flask import url_for

md = markdown.Markdown(extensions=["codehilite", "fenced_code", "meta"])


class NoteConverter:
    def __init__(self, file_path: Path, file_content: str):
        self.file_path = file_path
        self.file_content = file_content
        self.id = self._generate_id()
        self.href = self._generate_href()
        self.content = self._generate_content()
        self.date, self.tags, self.title = self._generate_metadata()

    def _generate_id(self) -> str:
        return self.file_path.stem

    def _generate_href(self) -> str:
        return url_for("pages.note", note=self.id)

    def _generate_content(self) -> str:
        return md.convert(self.file_content)

    def _generate_metadata(self) -> tuple:
        md.convert(self.file_content)
        meta = md.Meta  # type: ignore

        date = meta.get("date", [None])[0]
        title = meta.get("title", [None])[0]

        # Remove spaces and split tags by comma
        tags = meta.get("tags", [None])[0].split(", ")
        # Remove empty tags
        tags = [tag for tag in tags if tag]
        # Generate tag links
        tags = [
            {"label": label, "id": label.lower().replace(" ", "-")} for label in tags
        ]

        return date, tags, title
