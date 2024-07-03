import argparse
from pathlib import Path
import subprocess

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def convert_excalidraw_to_svg(input_path: Path) -> Path:
    """Use the docker files of the directory to convert an excaliraw file to svg.

    This docker image contains all the necessary dependencies for ease of use on every dev machines.
    """
    current_directory = Path(__file__).parent.resolve()
    directory_of_path = input_path.parent.resolve()
    output_name = input_path.with_suffix(".svg").name

    command = [
        "docker",
        "compose",
        "-f",
        str(current_directory / "docker-compose.yml"),
        "run",
        "--rm",
        "-v",
        f"{directory_of_path}:/tmp",
        "excalidraw-to-svg",
        "/app/node_modules/.bin/excalidraw-to-svg",
        str(Path("/tmp") / input_path.name),
        str(Path("/tmp") / output_name),
    ]

    subprocess.run(command, check=True)
    return directory_of_path / output_name


def main():
    parser = argparse.ArgumentParser(description="Convert an .excalidraw file to svg")
    parser.add_argument("input_path", type=str, help="The path to the input file.")
    args = parser.parse_args()

    try:
        output_path = convert_excalidraw_to_svg(Path(args.input_path))
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred while running the Docker Compose command: {e}")

    logger.info(f"Successfully created file {output_path}")


if __name__ == "__main__":
    main()
