import argparse
import dataclasses
import logging
import os
import re
from typing import List

@dataclasses.dataclass
class Config:
    include_patterns: List[str]
    exclude_patterns: List[str]

def load_config(file_path: str) -> Config:
    try:
        with open(file_path, 'r') as file:
            import yaml
            config_data = yaml.safe_load(file)
            if config_data is None:
                config_data = {}
            return Config(
                include_patterns=config_data.get('include_patterns', []),
                exclude_patterns=config_data.get('exclude_patterns', [])
            )
    except FileNotFoundError:
        logging.warning(f"Config file {file_path} not found. Using default config.")
        return Config(
            include_patterns=['*.py', '*.java', '*.cpp'],
            exclude_patterns=['test*', 'example*']
        )

def extract_files(directory: str, config: Config) -> List[str]:
    extracted_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if any(re.match(pattern.replace('*', '.*'), file) for pattern in config.include_patterns):
                if any(re.match(pattern.replace('*', '.*'), file) for pattern in config.exclude_patterns):
                    logging.info(f"Excluding file {file_path}")
                    continue
                extracted_files.append(file_path)
    return extracted_files

def main():
    parser = argparse.ArgumentParser(description='Lang-sync extractor')
    parser.add_argument('--config', default='lang-sync.yaml', help='Path to config file')
    parser.add_argument('--directory', default='.', help='Directory to extract files from')
    args = parser.parse_args()
    config = load_config(args.config)
    extracted_files = extract_files(args.directory, config)
    print(extracted_files)

if __name__ == '__main__':
    main()
