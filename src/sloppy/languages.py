"""Language detection and configuration."""

from __future__ import annotations

from enum import Enum
from pathlib import Path


class Language(Enum):
    """Supported languages."""

    PYTHON = "python"
    GO = "go"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"


# File extension to language mapping
EXTENSION_MAP = {
    ".py": Language.PYTHON,
    ".go": Language.GO,
    ".js": Language.JAVASCRIPT,
    ".jsx": Language.JAVASCRIPT,
    ".ts": Language.TYPESCRIPT,
    ".tsx": Language.TYPESCRIPT,
}


def detect_language(file_path: Path) -> Language | None:
    """Detect language from file extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Language enum or None if not supported
    """
    suffix = file_path.suffix.lower()
    return EXTENSION_MAP.get(suffix)


def get_supported_extensions(language: Language | None = None) -> list[str]:
    """Get list of supported file extensions.
    
    Args:
        language: If specified, returns extensions for that language only
        
    Returns:
        List of file extensions (including the dot)
    """
    if language is None:
        return list(EXTENSION_MAP.keys())
    return [ext for ext, lang in EXTENSION_MAP.items() if lang == language]


def get_language_from_name(name: str) -> Language | None:
    """Get Language enum from string name.
    
    Args:
        name: Language name (e.g., "python", "go", "javascript", "typescript")
        
    Returns:
        Language enum or None if not recognized
    """
    name_lower = name.lower()
    # Handle aliases
    if name_lower in ("js", "javascript"):
        return Language.JAVASCRIPT
    if name_lower in ("ts", "typescript"):
        return Language.TYPESCRIPT
    
    for lang in Language:
        if lang.value == name_lower:
            return lang
    return None
