#This file is part of numword.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
numword for EN
'''

from .numword_eu import NumWordEU


class NumWordEN(NumWordEU):
    '''
    NumWord EN
    '''

    def _set_high_numwords(self, high):
        '''
        Set high num words
        '''
        max_val = 3 + 3 * len(high)
        for word, i in zip(high, list(range(max_val, 3, -3))):
            self.cards[10 ** i] = word + "illion"

    def _setup(self):
        '''
        Setup
        '''
        self.negword = "minus "
        self.pointword = "point"
        self.exclude_title = ["and", "point", "minus"]

        self.mid_numwords = [
            (1000, "thousand"),
            (100, "hundred"),
            (90, "ninety"),
            (80, "eighty"),
            (70, "seventy"),
            (60, "sixty"),
            (50, "fifty"),
            (40, "forty"),
            (30, "thirty"),
            ]
        self.low_numwords = [
            "twenty",
            "nineteen",
            "eighteen",
            "seventeen",
            "sixteen",
            "fifteen",
            "fourteen",
            "thirteen",
            "twelve",
            "eleven",
            "ten",
            "nine",
            "eight",
            "seven",
            "six",
            "five",
            "four",
            "three",
            "two",
            "one",
            "zero",
            ]
        self.ords = {
            "one": "first",
            "two": "second",
            "three": "third",
            "five": "fifth",
            "eight": "eighth",
            "nine": "ninth",
            "twelve": "twelfth",
            }

    def _merge(self, curr, next):
        '''
        Merge
        '''
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1 and nnum < 100:
            return next
        elif 100 > cnum > nnum:
            return ("%s-%s" % (ctext, ntext), cnum + nnum)
        elif cnum >= 100 > nnum:
            return ("%s and %s" % (ctext, ntext), cnum + nnum)
        elif nnum > cnum:
            return ("%s %s" % (ctext, ntext), cnum * nnum)
        return ("%s, %s" % (ctext, ntext), cnum + nnum)

    def ordinal(self, value):
        '''
        Convert to ordinal
        '''
        self._verify_ordinal(value)
        outwords = self.cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie"
            lastword += "th"
        lastwords[-1] = self._title(lastword)
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)

    def ordinal_number(self, value):
        '''
        Convert to ordinal num
        '''
        self._verify_ordinal(value)
        return "%s%s" % (value, self.ordinal(value)[-2:])

    def year(self, val, longval=True):
        '''
        Convert to year
        '''
        if not (val // 100) % 10:
            return self.cardinal(val)
        return self._split(val, hightxt="hundred", jointxt="and",
            longval=longval)

    def currency(self, val, longval=True):
        '''
        Convert to currency
        '''
        return self._split(val, hightxt="dollar/s", lowtxt="cent/s",
            jointxt="and", longval=longval)


_NW = NumWordEN()


def cardinal(value):
    '''
    Convert to cardinal
    '''
    return _NW.cardinal(value)


def ordinal(value):
    '''
    Convert to ordinal
    '''
    return _NW.ordinal(value)


def ordinal_number(value):
    '''
    Convert to ordinal num
    '''
    return _NW.ordinal_number(value)


def currency(value, longval=True):
    '''
    Convert to currency
    '''
    return _NW.currency(value, longval=longval)


def year(value, longval=True):
    '''
    Convert to year
    '''
    return _NW.year(value, longval=longval)
