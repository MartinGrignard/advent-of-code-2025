from dataclasses import dataclass
from pathlib import Path
from typing import Self

import nox
from nox import Session


@dataclass
class Day:
    day: int

    @property
    def directory(self: Self) -> Path:
        return Path("days") / f"{self.day:02d}"

    @property
    def main_script(self: Self) -> Path:
        return self.directory / "main.py"

    @property
    def test_script(self: Self) -> Path:
        return self.directory / "test.py"

    @classmethod
    def from_session(cls: type[Self], session: Session) -> Self:
        day = int((session.posargs or ["1"])[0])
        return cls(day)


@nox.session(python=False)
def init(session: Session) -> None:
    """Initialise the structure for a problem."""
    day = Day.from_session(session)
    session.run(
        "uv",
        "run",
        "cookiecutter",
        "--no-input",
        "--output-dir",
        "days",
        "template",
        f"day={day.day}",
    )
