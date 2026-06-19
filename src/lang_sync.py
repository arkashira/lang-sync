import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Translation:
    source_text: str
    target_text: str
    source_lang: str
    target_lang: str

class TranslationEngine:
    def __init__(self, translations: Optional[Dict[str, Dict[str, str]]] = None):
        self.translations = translations or {}

    def add_translation(self, source_text: str, target_text: str, source_lang: str, target_lang: str) -> None:
        if source_lang not in self.translations:
            self.translations[source_lang] = {}
        self.translations[source_lang][source_text] = target_text

    def translate(self, text: str, source_lang: str, target_lang: str) -> Optional[str]:
        if source_lang in self.translations and text in self.translations[source_lang]:
            return self.translations[source_lang][text]
        return None

    def get_supported_languages(self) -> List[str]:
        return list(self.translations.keys())

    def save_to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            json.dump(self.translations, f)

    def load_from_file(self, file_path: str) -> None:
        with open(file_path, 'r') as f:
            self.translations = json.load(f)

class GitHubIntegration:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_pull_request(self, repo: str, title: str, body: str, head: str, base: str) -> Dict:
        # Simulate creating a pull request
        return {
            "repo": repo,
            "title": title,
            "body": body,
            "head": head,
            "base": base,
            "status": "created"
        }

class JenkinsIntegration:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def trigger_build(self, job_name: str, parameters: Dict) -> Dict:
        # Simulate triggering a build
        return {
            "job_name": job_name,
            "parameters": parameters,
            "status": "triggered"
        }
