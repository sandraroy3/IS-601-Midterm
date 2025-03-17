import pytest
from app.plugins.divide import DivideCommand

def test_multiprocessing_divide(capsys):
    """
    Tests whether DivideCommand executes correctly.
    Runs `execute()` directly to capture stdout instead of using multiprocessing.
    """
    command = DivideCommand()
    
    # Run command directly to capture output
    command.execute(10, 2)

    # Capture printed output
    captured = capsys.readouterr()
    
    # Assert expected result
    assert "Result = 5.0" in captured.out
