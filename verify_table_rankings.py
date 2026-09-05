"""Verify best/second-best formatting in manuscript comparison tables."""

import re
from pathlib import Path


SOURCE = Path(__file__).parent / "sections" / "04_experiments.tex"
METRICS = ("mDice", "mIoU", "Fw", "S", "mE", "maxE", "MAE")


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    tables = re.findall(r"\\begin\{longtable\}.*?\\end\{longtable\}", text, re.S)
    comparison_tables = [table for table in tables if "Methods & Year & mDice" in table]
    errors = []

    for table in comparison_tables:
        name = re.search(r"\\caption\{Quantitative comparison on ([^}]+)", table).group(1)
        body = table.split(r"\endlastfoot", 1)[1]
        rows = []
        for row in re.split(r"\\\\\s*(?:\n|$)", body):
            cells = [cell.strip() for cell in row.split("&")]
            if len(cells) != 9:
                continue
            values = []
            for cell in cells[2:]:
                match = re.search(r"0\.\d+", cell)
                values.append(float(match.group()) if match else None)
            rows.append((cells[0], cells[2:], values))

        for index, metric in enumerate(METRICS):
            available = sorted(
                {values[index] for _, _, values in rows if values[index] is not None},
                reverse=metric != "MAE",
            )
            best = available[0]
            second = available[1] if len(available) > 1 else None
            for method, cells, values in rows:
                value = values[index]
                if value is None:
                    continue
                bold = r"\textbf" in cells[index]
                underline = r"\underline" in cells[index]
                if bold != (value == best) or underline != (value == second):
                    errors.append(
                        f"{name}: {method} {metric}={value:.3f} "
                        f"(bold={bold}, underline={underline}; best={best:.3f}, "
                        f"second={second:.3f})"
                    )

    if errors:
        raise SystemExit("Ranking-format errors:\n" + "\n".join(errors))
    print(f"Verified {len(comparison_tables)} tables: ranking formatting is correct.")


if __name__ == "__main__":
    main()
