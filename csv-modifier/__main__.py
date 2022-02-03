#! /usr/bin/env python3

"""
CSV-modifier: takes a CSV file and uses the OpenAI GPT-3 API to process it
"""

import sys
import os
import configparser

if __name__ == "__main__":
    # Checking if the user is using the correct version of Python
    # Reference:
    #  If Python version is 3.6.5
    #               major --^
    #               minor ----^
    #               micro ------^
    major = sys.version_info[0]
    minor = sys.version_info[1]

    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    if major != 3 or major == 3 and minor < 6:
        print("CSV-modifier requires Python 3.6+\nYou are using Python %s, which is not supported" % (python_version))
        sys.exit(1)

    main_config = configparser.ConfigParser()
    main_config.read(os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini', encoding='utf-8')

    from CsvModifier import CsvModifier

    csv_modifier = CsvModifier(dict(main_config.items('OPTIONS')))
    csv_modifier.generate()