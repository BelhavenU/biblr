from collections import OrderedDict

short_to_long = OrderedDict([
    # Old
    ('ge', 'Genesis'), ('ex', 'Exodus'), ('le', 'Leviticus'),
    ('nu', 'Numbers'), ('de', 'Deuteronomy'), ('jos', 'Joshua'),
    ('jg', 'Judges'), ('ru', 'Ruth'),
    ('1sa', '1 Samuel'), ('2sa', '2 Samuel'), ('1ki', '1 Kings'),
    ('2ki', '2 Kings'), ('1ch', '1 Chronicles'), ('2ch', '2 Chronicles'), 
    ('ezr', 'Ezra'), ('ne', 'Nehemiah'), ('es', 'Esther'), ('job', 'Job'),
    ('ps', 'Psalms'), ('pr', 'Proverbs'), ('ec', 'Ecclesiastes'),
    ('song', 'Song of Solomon'), ('isa', 'Isaiah'), ('jer', 'Jeremiah'),
    ('la', 'Lamentations'), ('eze', 'Ezekiel'), ('da', 'Daniel'),
    ('ho', 'Hosea'), ('joe', 'Joel'), ('am', 'Amos'), ('ob', 'Obadiah'),
    ('jon', 'Jonah'), ('mic', 'Micah'), ('na', 'Nahum'), ('hab', 'Habakkuk'),
    ('zep', 'Zephaniah'), ('hag', 'Haggai'), ('zec', 'Zechariah'),
    ('mal', 'Malachi'),
    # New
    ('mt', 'Matthew'), ('mr', 'Mark'), ('lu', 'Luke'), ('joh', 'John'), 
    ('ac', 'Acts'), ('ro', 'Romans'), ('1co', '1 Corinthians'),
    ('2co', '2 Corinthians'), ('ga', 'Galatians'), ('eph', 'Ephesians'),
    ('php', 'Philippians'), ('col', 'Colossians'),
    ('1th', '1 Thessalonians'), ('2th', '2 Thessalonians'),
    ('1ti', '1 Timothy'), ('2ti', '2 Timothy'), ('tit', 'Titus'),
    ('phm', 'Philemon'), ('heb', 'Hebrews'), ('jas', 'James'),
    ('1pe', '1 Peter'), ('2pe', '2 Peter'), ('1jo', '1 John'),
    ('2jo', '2 John'), ('3jo', '3 John'), ('jude', 'Jude'),
    ('re', 'Revelation'),
])

testament_to_short = OrderedDict([
    ('old', [
        'ge', 'ex', 'le', 'nu', 'de', 'jos', 'jg', 'ru', '1sa', '2sa',
        '1ki', '2ki', '1ch', '2ch', 'ezr', 'ne', 'es', 'job', 'ps',
        'pr', 'ec', 'song', 'isa', 'jer', 'la', 'eze', 'da', 'ho', 'joe',
        'am', 'ob', 'jon', 'mic', 'na', 'hab', 'zep', 'hag', 'zec', 'mal',
    ]),

    ('new', [
        'mt', 'mr', 'lu', 'joh', 'ac', 'ro', '1co', '2co', 'ga', 'eph',
        'php', 'col', '1th', '2th', '1ti', '2ti', 'tit', 'phm', 'heb',
        'jas', '1pe', '2pe', '1jo', '2jo', '3jo', 'jude', 're',
    ]),
])

short_to_testament = OrderedDict([
    (s, t) for t in testament_to_short for s in testament_to_short[t]
])
