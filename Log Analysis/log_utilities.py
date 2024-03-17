import datetime
import time
from collections import defaultdict


def in_green(text: (int, str)) -> str:
    return "\033[32;1m" + str(text) + "\033[0m"


def add_or_create(dictionary: {}, key: str, value: [int, float] = 1):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value


def bytes_to_ip(these_bytes: bytes) -> str:
    ip = ""
    for this_byte in these_bytes:
        ip += str(this_byte) + "."
    return ip.rstrip(".")


def bytes_to_int(these_bytes: bytes) -> int:
    return int.from_bytes(these_bytes, "big")


def bytes_to_date(date_bytes: bytes) -> str:
    return time.strftime('%Y-%m-%d %H:%M', time.gmtime(int.from_bytes(date_bytes, "big")))


def timestamp_to_year(timestamp: str) -> str:
    date = datetime.datetime.utcfromtimestamp(float(timestamp))
    return str(date.year)


def in_quotes(line: str, num: int=1) -> str:
    """This returns what is inside a set of quotes. The num vaiable is which set of qotes.
        For example num=2 will return what is inside the 2nd set of quotes.
        ordinal based number (1,2,3,...) not 0 """
    # may need to remove escaped quotes for future challenges
    # quote_count = line.count('"')
    # if quote_count % 2 != 0:
    #   line.replace('//"', '')
    split_line = line.split('"')
    offset = 2 * (num - 1) + 1
    return split_line[offset]


def get_text_between(text: str, start: str, end: str) -> str:
    begin = text.find(start) + len(start)
    stop = text.find(end, begin)
    return text[begin:stop]


def get_key_with_longest_set(dict_of_sets: defaultdict) -> str:
    longest_set = None
    longest_set_key = ""
    for key, this_set in dict_of_sets.items():
        if longest_set is None or len(this_set) > len(longest_set):
            longest_set = this_set
            longest_set_key = key
    return longest_set_key
