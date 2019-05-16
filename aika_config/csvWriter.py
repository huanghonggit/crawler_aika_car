"""
py3 csvwriter
"""
import csv
import traceback


class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect="excel", encoding="gb18030", **kwds):
        self.writer = csv.writer(f, dialect=dialect, **kwds)
        self.encoding = encoding

    def writerow(self, row):
        row = [str(item) for item in row]
        row = [s for s in row]
        # print('写出一行数据')
        self.writer.writerow(row)


class CSVDumper(object):
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath
        self.f = None
        self.writer = None

    def process_item(self, item):
        try:
            if self.f is None:
                with open(self.csv_filepath, "a+", newline='', encoding='gb18030') as self.f:
                    self.writer = UnicodeWriter(self.f)
                    self.writer.writerow(item.keys())
                    self.writer.writerow([v for _, v in item.items()])
            else:
                with open(self.csv_filepath, "a+", newline='', encoding='gb18030') as self.f:
                    self.writer = UnicodeWriter(self.f)
                    self.writer.writerow([v for _, v in item.items()])
        except:
            print(traceback.format_exc())
