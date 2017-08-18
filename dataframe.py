import csv


class DataList(object):

    def __init__(self, data):
        # Just a list of data for now
        self.data = data

    def merge(self, df, how='outer'):
        strategies = {
            'inner': self._inner_merge,
            'outer': self._outer_merge,
        }

        try:
            method = strategies[how]
        except KeyError:
            raise ValueError('{} is not a valid strategy.'.format(how))

        return method(df)

    def _inner_merge(self, df):
        return list(set(self.data).union(set(df)))

    def _outer_merge(self, df):
        return self.data + df

    def to_csv(self, fp, index=True):
        with open(fp, 'w') as f:
            writer = csv.writer(f)
            for i, row in enumerate(self.data):
                if index:
                    writer.writerow([i, row])
                else:
                    writer.writerow([row])
