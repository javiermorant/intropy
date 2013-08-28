import unittest

class TestA1(unittest.TestCase):
    def test_seconds_difference(self):
        self.assertEqual(seconds_difference(1800.0, 3600.0), 1800.0)
        self.assertEqual(seconds_difference(3600.0, 1800.0), -1800.0)
        self.assertEqual(seconds_difference(1800.0, 2160.0), 360.0)
        self.assertEqual(seconds_difference(1800.0, 1800.0), 0)
    def test_hours_difference(self):
        self.assertEqual(hours_difference(1800.0, 3600.0),0.5)
        self.assertEqual(hours_difference(3600.0, 1800.0), -0.5)
        self.assertEqual(hours_difference(1800.0, 2160.0), 0.1)
        self.assertEqual(hours_difference(1800.0, 1800.0),0.0)
    def test_to_float_hours(self):
        self.assertEqual(to_float_hours(0, 15, 0),0.25)
        self.assertEqual(to_float_hours(2, 45, 9),2.7525)
        self.assertEqual(to_float_hours(1, 0, 36),1.01)
        
    def test_to_24_hour_clock(self):
        self.assertEqual(to_24_hour_clock(24),0)
        self.assertEqual(to_24_hour_clock(48),0)
        self.assertEqual(to_24_hour_clock(25),1)
        self.assertEqual(to_24_hour_clock(4),4)
        self.assertEqual(to_24_hour_clock(28.5),4.5)
    def test_get_hours(self):
        self.assertEqual(get_hours(0),0)
        self.assertEqual(get_hours(0),0)
        self.assertEqual(get_hours(3600),1)
        self.assertEqual(get_hours(3800),1)
    def test_get_minutes(self):
        self.assertEqual(get_minutes(0),0)
        self.assertEqual(get_minutes(120),2)
        self.assertEqual(get_minutes(1500),25)
        self.assertEqual(get_minutes(3600),0)
        self.assertEqual(get_minutes(3780),3)
    def test_get_seconds(self):
        self.assertEqual(get_seconds(0),0)
        self.assertEqual(get_seconds(122),2)
        self.assertEqual(get_seconds(1518),18)
        self.assertEqual(get_seconds(3600),0)
        self.assertEqual(get_seconds(3795),15)
    def test_time_to_utc(self):
        self.assertEqual(time_to_utc(+0, 12.0),12.0)
        self.assertEqual(time_to_utc(+1, 12.0),11.0)
        self.assertEqual(time_to_utc(-1, 12.0),13.0)
        self.assertEqual(time_to_utc(-11, 18.0),5.0)
        self.assertEqual(time_to_utc(-1, 0.0),1.0)
        self.assertEqual(time_to_utc(-1, 23.0),0.0)
    def test_time_from_utc(self):
        self.assertEqual(time_from_utc(+0, 12.0),12.0)
        self.assertEqual(time_from_utc(+1, 12.0),13.0)
        self.assertEqual(time_from_utc(-1, 12.0),11.0)
        self.assertEqual(time_from_utc(+6, 6.0),12.0)
        self.assertEqual(time_from_utc(-7, 6.0),23.0)
        self.assertEqual(time_from_utc(-1, 23.0),22.0)
        self.assertEqual(time_from_utc(+1, 23.0),0.0)

if __name__ == '__main__':
    unittest.main()
    
def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2-time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return seconds_difference(time_1,time_2)/3600



def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return hours+minutes/60+seconds/3600


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24



### Write your get_hours function definition here:
def get_hours(seconds):
    """(int)->int

    The parameter is a number of seconds since midnight.
    Return the number of hours that have elapsed since midnight,
    as seen on a 24-hour clock.
    (You should call to_24_hour_clock to convert the number of full hours
    to a time on a 24 hour clock.
    This means that the return value should be in the range 0 to 23, inclusive.) 

    Precondition: seconds >=0  seconds<86400

    >>>get_hours(0)
    0
    >>>get_hours(1500)
    0
    >>>get_hours(3600)
    1
    >>>get_hours(3800)
    1
    """
    return seconds//3600


### Write your get_minutes function definition here:
def get_minutes(seconds):
    """(int)->int

    The parameter is a number of seconds since midnight.
    Return the number of minutes that have elapsed since midnight
    as seen on a clock. (This means that the return value should be
    in the range 0 to 59, inclusive.) 

    Precondition: seconds >=0  seconds<86400
    >>>get_minutes(0)
    0
    >>>get_minutes(120)
    2
    >>>get_minutes(1500)
    25
    >>>get_minutes(3600)
    0
    >>>get_minutes(3780)
    3
    """
    return (seconds%3600)//60



### Write your get_seconds function definition here:
def get_seconds(seconds):
    """(int)->int

    The parameter is a number of seconds since midnight.
    Return the number of seconds that have elapsed since
    midnight as seen on a clock. (This means that the return
    value should be in the range 0 to 59, inclusive.) 

    Precondition: seconds >=0  seconds<86400
    >>>get_seconds(0)
    0
    >>>get_seconds(122)
    2
    >>>get_seconds(1518)
    18
    >>>get_seconds(3600)
    0
    >>>get_seconds(3795)
    15
    """
    return seconds%60



def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return to_24_hour_clock(time-utc_offset)


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return to_24_hour_clock(time+utc_offset)



