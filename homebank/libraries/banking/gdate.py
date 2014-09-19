from datetime import date, timedelta


GDATE_1970 = 719163
DT_1970 = date(1970, 1, 1)


def from_gdate(something):
    return DT_1970 + timedelta(days=something - GDATE_1970)


def to_gdate(date):
    return GDATE_1970 + (date - DT_1970).days
