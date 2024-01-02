from flask import Blueprint, g, render_template

from app.config import Config
from app.utils import (
    generate_all_notes,
    generate_diagram,
    generate_note,
    generate_notes_by_tag,
    generate_search_index,
)

bp = Blueprint("pages", __name__)
config = Config()


@bp.before_request
def search():
    g.search_index = generate_search_index(config)


@bp.route("/")
def index() -> str:
    edges, nodes = generate_diagram(config)
    return render_template(
        "pages/index.html",
        edges=edges,
        nodes=nodes,
        title="Knowledge Graph",
    )


@bp.route("/about/")
def about() -> str:
    return render_template(
        "pages/about.html",
        title="About",
    )


@bp.route("/notes/")
def notes() -> str:
    notes = generate_all_notes(config)
    return render_template(
        "pages/note-list.html",
        notes=notes,
        title="All Notes",
    )


@bp.route("/tags/<tag>/")
def tag(tag: str) -> str:
    notes = generate_notes_by_tag(tag, config)
    title = f"Tag: {tag[0].upper() + tag[1:]}"
    return render_template(
        "pages/note-list.html",
        notes=notes,
        title=title,
    )


@bp.route("/notes/<note>/")
def note(note: str) -> str:
    data = generate_note(note, config)
    return render_template(
        "pages/note-detail.html",
        content=data.content,
        date=data.date,
        tags=data.tags,
        title=data.title,
    )


@bp.route("/page-not-found/")
def page_not_found() -> str:
    return render_template(
        "pages/page-not-found.html",
        title="Page Not Found",
    )
