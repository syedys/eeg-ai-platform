import eeg_ai_platform


def test_package_metadata():
    assert eeg_ai_platform.__version__ == "0.1.0"


def test_hello_message():
    assert eeg_ai_platform.hello() == "EEG AI Platform ready for development."
