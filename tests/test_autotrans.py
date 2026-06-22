from autotrans import AutoTrans, Translation

def test_translate():
    autotrans = AutoTrans(["en", "fr"])
    translation = autotrans.translate("Hello, world!", "en")
    assert translation.text == "Hello, world! (en)"
    assert translation.language == "en"
    assert translation.confidence == 0.8

def test_translate_unsupported_language():
    autotrans = AutoTrans(["en", "fr"])
    try:
        autotrans.translate("Hello, world!", "es")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Unsupported language: es"

def test_detect_language():
    autotrans = AutoTrans(["en", "fr"])
    language = autotrans.detect_language("Hello, world!")
    assert language == "en"

def test_detect_unknown_language():
    autotrans = AutoTrans(["en", "fr"])
    language = autotrans.detect_language(" Foo bar")
    assert language == "unknown"

def test_fallback_to_human_review():
    autotrans = AutoTrans(["en", "fr"])
    translation = Translation("Hello, world! (fr)", "fr", 0.6)
    assert autotrans.fallback_to_human_review(translation)

def test_add_translation():
    autotrans = AutoTrans(["en", "fr"])
    translation = Translation("Hello, world! (en)", "en", 0.8)
    autotrans.add_translation(translation)
    assert autotrans.get_translations() == {"en": "Hello, world! (en)"}

def test_get_translations():
    autotrans = AutoTrans(["en", "fr"])
    translation1 = Translation("Hello, world! (en)", "en", 0.8)
    translation2 = Translation("Bonjour, monde! (fr)", "fr", 0.5)
    autotrans.add_translation(translation1)
    autotrans.add_translation(translation2)
    assert autotrans.get_translations() == {"en": "Hello, world! (en)", "fr": "Bonjour, monde! (fr)"}
