import os
from dataclasses import dataclass
from dotenv import load_dotenv


"""
This file stores the application configuration class. We can either load to the application config by using environment
variables or by direct declaration in the `__init__` method.
"""


@dataclass
class Config:
    """Holds application configuration"""

    sample_config: str
    another_config: str
    app_name: str = "Dash Starter App"
    update_title: str = "Loading"

    def __init__(self):
        # Inject environment variables from local file
        load_dotenv()
        self.sample_config = os.getenv("SAMPLE_CONFIG")
        self.another_config = "bar"


# Singleton configuration instance
app_config = Config()
