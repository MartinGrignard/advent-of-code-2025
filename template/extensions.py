from typing import Self, cast

from bs4 import BeautifulSoup
import httpx
from jinja2 import Environment
from jinja2.ext import Extension


def get_day_url(day: int) -> str:
    return f"https://adventofcode.com/2025/day/{day}"


def get_day_html(day: int) -> BeautifulSoup:
    response = httpx.get(get_day_url(day))
    return BeautifulSoup(response.text, "html.parser")


def get_day_title(day: int) -> str:
    html = get_day_html(day)
    return cast(str, html.find("main").find("h2").text).replace("---", "").strip()


class AdventOfCodeExtension(Extension):
    def __init__(self: Self, environment: Environment) -> None:
        super().__init__(environment)
        environment.filters["day_url"] = lambda day: get_day_url(int(day))
        environment.filters["day_title"] = lambda day: get_day_title(int(day))
