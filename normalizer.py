import sys 
import csv
from helpers import handle_unicode, convert_est, convert_timestamp, unicode_parse, pad_zip

def main():
    header_flag = True
    decoded_input = []
    for row in sys.stdin.buffer.raw:
        try:
            decoded = row.decode('utf-8')
        except UnicodeDecodeError:
            decoded = handle_unicode(row)
        decoded_input.append(decoded)

    for row in csv.reader(decoded_input):
        if header_flag:
            header_flag = False
            print(",".join(row))
            continue
        parsed_row = unicode_parse(row)
        if parsed_row:
            row[0] = convert_est(parsed_row[0])
            row[1] = f'"{parsed_row[1]}"'
            row[2] = pad_zip(parsed_row[2])
            row[3] = parsed_row[3].upper()
            row[4] = convert_timestamp(parsed_row[4])
            row[5] = convert_timestamp(parsed_row[5])
            row[6] = str(int(row[5]) + int(row[4])).rjust(12,'0')
            row[7] = parsed_row[7]
            print(",".join(row))


if __name__=='__main__':
    main()
 
        
        