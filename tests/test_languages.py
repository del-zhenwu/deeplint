"""Tests for language detection."""

from pathlib import Path

from sloppy.languages import (
    Language,
    detect_language,
    get_language_from_name,
    get_supported_extensions,
)


class TestLanguageDetection:
    """Test language detection from file extensions."""

    def test_detect_python(self) -> None:
        """Python files should be detected correctly."""
        assert detect_language(Path("test.py")) == Language.PYTHON
        assert detect_language(Path("/path/to/file.py")) == Language.PYTHON

    def test_detect_go(self) -> None:
        """Go files should be detected correctly."""
        assert detect_language(Path("main.go")) == Language.GO
        assert detect_language(Path("/path/to/main.go")) == Language.GO

    def test_detect_javascript(self) -> None:
        """JavaScript files should be detected correctly."""
        assert detect_language(Path("app.js")) == Language.JAVASCRIPT
        assert detect_language(Path("component.jsx")) == Language.JAVASCRIPT

    def test_detect_typescript(self) -> None:
        """TypeScript files should be detected correctly."""
        assert detect_language(Path("app.ts")) == Language.TYPESCRIPT
        assert detect_language(Path("component.tsx")) == Language.TYPESCRIPT

    def test_detect_unsupported(self) -> None:
        """Unsupported file types should return None."""
        assert detect_language(Path("file.txt")) is None
        assert detect_language(Path("file.rs")) is None
        assert detect_language(Path("file.java")) is None

    def test_case_insensitive(self) -> None:
        """File extension detection should be case insensitive."""
        assert detect_language(Path("test.PY")) == Language.PYTHON
        assert detect_language(Path("main.GO")) == Language.GO
        assert detect_language(Path("app.JS")) == Language.JAVASCRIPT


class TestGetLanguageFromName:
    """Test getting language enum from string name."""

    def test_python_names(self) -> None:
        """Python should be recognized."""
        assert get_language_from_name("python") == Language.PYTHON
        assert get_language_from_name("Python") == Language.PYTHON
        assert get_language_from_name("PYTHON") == Language.PYTHON

    def test_go_names(self) -> None:
        """Go should be recognized."""
        assert get_language_from_name("go") == Language.GO
        assert get_language_from_name("Go") == Language.GO

    def test_javascript_names(self) -> None:
        """JavaScript and aliases should be recognized."""
        assert get_language_from_name("javascript") == Language.JAVASCRIPT
        assert get_language_from_name("JavaScript") == Language.JAVASCRIPT
        assert get_language_from_name("js") == Language.JAVASCRIPT
        assert get_language_from_name("JS") == Language.JAVASCRIPT

    def test_typescript_names(self) -> None:
        """TypeScript and aliases should be recognized."""
        assert get_language_from_name("typescript") == Language.TYPESCRIPT
        assert get_language_from_name("TypeScript") == Language.TYPESCRIPT
        assert get_language_from_name("ts") == Language.TYPESCRIPT
        assert get_language_from_name("TS") == Language.TYPESCRIPT

    def test_unknown_names(self) -> None:
        """Unknown language names should return None."""
        assert get_language_from_name("rust") is None
        assert get_language_from_name("java") is None
        assert get_language_from_name("unknown") is None


class TestGetSupportedExtensions:
    """Test getting supported file extensions."""

    def test_all_extensions(self) -> None:
        """Should return all extensions when language is None."""
        exts = get_supported_extensions()
        assert ".py" in exts
        assert ".go" in exts
        assert ".js" in exts
        assert ".jsx" in exts
        assert ".ts" in exts
        assert ".tsx" in exts

    def test_python_extensions(self) -> None:
        """Should return only Python extensions."""
        exts = get_supported_extensions(Language.PYTHON)
        assert exts == [".py"]

    def test_go_extensions(self) -> None:
        """Should return only Go extensions."""
        exts = get_supported_extensions(Language.GO)
        assert exts == [".go"]

    def test_javascript_extensions(self) -> None:
        """Should return JavaScript extensions including JSX."""
        exts = get_supported_extensions(Language.JAVASCRIPT)
        assert ".js" in exts
        assert ".jsx" in exts

    def test_typescript_extensions(self) -> None:
        """Should return TypeScript extensions including TSX."""
        exts = get_supported_extensions(Language.TYPESCRIPT)
        assert ".ts" in exts
        assert ".tsx" in exts
