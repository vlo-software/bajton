import re
from functools import lru_cache


TEMPLATE_BASE = """
//TEMPLATE BEGIN
{}
//TEMPLATE END
"""


@lru_cache(maxsize=100)
def parse_problem_template(template_str):
    template = re.findall(r"//TEMPLATE BEGIN\n([\s\S]+?)//TEMPLATE END", template_str)
    return {"template": template[0] if template else ""}


@lru_cache(maxsize=100)
def build_problem_template(template):
    return TEMPLATE_BASE.format(template)
