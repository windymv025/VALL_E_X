NUM_LAYERS = 12
NUM_HEAD = 16
N_DIM = 1024
PREFIX_MODE = 1
NUM_QUANTIZERS = 8
SAMPLE_RATE = 24000

lang2token = {
    'zh': "[ZH]",
    'ja': "[JA]",
    "en": "[EN]",
    "vi": "[VI]",
    'mix': "",
}

lang2code = {
    'zh': 0,
    'ja': 1,
    "en": 2,
    "vi": 3
}

token2lang = {
    '[ZH]': "zh",
    '[JA]': "ja",
    "[EN]": "en",
    "[VI]": "vi",
    "": "mix"
}

code2lang = {
    0: 'zh',
    1: 'ja',
    2: "en",
    3: "vi",
}

langdropdown2token = {
    'English': "[EN]",
    '中文': "[ZH]",
    '日本語': "[JA]",
    'Tiếng Việt': "VI",
    'Mix': "",
}