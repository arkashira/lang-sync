import os
import pytest
from lang_sync import Config, load_config, extract_files
import logging

@pytest.fixture
def temp_config_file(tmp_path):
    config_file = tmp_path / 'lang-sync.yaml'
    with open(config_file, 'w') as file:
        file.write(''' 
include_patterns:
  - "*.py"
  - "*.java"
exclude_patterns:
  - "test*"
  - "example*"
''')
    return config_file

def test_load_config(temp_config_file):
    config = load_config(temp_config_file)
    assert config.include_patterns == ['*.py', '*.java']
    assert config.exclude_patterns == ['test*', 'example*']

def test_load_config_default():
    config = load_config('non_existent_file.yaml')
    assert config.include_patterns == ['*.py', '*.java', '*.cpp']
    assert config.exclude_patterns == ['test*', 'example*']

def test_extract_files(temp_config_file, tmp_path):
    # Create test files
    test_file = tmp_path / 'test.py'
    example_file = tmp_path / 'example.java'
    normal_file = tmp_path / 'normal.py'
    with open(test_file, 'w') as file:
        file.write('Test file')
    with open(example_file, 'w') as file:
        file.write('Example file')
    with open(normal_file, 'w') as file:
        file.write('Normal file')
    config = load_config(temp_config_file)
    extracted_files = extract_files(tmp_path, config)
    assert len(extracted_files) == 1
    assert extracted_files[0] == str(normal_file)

def test_extract_files_empty_directory(tmp_path):
    config = Config(include_patterns=['*.py'], exclude_patterns=[])
    extracted_files = extract_files(tmp_path, config)
    assert len(extracted_files) == 0

def test_extract_files_no_config_file(tmp_path):
    config = load_config('non_existent_file.yaml')
    extracted_files = extract_files(tmp_path, config)
    assert len(extracted_files) == 0
