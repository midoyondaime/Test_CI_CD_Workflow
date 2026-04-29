"""
Operation history tracker — logs all calculator operations.

This is a dependency we'll mock in tests (it's "external").
"""


class OperationHistory:
    """Tracks the history of calculator operations."""

    def __init__(self):
        self.entries = []

    def log(self, operation: str, result: float):
        """Log an operation with its result."""
        self.entries.append({"operation": operation, "result": result})

    def get_last(self):
        """Return the last logged operation."""
        return self.entries[-1] if self.entries else None

    def clear(self):
        """Clear all history."""
        self.entries.clear()

    def count(self):
        """Return number of operations logged."""
        return len(self.entries)
