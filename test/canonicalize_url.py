# coding: utf-8
# =============================================================================
# Ural URL Fingerprinting Unit Tests
# =============================================================================
from __future__ import unicode_literals

from ural import canonicalize_url

TESTS = [
    ("   http://lemonde.fr/test.html   ", "http://lemonde.fr/test.html"),
    ("http://lemonde.fr/test\x00.html", "http://lemonde.fr/test.html"),
    ("lemonde.fr", "https://lemonde.fr"),
    ("http://LEMONDE.FR/TEST", "http://lemonde.fr/TEST"),
    ("http://lemonde.fr:80/test", "http://lemonde.fr/test"),
    ("http://xn--tlrama-bvab.fr", "http://télérama.fr"),
    (
        "http://mozilla.org?x=%D1%88%D0%B5%D0%BB%D0%BB%D1%8B",
        "http://mozilla.org?x=шеллы",
    ),
    ("http://mozilla.org?x=шеллы", "http://mozilla.org?x=шеллы"),
    (
        "http://té%40%3A:té%40%3A@lemonde.fr/té%3F?%26té=%26té",
        "http://té%40%3A:té%40%3A@lemonde.fr/té%3F?%26té=%26té",
    ),
    (
        "http://t%C3%A9%40%3A:t%C3%A9%40%3A@lemonde.fr/t%C3%A9%3F?%26t%C3%A9=%26t%C3%A9",
        "http://té%40%3A:té%40%3A@lemonde.fr/té%3F?%26té=%26té",
    ),
]

TESTS_ADVANCED = [
    (
        "http://té%40%3A:té%40%3A@lemonde.fr/té%3F?%26té=%26té",
        "http://t%C3%A9%40%3A:t%C3%A9%40%3A@lemonde.fr/t%C3%A9%3F?%26t%C3%A9=%26t%C3%A9",
        {"quoted": True},
    ),
    (
        "http://t%C3%A9%40%3A:t%C3%A9%40%3A@lemonde.fr/t%C3%A9%3F?%26t%C3%A9=%26t%C3%A9",
        "http://t%C3%A9%40%3A:t%C3%A9%40%3A@lemonde.fr/t%C3%A9%3F?%26t%C3%A9=%26t%C3%A9",
        {"quoted": True},
    ),
]


class TestFingerprintUrl(object):
    def test_canonicalize_url(self):
        for url, result in TESTS:
            assert canonicalize_url(url) == result

        for url, result, kwargs in TESTS_ADVANCED:
            assert canonicalize_url(url, **kwargs) == result
