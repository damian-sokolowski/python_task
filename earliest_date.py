import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "in_date",
    type=file,
    help='Path to file containing date in the "A/B/C" format, '
         'where A,B,C are integers',
)
args = parser.parse_args()

line = args.in_date.readline().replace('\n', '',)
input_date = map(int, line.split('/'),)
input_date.sort()

dates = []
result_date = None
dates_map = [
    {'year': 0, 'month': 1, 'day': 2},
    {'year': 1, 'month': 0, 'day': 2},
    {'year': 2, 'month': 0, 'day': 1}
]

for date_map in dates_map:
    try:
        year = (
            input_date[date_map['year']] if input_date[date_map['year']] > 99
            else input_date[date_map['year']] + 2000
        )
        dates.append(datetime.date(
            year=year,
            month=input_date[date_map['month']],
            day=input_date[date_map['day']],
        ))
    except ValueError as e:
        pass

dates.sort()

for date in dates:
    if 2000 <= date.year <= 2999:
        result_date = date.strftime('%Y-%m-%d')
        break

print (
    "{} => {}".format(line, result_date) if result_date
    else "{} is illegal".format(line)
)
