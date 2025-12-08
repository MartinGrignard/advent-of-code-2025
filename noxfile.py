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

    @property
    def input(self: Self) -> Path:
        return self.directory / "input.txt"
    
    @property
    def test_input(self: Self) -> Path:
        return self.directory / "test_input.txt"

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


@nox.session(python=False)
def test(session: Session) -> None:
    """Test the implementation of a solution."""
    day = Day.from_session(session)
    session.run(
        "uv",
        "run",
        "pytest",
        str(day.test_script),
    )


@nox.session(python=False)
def run(session: Session) -> None:
    """Run a solution."""
    day = Day.from_session(session)
    session.run("bash", "-c", f"uv run {day.main_script} < {day.input}")


@nox.session(python=False, name="run-test")
def run_test(session: Session) -> None:
    """Run a solution on its test input."""
    day = Day.from_session(session)
    session.run("bash", "-c", f"uv run {day.main_script} < {day.test_input}")