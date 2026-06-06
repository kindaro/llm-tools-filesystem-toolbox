import llm
import os


class ReadFiles (llm.Toolbox):
    def __init__(self): pass

    def list_folder(self, target_folder: str) -> list[str]:
        """
        This function will return the list of files and folders in the folder
        specified in the input parameter `target_folder`.

        Parameters:
        - target_folder (str): A path relative to the current working folder
          that should be listed.

        Returns:
        - list[str]: the list of files and folders in the target folder.

        Example:
            call: list_folder({'target_folder': '.'})
            result: ["some_file", "another_file"]
        """
        return os.listdir(os.path.abspath(target_folder))

    def read_file(self, target_file: str) -> list[str]:
        """
        This function reads the content of a file located at a specified path and
        returns it as a string. The file must be encoded in UTF-8.

        Parameters:
        - target_file (str): A path relative to the current working folder
          that should be read.

        Returns:
        - str: the contents of the target file.

        Example:
            call: read_file(self, "README.md")
            Returns: "I am a README file."
        """
        with open(os.path.abspath(target_file), "r", encoding="utf-8") as file:
            data = file.read()
        return data


@llm.hookimpl
def register_tools(register):
    register(ReadFiles)
