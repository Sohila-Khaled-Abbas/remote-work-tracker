"""
We Work Remotely Scraper Package
--------------------------------
This module initializes the Scrapy project for scraping remote job listings 
from WeWorkRemotely.com.

Purpose:
    - Defines the root package for the wwr_scraper.
    - Ensures relative imports work correctly.
    - Enables external modules (ETL pipeline, orchestration scripts, etc.)
      to import Scrapy spiders and items cleanly.

Author: Sohila Khaled Abbas
Version: 1.0
Created: 2025-10-14
"""

# ✅ Standard library imports
import os
import sys

# ✅ Ensure Python can resolve relative imports when running scrapy commands
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

# ✅ Scrapy utilities (for serialization if needed later)
try:
    from scrapy.utils.request import request_to_dict, request_from_dict
except ImportError:
    # Compatibility fallback for older Scrapy versions
    request_to_dict = None
    request_from_dict = None

# ✅ Version and metadata
__version__ = "1.0"
__author__ = "Sohila Khaled Abbas"
__description__ = "Scrapy project for extracting remote job postings from We Work Remotely."
__project_name__ = "wwr_scraper"

# ✅ Optional: define a logger for package-level debugging
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info(f"Initialized {__project_name__} v{__version__}")
logger.info(f"Author: {__author__}")