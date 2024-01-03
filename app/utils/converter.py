import re
from pathlib import Path

import markdown
from flask import url_for
from markdown.extensions.wikilinks import WikiLinkExtension
from slugify import slugify


def note_url_builder(label, base, end):
    note = slugify(label)
    url = url_for("pages.note", note=note)
    return url


md = markdown.Markdown(
    extensions=[
        "codehilite",
        "fenced_code",
        "meta",
        WikiLinkExtension(build_url=note_url_builder),
    ]
)


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
        content = md.convert(self.file_content)
        content = re.sub(
            r'src="(/[^"]*)"',
            lambda match: f'src="{url_for("static", filename=match.group(1))}"',
            content,
        )
        return content

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
        tags = [{"label": label, "id": slugify(label)} for label in tags]

        return date, tags, title
