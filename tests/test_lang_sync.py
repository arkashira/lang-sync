from lang_sync import LangSync, TranslationFile

def test_create_branch():
    lang_sync = LangSync("test-branch", [])
    assert lang_sync.create_branch() == "translations/test-branch"

def test_commit_translated_files():
    lang_sync = LangSync("test-branch", [TranslationFile("file1.txt", "content1")])
    assert lang_sync.commit_translated_files() == "Translated files for test-branch"

def test_delete_branch():
    lang_sync = LangSync("test-branch", [])
    # Test that delete_branch doesn't raise an exception
    lang_sync.delete_branch()

def test_main():
    # Test that main doesn't raise an exception
    import sys
    sys.argv = ["lang_sync.py", "--branch-name", "test-branch", "--translated-files", "file1.txt:content1"]
    from src.lang_sync import main
    main()
