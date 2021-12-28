"""This script converts the AviationData.xml to a flattened CSV file
it is only here for reference."""

from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd  # run with pandas 1.3.5


def xml_to_csv(xml_path: Path):
    tree = ET.parse(xml_path)

    data = []
    for element in tree.iterfind("./*"):
        for item in element.iterfind("*"):
            data.append(dict(item.items()))

    aviation_data = pd.DataFrame(data)
    aviation_data.to_csv(xml_path.parent / f"{xml_path.stem}.csv", index=False)


if __name__ == "__main__":
    xml_path = Path("data/AviationData.xml")
    xml_to_csv(xml_path)
