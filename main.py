"""One Line of Earned Pride: writes a quiet, earned moment of pride to /output/entry.txt.

The line: Mara has fought for this bakery -- the loan, the paperwork, the
years of saving. The pride is not announced; it arrives in the last word,
when she looks at the empty shop she now owns and whispers "Mine."
"""
import os

LINE = "Mara's hands shook as she signed the loan papers for the bakery \u2014 then she looked at the empty shop and whispered, 'Mine.'"


def write_entry(path: str) -> None:
    """Write the single entry line to ``path``, creating its directory."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


def main() -> None:
    # The gate requires 1-240 characters of UTF-8 text, one line.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    assert "\n" not in LINE, "line must be a single line"
    output_path = "/output/entry.txt"
    try:
        write_entry(output_path)
    except OSError:
        # Local run fallback: the sandbox always provides /output.
        output_path = "out/entry.txt"
        write_entry(output_path)
    # Round-trip check: the file the judge reads must be exactly the line.
    with open(output_path, encoding="utf-8") as f:
        assert f.read() == LINE, "written entry differs from LINE"


if __name__ == "__main__":
    main()
