import math
from datetime import datetime, timedelta
from typing import List
from ast import Bytes

def convert_est(timestamp:str)->str:
    """Convert timestamp from PST to EST"""
    date = datetime.strptime(timestamp, "%m/%d/%y %I:%M:%S %p")
    date = date+timedelta(hours=3)
    return(date.strftime('%Y-%m-%dT%I:%M:%S.00Z'))

def pad_zip(zipcode:str)->str:
    """Zero Pad Zipcode"""
    return zipcode.rjust(5,'0')

def convert_timestamp(timestamp:str) -> str:
    """HH:MM:SS.MS format (where MS is milliseconds) to Seconds"""
    hour,minute,second = timestamp.split(":")
    second = math.ceil(float(second))
    total_seconds = int(hour) * 3600 + int(minute) * 60 + second
    return(str(total_seconds).rjust(12,"0"))

def unicode_parse(arr:List) -> List:
    """
    Parse columns for invalid characters, if invalid return empty row
    Also check if replacement character makes data unparseable
    """
    err_flag = False
    if not arr[0].isascii(): 
        sys.stderr.write(f"Invalid character found in Timestamp: {arr[0]}\n")
        err_flag = True
    elif not arr[2].isascii():
        sys.stderr.write(f"Invalid character found in ZIP: {arr[2]}\n")
        err_flag = True
    elif not arr[4].isascii():
        sys.stderr.write(f"Invalid character found in FooDuration: {arr[4]}\n")
        err_flag = True
    elif not arr[5].isascii():
        sys.stderr.write(f"Invalid character found in BarDuration: {arr[5]}\n")
        err_flag = True
    if err_flag:
        return([])
    return(arr)

def handle_unicode(data:Bytes) -> str:
    """
    Handle Unicode Decode Error by replacing invalid characters with �
    """
    converted_row = ''
    chars = [data[i:i + 1] for i in range(0, len(data), 1)]
    for char in chars:
        try:
            new_char = char.decode('utf-8')
            converted_row += new_char
        except UnicodeDecodeError:
            converted_row += u"\uFFFD"
    return(converted_row)

