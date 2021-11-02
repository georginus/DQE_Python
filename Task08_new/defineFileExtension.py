from pathlib import Path


def defineFileExtension(filepath):
    file_extension = Path(filepath).suffix.lower()
    return file_extension
