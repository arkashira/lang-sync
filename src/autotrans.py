import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Translation:
    text: str
    language: str
    confidence: float

class AutoTrans:
    def __init__(self, languages: List[str]):
        self.languages = languages
        self.translations = {}

    def translate(self, text: str, language: str) -> Translation:
        if language not in self.languages:
            raise ValueError(f"Unsupported language: {language}")

        # Simulate translation logic
        translated_text = f"{text} ({language})"
        confidence = 0.8 if language == "en" else 0.5

        return Translation(translated_text, language, confidence)

    def detect_language(self, text: str) -> str:
        # Simulate language detection logic
        if "hello" in text.lower():
            return "en"
        elif "bonjour" in text.lower():
            return "fr"
        else:
            return "unknown"

    def fallback_to_human_review(self, translation: Translation) -> bool:
        return translation.confidence < 0.7

    def add_translation(self, translation: Translation):
        self.translations[translation.language] = translation.text

    def get_translations(self) -> Dict[str, str]:
        return self.translations
