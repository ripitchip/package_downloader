# Created Date: Thursday, January 11th 2024, 6:42:14 pm
# Created By: BriocheAF
# Copyright (c) 2024 BriocheAF
# -----
# Last Modified: Thursday, January 11th 2024, 6:45:20 pm
# Modified By: BriocheAF
from src.main import main


def test_main() -> None:
    """Test main function."""
    if not main() == "Hello World!":
        raise ValueError("Wrong value returned by main function.")
