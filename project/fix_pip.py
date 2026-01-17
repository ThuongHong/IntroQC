import json
import os

NB_PATH = (
    "/home/lesliu/Documents/school/25_26_Semester_1/intro_qc/project/quantum-gan.ipynb"
)


def fix_pip():
    if not os.path.exists(NB_PATH):
        print("Notebook not found")
        return

    with open(NB_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # 1. Fix Pip Install
    pip_cell = None
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            source = cell.get("source", [])
            if any("!pip install" in line for line in source):
                pip_cell = cell
                break

    if pip_cell:
        new_source = []
        for line in pip_cell["source"]:
            # Look for the broken string
            if 'matplotlib>=3.7.0 "torchmetrics[image]' in line:
                # Replace with correct quoting
                line = line.replace(
                    'matplotlib>=3.7.0 "torchmetrics[image]',
                    'matplotlib>=3.7.0" "torchmetrics[image]',
                )
                print("Fixed pip install line.")
            new_source.append(line)
        pip_cell["source"] = new_source

    with open(NB_PATH, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)

    print("Notebook pip fix completed.")


if __name__ == "__main__":
    fix_pip()
