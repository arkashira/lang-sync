import pytest
from lang_sync import TranslationEngine, GitHubIntegration, JenkinsIntegration

@pytest.fixture
def translation_engine():
    engine = TranslationEngine()
    engine.add_translation("Hello", "Hola", "en", "es")
    engine.add_translation("Goodbye", "Adiós", "en", "es")
    return engine

def test_add_translation(translation_engine):
    translation_engine.add_translation("Thank you", "Gracias", "en", "es")
    assert translation_engine.translate("Thank you", "en", "es") == "Gracias"

def test_translate(translation_engine):
    assert translation_engine.translate("Hello", "en", "es") == "Hola"
    assert translation_engine.translate("Goodbye", "en", "es") == "Adiós"
    assert translation_engine.translate("Unknown", "en", "es") is None

def test_get_supported_languages(translation_engine):
    assert "en" in translation_engine.get_supported_languages()

def test_save_and_load(translation_engine, tmp_path):
    file_path = tmp_path / "translations.json"
    translation_engine.save_to_file(file_path)
    new_engine = TranslationEngine()
    new_engine.load_from_file(file_path)
    assert new_engine.translate("Hello", "en", "es") == "Hola"

def test_github_integration():
    github = GitHubIntegration("test_api_key")
    pr = github.create_pull_request("test_repo", "Test PR", "Test body", "test_branch", "main")
    assert pr["status"] == "created"

def test_jenkins_integration():
    jenkins = JenkinsIntegration("test_api_key")
    build = jenkins.trigger_build("test_job", {"param1": "value1"})
    assert build["status"] == "triggered"
