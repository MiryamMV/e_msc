import numpy  as np
import pandas as pd


def read_degrad(filename: str) -> pd.DataFrame:

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    events.extend(content[1::2])

    evtnums, x, y, z = (list() for _ in range(4))

    for i, evt in enumerate(events):
        words  = evt.split()
        values = np.array(words, dtype=float)
        nrows  = 7
        ncols  = int(len(values)/7)
        values = values.reshape(ncols,nrows)
        xl = np.divide(values[:,0], 1e3).tolist()
        yl = np.divide(values[:,1], 1e3).tolist()
        zl = np.divide(values[:,2], 1e3).tolist()
        x.extend(xl)
        y.extend(yl)
        z.extend(zl)
        evtnums.extend([i]*len(xl))

    return pd.DataFrame({'event_number': evtnums, 'x': x, 'y': y, 'z': z})
