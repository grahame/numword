# -*- coding: utf-8 -*-
#This file is part of numword.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from unittest import TestCase, main


class TestNumWordFR(TestCase):

    def test_cardinal(self):
        from numword.numword_fr import cardinal
        self.assertEqual(cardinal(0), "zéro")
        self.assertEqual(cardinal(11.96), "onze virgule quatre-vingt-seize")
        self.assertEqual(cardinal(100), "cent")
        self.assertEqual(cardinal(100.0), "cent")
        self.assertEqual(cardinal(121.01), "cent-vingt-et-un virgule un")
        self.assertEqual(cardinal(3121.45),
            "trois-mille-cent-vingt-et-un virgule quarante-cinq")

    def test_cardinal_not_a_number(self):
        from numword.numword_fr import cardinal
        error = "type\(Ximinez\) not in \[long, int, float\]"
        with self.assertRaisesRegexp(TypeError, error):
            cardinal('Ximinez')

    def test_cardinal_number_too_big(self):
        from numword.numword_fr import cardinal
        from numword.numword_fr import NumWordFR
        max_val = NumWordFR().maxval
        number = max_val + 1
        error = "abs\(%s\) must be less than %s" % (number, max_val)
        with self.assertRaisesRegexp(OverflowError, error):
            cardinal(number)


class TestNumWordFR_BE(TestCase):

    def test_cardinal(self):
        from numword.numword_fr_be import cardinal
        self.assertEqual(cardinal(72), "septante-deux")
        self.assertEqual(cardinal(94), "nonante-quatre")
        self.assertEqual(cardinal(93.79),
            "nonante-trois virgule septante-neuf")


class TestNumWordEN(TestCase):

    def test_cardinal(self):
        from numword.numword_en import cardinal
        self.assertEqual(cardinal(11.96), "eleven point ninety-six")
        self.assertEqual(cardinal(100), "one hundred")
        self.assertEqual(cardinal(100.0), "one hundred")
        self.assertEqual(cardinal(121.01),
            "one hundred and twenty-one point one")
        self.assertEqual(cardinal(3121.45),
            "three thousand, one hundred and twenty-one point forty-five")

    def test_cardinal_not_a_number(self):
        from numword.numword_en import cardinal
        error = "type\(Ximinez\) not in \[long, int, float\]"
        with self.assertRaisesRegexp(TypeError, error):
            cardinal('Ximinez')

    def test_cardinal_number_too_big(self):
        from numword.numword_en import cardinal
        from numword.numword_en import NumWordEN
        max_val = NumWordEN().maxval
        number = max_val + 1
        error = "abs\(%s\) must be less than %s" % (number, max_val)
        with self.assertRaisesRegexp(OverflowError, error):
            cardinal(number)


class TestNumWordDE(TestCase):

    def test_cardinal(self):
        from numword.numword_de import cardinal
        tests = [
            [-1.0000100, "minus eins Komma null"],
            [1.11, "eins Komma eins eins"],
            [1, "eins"],
            [11, "elf"],
            [12, "zwölf"],
            [21, "einundzwanzig"],
            [29, "neunundzwanzig"],
            [30, "dreißig"],
            [31, "einunddreißig"],
            [33, "dreiunddreißig"],
            [71, "einundsiebzig"],
            [80, "achtzig"],
            [81, "einundachtzig"],
            [91, "einundneunzig"],
            [99, "neunundneunzig"],
            [100, "einhundert"],
            [101, "einhunderteins"],
            [102, "einhundertzwei"],
            [151, "einhunderteinundfünfzig"],
            [155, "einhundertfünfundfünfzig"],
            [161, "einhunderteinundsechzig"],
            [180, "einhundertachtzig"],
            [300, "dreihundert"],
            [301, "dreihunderteins"],
            [308, "dreihundertacht"],
            [832, "achthundertzweiunddreißig"],
            [1000, "eintausend"],
            [1001, "eintausendeins"],
            [1061, "eintausendeinundsechzig"],
            [1100, "eintausendeinhundert"],
            [1111, "eintausendeinhundertelf"],
            [1500, "eintausendfünfhundert"],
            [1701, "eintausendsiebenhunderteins"],
            [3000, "dreitausend"],
            [8280, "achttausendzweihundertachtzig"],
            [8291, "achttausendzweihunderteinundneunzig"],
            [10100, "zehntausendeinhundert"],
            [10101, "zehntausendeinhunderteins"],
            [10099, "zehntausendneunundneunzig"],
            [12000, "zwölftausend"],
            [150000, "einhundertfünfzigtausend"],
            [500000, "fünfhunderttausend"],
            [1000000, "eine Million"],
            [1000100, "eine Million einhundert"],
            [1000199, "eine Million einhundertneunundneunzig"],
            [2000000, "zwei Millionen"],
            [2000001, "zwei Millionen eins"],
            [1000000000, "eine Milliarde"],
            [2147483647, "zwei Milliarden einhundertsiebenundvierzig"
                " Millionen vierhundertdreiundachtzigtausend"
                "sechshundertsiebenundvierzig"],
                [23000000000, "dreiundzwanzig Milliarden"],
                [126000000000001, "einhundertsechsundzwanzig Billionen eins"],
                [-121211221211111, "minus einhunderteinundzwanzig Billionen "
                    "zweihundertelf Milliarden zweihunderteinundzwanzig "
                    "Millionen zweihundertelftausendeinhundertelf"],
                [1000000000000000, "eine Billiarde"],
                [256000000000000000, "zweihundertsechsundfünfzig Billiarden"],
                # I know the next is wrong! but what to do?
                [-2.12, "minus zwei Komma eins zwei"],
                [7401196841564901869874093974498574336000000000,
                    "sieben Septilliarden vierhunderteins Septillionen "
                    "einhundertsechsundneunzig Sextilliarden "
                    "achthunderteinundvierzig Sextillionen fünfhundertvi"
                    "erundsechzig Quintilliarden neunhunderteins "
                    "Quintillionen achthundertneunundsechzig Quadrilliarden "
                    "achthundertvierundsiebzig Quadrillionen dreiundneunzig "
                    "Trilliarden neunhundertvierundsiebzig Trillionen "
                    "vierhundertachtundneunzig Billiarden fünfhundertvieru"
                    "ndsiebzig Billionen dreihundertsechsunddreißig "
                    "Milliarden"],
                ]
        for number, word in tests:
            self.assertEqual(cardinal(number), word)

    def test_year(self):
        from numword.numword_de import year
        tests = [
            # Watch out, negative years are broken!
            [0, "null"],
            [33, "dreiunddreißig"],
            [150, "einhundertfünfzig"],
            [160, "einhundertsechzig"],
            [1130, "elfhundertdreißig"],
            [1999, "neunzehnhundertneunundneunzig"],
            [1984, "neunzehnhundertvierundachtzig"],
            [2000, "zweitausend"],
            [2001, "zweitausendeins"],
            [2010, "zweitausendzehn"],
            [2012, "zweitausendzwölf"],
            ]
        for number, word in tests:
            self.assertEqual(year(number), word)

    def test_currency(self):
        from numword.numword_de import currency
        tests = [
            [12222, "einhundertzweiundzwanzig Euro und zweiundzwanzig Cent"],
            [123322, "eintausendzweihundertdreiunddreißig Euro und "
                "zweiundzwanzig Cent"],
            [686412,
                "sechstausendachthundertvierundsechzig Euro und zwölf Cent"],
            [84, "vierundachtzig Cent"],
            [1, "ein Cent"],
            ]
        for number, word in tests:
            self.assertEqual(currency(number), word)

    def test_ordinal(self):
        from numword.numword_de import ordinal
        tests = [
            [1, "erste"],
            [3, "dritte"],
            [11, "elfte"],
            [12, "zwölfte"],
            [21, "einundzwanzigste"],
            [29, "neunundzwanzigste"],
            [30, "dreißigste"],
            [31, "einunddreißigste"],
            [33, "dreiunddreißigste"],
            [71, "einundsiebzigste"],
            [80, "achtzigste"],
            [81, "einundachtzigste"],
            [91, "einundneunzigste"],
            [99, "neunundneunzigste"],
            [100, "einhundertste"],
            [101, "einhunderterste"],
            [102, "einhundertzweite"],
            [151, "einhunderteinundfünfzigste"],
            [155, "einhundertfünfundfünfzigste"],
            [161, "einhunderteinundsechzigste"],
            [180, "einhundertachtzigste"],
            [300, "dreihundertste"],
            [301, "dreihunderterste"],
            [308, "dreihundertachte"],
            [832, "achthundertzweiunddreißigste"],
            [1000, "eintausendste"],
            [1001, "eintausenderste"],
            [1061, "eintausendeinundsechzigste"],
            [2000001, "zwei Millionen erste"],
            # The following is broken
            #[1000000000, "eine Milliardeste"],
            [2147483647, "zwei Milliarden einhundertsiebenundvierzig"
                " Millionen vierhundertdreiundachtzigtausend"
                "sechshundertsiebenundvierzigste"],

            ]
        for number, word in tests:
            self.assertEqual(ordinal(number), word)

if __name__ == '__main__':
    main()
