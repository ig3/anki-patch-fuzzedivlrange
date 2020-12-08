# anki-patch-fuzzIvlRange
This add-on monkey patches the V2 scheduler routine _fuzzIvlRange.

The original procedure is unnecessarily complex and returns not quite
monotonically increasing ranges as the input interval increases, at low
intervals. There is an approximation to a logarithmic growth at low
intervals, but beyond 20 days it is linear at about  +/-5% of the interval.

The patched implementation returns ranges that increase in size
monotonically as the interval increases. Special cases below interval of 4
days, then (ivl +/- int(log(ivl,2))-1) days, so a logarithmic rolloff. This
reaches +/-7days at an interval of 365 days / 1 year. This is small, but
enough to ensure that cards don't stick together on the say days. From
learning, the cumulative difference should be significant.
