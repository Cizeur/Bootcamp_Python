import csv


class CsvReader():
    def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
        args = locals()
        args.pop("self")
        args = {"_"+k: v for k, v in args.items()}
        self.__dict__.update(args)

    def _trimmed(self, data):
        try:
            data = data.splitlines()
            data = data[self._skip_top: len(data) - self._skip_bottom]
            if not data:
                return False
            return data
        except Exception:
            return False

    def check_integrity(self, data):
        data = self._trimmed(data)

        def quick_check(fields, size):
            if not all(x not in ["", None] for x in fields):
                return False
            if len(fields) != size:
                return False
            return True
        if not self._trimmed:
            return False
        try:
            data = list(csv.reader(data, delimiter=self._sep))
            check = len(data[0])
            if not all(quick_check(x, check) for x in data):
                return False
            return True
        except Exception:
            return False

    def getdata(self, data):
        data = self._trimmed(data)
        if not self._trimmed:
            return False
        start = 1 if self._header else 0
        try:
            return list(csv.reader(data, delimiter=self._sep))[start:]
        except Exception:
            return None

    def getheader(self, data):
        data = self._trimmed(data)
        if not self._trimmed:
            return False
        if self._header:
            try:
                return list(csv.reader(data, delimiter=self._sep))[0]
            except Exception:
                return None
        else:
            return None


class Loadjson(CsvReader):
    __data = []

    def __init__(self, filename):
        super().__init__(header=True)
        self.filename = filename

    def __enter__(self):
        try:
            self.f = open(self.filename, "r")
        except Exception:
            return None
        self.__data = self.f.read()
        if not self.__data or not self.check_integrity(self.__data):
            return None
        return self

    def getdata(self):
        return super().getdata(self.__data)

    def getheader(self):
        return super().getheader(self.__data)

    def __exit__(self, exception_type, exception_value, traceback):
        self.__data = []
        try:
            self.f.close()
        except Exception:
            pass


if __name__ == "__main__":

    import sys

    args = sys.argv
    args.pop(0)
    if not len(args):
        exit(0)
    with Loadjson(args[0]) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
