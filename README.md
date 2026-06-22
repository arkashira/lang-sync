# AutoTrans
A Python library for translating localization strings in 50+ languages.

## Features

* Translate text in multiple languages
* Detect language-specific nuances
* Fallback to human review when confidence is low

## Usage

1. Install the library using `poetry install`
2. Import the library in your Python script: `from autotrans import AutoTrans`
3. Create an instance of the `AutoTrans` class: `autotrans = AutoTrans(["en", "fr"])`
4. Use the `translate` method to translate text: `translation = autotrans.translate("Hello, world!", "en")`

## Testing

Run the tests using `pytest`
