import csv
import logging
import os
import shutil

logger = logging.getLogger("development")


def list_csv_files(path: str) -> dict[str, dict[str, list]]:
    """
    Returns a dictionary of all CSV files in the given path.

    Args:
        path (str): The path to search for CSV files.

    Returns:
        files_to_process (dict): A dictionary of file paths for all CSV files found in the given path.

    Raises:
        FileNotFoundError: If the provided path does not exist.
    """

    # Check if the path exists
    if not os.path.exists(path):
        logger.error(f"The path '{path}' does not exist.")
        raise FileNotFoundError(f"The path '{path}' does not exist.")

    csv_files = []
    files_to_process = {}

    # Walk through the directory tree starting from the given path
    for root, dirs, files in os.walk(path):
        for file in files:
            # Check if the file has a .csv extension
            if file.endswith('.csv'):
                # Construct the full file path and append it to the list
                db_id, table, _ = parse_filename(file)
                files_to_process[db_id] = files_to_process.get(db_id, {})
                files_to_process[db_id][table] = files_to_process[db_id].get(table, [])
                files_to_process[db_id][table].append(os.path.join(root, file))

    logger.info(f"Found {len(csv_files)} files")
    return files_to_process


def read_file_content(path: str) -> list[list[str]]:
    """
    Returns the content of the CSV file
    :param path: The CSV path
    :return: List of rows from the CSV file
    """
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        return [row for row in reader]


def parse_filename(file_path: str) -> tuple[str, ...]:
    """
    Returns the parts from the filename
    :param file_path: complete file path
    :return: list with DB name, Table name and date
    """
    file_name = os.path.basename(file_path)
    name = os.path.splitext(file_name)[0]  # removes file's extension
    return tuple(name.strip('%').split('%'))


def move_file(file_path: str, destination_path: str) -> str:
    """
    Moves a file to a destination directory
    :param file_path: Current file path
    :param destination_path: Destination directory
    :return: New file path after the move operation
    Raises:
        FileNotFoundError: If the file to be moved is not found.
        NotADirectoryError: If either of the destination directories is not a valid directory.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check if the destination directories are valid
    if not os.path.isdir(destination_path):
        raise NotADirectoryError(f"Invalid directory: {destination_path}")

    # Get the filename from the file path
    filename = os.path.basename(file_path)

    # Construct the new file path
    new_file_path = os.path.join(destination_path, filename)

    # Move the file
    shutil.move(file_path, new_file_path)

    return new_file_path
