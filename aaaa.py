import re


def format_kwargs_docstring(docstring):
    """Add extra newlines between list items in kwargs sections.
    """
    pattern = r"(\*\*kwargs:\*\*.*?)\n\s*-\s"
    formatted_docstring = re.sub(
        pattern, lambda m: f"{m.group(1)}\n\n- ", docstring, flags=re.DOTALL
    )
    return formatted_docstring


# Example usage
docstring = """
    Args:
        **kwargs: These are keyword arguments that include:
            - `option1` (str): Description of option1.
            - `option2` (int): Description of option2.
    """
formatted = format_kwargs_docstring(docstring)
print(formatted)
