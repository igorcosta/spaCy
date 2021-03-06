# encoding: utf8
from __future__ import unicode_literals

import pytest


DEFAULT_TESTS = [
    ('N. kormányzósági\nszékhely.', ['N.', 'kormányzósági', 'székhely', '.']),
    ('A .hu egy tld.', ['A', '.hu', 'egy', 'tld', '.']),
    ('Az egy.ketto pelda.', ['Az', 'egy.ketto', 'pelda', '.']),
    ('A pl. rovidites.', ['A', 'pl.', 'rovidites', '.']),
    ('A S.M.A.R.T. szo.', ['A', 'S.M.A.R.T.', 'szo', '.']),
    ('A .hu.', ['A', '.hu', '.']),
    ('Az egy.ketto.', ['Az', 'egy.ketto', '.']),
    ('A pl.', ['A', 'pl.']),
    ('A S.M.A.R.T.', ['A', 'S.M.A.R.T.']),
    ('Egy..ket.', ['Egy', '..', 'ket', '.']),
    ('Valami... van.', ['Valami', '...', 'van', '.']),
    ('Valami ...van...', ['Valami', '...', 'van', '...']),
    ('Valami...', ['Valami', '...']),
    ('Valami ...', ['Valami', '...']),
    ('Valami ... más.', ['Valami', '...', 'más', '.'])
]

HYPHEN_TESTS = [
    ('Egy -nak, -jaiért, -magyar, bel- van.', ['Egy', '-nak', ',', '-jaiért', ',', '-magyar', ',', 'bel-', 'van', '.']),
    ('Egy -nak.', ['Egy', '-nak', '.']),
    ('Egy bel-.', ['Egy', 'bel-', '.']),
    ('Dinnye-domb-.', ['Dinnye-domb-', '.']),
    ('Ezen -e elcsatangolt.', ['Ezen', '-e', 'elcsatangolt', '.']),
    ('Lakik-e', ['Lakik', '-e']),
    ('Lakik-e?', ['Lakik', '-e', '?']),
    ('Lakik-e.', ['Lakik', '-e', '.']),
    ('Lakik-e...', ['Lakik', '-e', '...']),
    ('Lakik-e... van.', ['Lakik', '-e', '...', 'van', '.']),
    ('Lakik-e van?', ['Lakik', '-e', 'van', '?']),
    ('Lakik-elem van?', ['Lakik-elem', 'van', '?']),
    ('Van lakik-elem.', ['Van', 'lakik-elem', '.']),
    ('A 7-es busz?', ['A', '7-es', 'busz', '?']),
    ('A 7-es?', ['A', '7-es', '?']),
    ('A 7-es.', ['A', '7-es', '.']),
    ('Ez (lakik)-e?', ['Ez', '(', 'lakik', ')', '-e', '?']),
    ('A %-sal.', ['A', '%-sal', '.']),
    ('A CD-ROM-okrol.', ['A', 'CD-ROM-okrol', '.'])
]

NUMBER_TESTS = [
    ('A 2b van.', ['A', '2b', 'van', '.']),
    ('A 2b-ben van.', ['A', '2b-ben', 'van', '.']),
    ('A 2b.', ['A', '2b', '.']),
    ('A 2b-ben.', ['A', '2b-ben', '.']),
    ('A 3.b van.', ['A', '3.b', 'van', '.']),
    ('A 3.b-ben van.', ['A', '3.b-ben', 'van', '.']),
    ('A 3.b.', ['A', '3.b', '.']),
    ('A 3.b-ben.', ['A', '3.b-ben', '.']),
    ('A 1:20:36.7 van.', ['A', '1:20:36.7', 'van', '.']),
    ('A 1:20:36.7-ben van.', ['A', '1:20:36.7-ben', 'van', '.']),
    ('A 1:20:36.7-ben.', ['A', '1:20:36.7-ben', '.']),
    ('A 1:35 van.', ['A', '1:35', 'van', '.']),
    ('A 1:35-ben van.', ['A', '1:35-ben', 'van', '.']),
    ('A 1:35-ben.', ['A', '1:35-ben', '.']),
    ('A 1.35 van.', ['A', '1.35', 'van', '.']),
    ('A 1.35-ben van.', ['A', '1.35-ben', 'van', '.']),
    ('A 1.35-ben.', ['A', '1.35-ben', '.']),
    ('A 4:01,95 van.', ['A', '4:01,95', 'van', '.']),
    ('A 4:01,95-ben van.', ['A', '4:01,95-ben', 'van', '.']),
    ('A 4:01,95-ben.', ['A', '4:01,95-ben', '.']),
    ('A 10--12 van.', ['A', '10--12', 'van', '.']),
    ('A 10--12-ben van.', ['A', '10--12-ben', 'van', '.']),
    ('A 10--12-ben.', ['A', '10--12-ben', '.']),
    ('A 10‐12 van.', ['A', '10‐12', 'van', '.']),
    ('A 10‐12-ben van.', ['A', '10‐12-ben', 'van', '.']),
    ('A 10‐12-ben.', ['A', '10‐12-ben', '.']),
    ('A 10‑12 van.', ['A', '10‑12', 'van', '.']),
    ('A 10‑12-ben van.', ['A', '10‑12-ben', 'van', '.']),
    ('A 10‑12-ben.', ['A', '10‑12-ben', '.']),
    ('A 10‒12 van.', ['A', '10‒12', 'van', '.']),
    ('A 10‒12-ben van.', ['A', '10‒12-ben', 'van', '.']),
    ('A 10‒12-ben.', ['A', '10‒12-ben', '.']),
    ('A 10–12 van.', ['A', '10–12', 'van', '.']),
    ('A 10–12-ben van.', ['A', '10–12-ben', 'van', '.']),
    ('A 10–12-ben.', ['A', '10–12-ben', '.']),
    ('A 10—12 van.', ['A', '10—12', 'van', '.']),
    ('A 10—12-ben van.', ['A', '10—12-ben', 'van', '.']),
    ('A 10—12-ben.', ['A', '10—12-ben', '.']),
    ('A 10―12 van.', ['A', '10―12', 'van', '.']),
    ('A 10―12-ben van.', ['A', '10―12-ben', 'van', '.']),
    ('A 10―12-ben.', ['A', '10―12-ben', '.']),
    ('A -23,12 van.', ['A', '-23,12', 'van', '.']),
    ('A -23,12-ben van.', ['A', '-23,12-ben', 'van', '.']),
    ('A -23,12-ben.', ['A', '-23,12-ben', '.']),
    ('A 2+3 van.', ['A', '2', '+', '3', 'van', '.']),
    ('A 2 +3 van.', ['A', '2', '+', '3', 'van', '.']),
    ('A 2+ 3 van.', ['A', '2', '+', '3', 'van', '.']),
    ('A 2 + 3 van.', ['A', '2', '+', '3', 'van', '.']),
    ('A 2*3 van.', ['A', '2', '*', '3', 'van', '.']),
    ('A 2 *3 van.', ['A', '2', '*', '3', 'van', '.']),
    ('A 2* 3 van.', ['A', '2', '*', '3', 'van', '.']),
    ('A 2 * 3 van.', ['A', '2', '*', '3', 'van', '.']),
    ('A C++ van.', ['A', 'C++', 'van', '.']),
    ('A C++-ben van.', ['A', 'C++-ben', 'van', '.']),
    ('A C++.', ['A', 'C++', '.']),
    ('A C++-ben.', ['A', 'C++-ben', '.']),
    ('A 2003. I. 06. van.', ['A', '2003.', 'I.', '06.', 'van', '.']),
    ('A 2003. I. 06-ben van.', ['A', '2003.', 'I.', '06-ben', 'van', '.']),
    ('A 2003. I. 06.', ['A', '2003.', 'I.', '06.']),
    ('A 2003. I. 06-ben.', ['A', '2003.', 'I.', '06-ben', '.']),
    ('A 2003. 01. 06. van.', ['A', '2003.', '01.', '06.', 'van', '.']),
    ('A 2003. 01. 06-ben van.', ['A', '2003.', '01.', '06-ben', 'van', '.']),
    ('A 2003. 01. 06.', ['A', '2003.', '01.', '06.']),
    ('A 2003. 01. 06-ben.', ['A', '2003.', '01.', '06-ben', '.']),
    ('A IV. 12. van.', ['A', 'IV.', '12.', 'van', '.']),
    ('A IV. 12-ben van.', ['A', 'IV.', '12-ben', 'van', '.']),
    ('A IV. 12.', ['A', 'IV.', '12.']),
    ('A IV. 12-ben.', ['A', 'IV.', '12-ben', '.']),
    ('A 2003.01.06. van.', ['A', '2003.01.06.', 'van', '.']),
    ('A 2003.01.06-ben van.', ['A', '2003.01.06-ben', 'van', '.']),
    ('A 2003.01.06.', ['A', '2003.01.06.']),
    ('A 2003.01.06-ben.', ['A', '2003.01.06-ben', '.']),
    ('A IV.12. van.', ['A', 'IV.12.', 'van', '.']),
    ('A IV.12-ben van.', ['A', 'IV.12-ben', 'van', '.']),
    ('A IV.12.', ['A', 'IV.12.']),
    ('A IV.12-ben.', ['A', 'IV.12-ben', '.']),
    ('A 1.1.2. van.', ['A', '1.1.2.', 'van', '.']),
    ('A 1.1.2-ben van.', ['A', '1.1.2-ben', 'van', '.']),
    ('A 1.1.2.', ['A', '1.1.2.']),
    ('A 1.1.2-ben.', ['A', '1.1.2-ben', '.']),
    ('A 1,5--2,5 van.', ['A', '1,5--2,5', 'van', '.']),
    ('A 1,5--2,5-ben van.', ['A', '1,5--2,5-ben', 'van', '.']),
    ('A 1,5--2,5-ben.', ['A', '1,5--2,5-ben', '.']),
    ('A 3,14 van.', ['A', '3,14', 'van', '.']),
    ('A 3,14-ben van.', ['A', '3,14-ben', 'van', '.']),
    ('A 3,14-ben.', ['A', '3,14-ben', '.']),
    ('A 3.14 van.', ['A', '3.14', 'van', '.']),
    ('A 3.14-ben van.', ['A', '3.14-ben', 'van', '.']),
    ('A 3.14-ben.', ['A', '3.14-ben', '.']),
    ('A 15. van.', ['A', '15.', 'van', '.']),
    ('A 15-ben van.', ['A', '15-ben', 'van', '.']),
    ('A 15-ben.', ['A', '15-ben', '.']),
    ('A 15.-ben van.', ['A', '15.-ben', 'van', '.']),
    ('A 15.-ben.', ['A', '15.-ben', '.']),
    ('A 2002--2003. van.', ['A', '2002--2003.', 'van', '.']),
    ('A 2002--2003-ben van.', ['A', '2002--2003-ben', 'van', '.']),
    ('A 2002--2003-ben.', ['A', '2002--2003-ben', '.']),
    ('A -0,99% van.', ['A', '-0,99%', 'van', '.']),
    ('A -0,99%-ben van.', ['A', '-0,99%-ben', 'van', '.']),
    ('A -0,99%.', ['A', '-0,99%', '.']),
    ('A -0,99%-ben.', ['A', '-0,99%-ben', '.']),
    ('A 10--20% van.', ['A', '10--20%', 'van', '.']),
    ('A 10--20%-ben van.', ['A', '10--20%-ben', 'van', '.']),
    ('A 10--20%.', ['A', '10--20%', '.']),
    ('A 10--20%-ben.', ['A', '10--20%-ben', '.']),
    ('A 99§ van.', ['A', '99§', 'van', '.']),
    ('A 99§-ben van.', ['A', '99§-ben', 'van', '.']),
    ('A 99§-ben.', ['A', '99§-ben', '.']),
    ('A 10--20§ van.', ['A', '10--20§', 'van', '.']),
    ('A 10--20§-ben van.', ['A', '10--20§-ben', 'van', '.']),
    ('A 10--20§-ben.', ['A', '10--20§-ben', '.']),
    ('A 99° van.', ['A', '99°', 'van', '.']),
    ('A 99°-ben van.', ['A', '99°-ben', 'van', '.']),
    ('A 99°-ben.', ['A', '99°-ben', '.']),
    ('A 10--20° van.', ['A', '10--20°', 'van', '.']),
    ('A 10--20°-ben van.', ['A', '10--20°-ben', 'van', '.']),
    ('A 10--20°-ben.', ['A', '10--20°-ben', '.']),
    ('A °C van.', ['A', '°C', 'van', '.']),
    ('A °C-ben van.', ['A', '°C-ben', 'van', '.']),
    ('A °C.', ['A', '°C', '.']),
    ('A °C-ben.', ['A', '°C-ben', '.']),
    ('A 100°C van.', ['A', '100°C', 'van', '.']),
    ('A 100°C-ben van.', ['A', '100°C-ben', 'van', '.']),
    ('A 100°C.', ['A', '100°C', '.']),
    ('A 100°C-ben.', ['A', '100°C-ben', '.']),
    ('A 800x600 van.', ['A', '800x600', 'van', '.']),
    ('A 800x600-ben van.', ['A', '800x600-ben', 'van', '.']),
    ('A 800x600-ben.', ['A', '800x600-ben', '.']),
    ('A 1x2x3x4 van.', ['A', '1x2x3x4', 'van', '.']),
    ('A 1x2x3x4-ben van.', ['A', '1x2x3x4-ben', 'van', '.']),
    ('A 1x2x3x4-ben.', ['A', '1x2x3x4-ben', '.']),
    ('A 5/J van.', ['A', '5/J', 'van', '.']),
    ('A 5/J-ben van.', ['A', '5/J-ben', 'van', '.']),
    ('A 5/J-ben.', ['A', '5/J-ben', '.']),
    ('A 5/J. van.', ['A', '5/J.', 'van', '.']),
    ('A 5/J.-ben van.', ['A', '5/J.-ben', 'van', '.']),
    ('A 5/J.-ben.', ['A', '5/J.-ben', '.']),
    ('A III/1 van.', ['A', 'III/1', 'van', '.']),
    ('A III/1-ben van.', ['A', 'III/1-ben', 'van', '.']),
    ('A III/1-ben.', ['A', 'III/1-ben', '.']),
    ('A III/1. van.', ['A', 'III/1.', 'van', '.']),
    ('A III/1.-ben van.', ['A', 'III/1.-ben', 'van', '.']),
    ('A III/1.-ben.', ['A', 'III/1.-ben', '.']),
    ('A III/c van.', ['A', 'III/c', 'van', '.']),
    ('A III/c-ben van.', ['A', 'III/c-ben', 'van', '.']),
    ('A III/c.', ['A', 'III/c', '.']),
    ('A III/c-ben.', ['A', 'III/c-ben', '.']),
    ('A TU–154 van.', ['A', 'TU–154', 'van', '.']),
    ('A TU–154-ben van.', ['A', 'TU–154-ben', 'van', '.']),
    ('A TU–154-ben.', ['A', 'TU–154-ben', '.'])
]

QUOTE_TESTS = [
    ('Az "Ime, hat"-ban irja.', ['Az', '"', 'Ime', ',', 'hat', '"', '-ban', 'irja', '.']),
    ('"Ime, hat"-ban irja.', ['"', 'Ime', ',', 'hat', '"', '-ban', 'irja', '.']),
    ('Az "Ime, hat".', ['Az', '"', 'Ime', ',', 'hat', '"', '.']),
    ('Egy 24"-os monitor.', ['Egy', '24', '"', '-os', 'monitor', '.']),
    ("A don't van.", ['A', "don't", 'van', '.'])
]

DOT_TESTS = [
    ('N. kormányzósági\nszékhely.', ['N.', 'kormányzósági', 'székhely', '.']),
    ('A .hu egy tld.', ['A', '.hu', 'egy', 'tld', '.']),
    ('Az egy.ketto pelda.', ['Az', 'egy.ketto', 'pelda', '.']),
    ('A pl. rovidites.', ['A', 'pl.', 'rovidites', '.']),
    ('A S.M.A.R.T. szo.', ['A', 'S.M.A.R.T.', 'szo', '.']),
    ('A .hu.', ['A', '.hu', '.']),
    ('Az egy.ketto.', ['Az', 'egy.ketto', '.']),
    ('A pl.', ['A', 'pl.']),
    ('A S.M.A.R.T.', ['A', 'S.M.A.R.T.']),
    ('Egy..ket.', ['Egy', '..', 'ket', '.']),
    ('Valami... van.', ['Valami', '...', 'van', '.']),
    ('Valami ...van...', ['Valami', '...', 'van', '...']),
    ('Valami...', ['Valami', '...']),
    ('Valami ...', ['Valami', '...']),
    ('Valami ... más.', ['Valami', '...', 'más', '.'])
]


TESTCASES = DEFAULT_TESTS + HYPHEN_TESTS + NUMBER_TESTS + DOT_TESTS + QUOTE_TESTS


@pytest.mark.parametrize('text,expected_tokens', TESTCASES)
def test_tokenizer_handles_testcases(hu_tokenizer, text, expected_tokens):
    tokens = hu_tokenizer(text)
    token_list = [token.text for token in tokens if not token.is_space]
    assert expected_tokens == token_list
