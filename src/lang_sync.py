import argparse
import json
from dataclasses import dataclass
from typing import List

@dataclass
class TranslationFile:
    filename: str
    content: str

class LangSync:
    def __init__(self, branch_name: str, translated_files: List[TranslationFile]):
        self.branch_name = branch_name
        self.translated_files = translated_files

    def create_branch(self) -> str:
        return f"translations/{self.branch_name}"

    def commit_translated_files(self) -> str:
        commit_message = f"Translated files for {self.branch_name}"
        return commit_message

    def delete_branch(self) -> None:
        print(f"Deleting branch translations/{self.branch_name}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Lang Sync")
    parser.add_argument("--branch-name", type=str, required=True)
    parser.add_argument("--translated-files", type=str, nargs="+", required=True)
    args = parser.parse_args()

    translated_files = []
    for file in args.translated_files:
        filename, content = file.split(":", 1)
        translated_files.append(TranslationFile(filename, content))

    lang_sync = LangSync(args.branch_name, translated_files)
    print(lang_sync.create_branch())
    print(lang_sync.commit_translated_files())
    lang_sync.delete_branch()

if __name__ == "__main__":
    main()
