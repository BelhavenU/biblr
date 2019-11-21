import csv
import bz2
from pathlib import Path

from pkg_resources import resource_filename

def get_data_path(filename: str):
    return Path(resource_filename(__name__, filename))

def get_all_verses():
    with bz2.open(get_data_path('kjv.tsv.bz2'), 'rt') as rfp:
        for row in csv.reader(rfp, delimiter='\t'):
            yield verse_dict(*row)

def verse_dict(b, c, v, text):
    return {
        'b': b, 'c': c, 'v': v, 'text': text,
    }


