# anki-patch-fuzzIvlRange
This add-on monkey patches the V2 scheduler routine _fuzzIvlRange.

The original procedure is unnecessarily complex and returns not quite
monotonically increasing ranges as the input interval increases.

Ivl Range       Size
1: 	[1, 1]      0
2: 	[2, 3]      1
3: 	[3, 3]      0
4: 	[3, 4]      1
5: 	[4, 6]      2
6: 	[5, 7]      2
7: 	[6, 8]      2
8: 	[7, 9]      2
9: 	[8, 10]     2
...
13: [12, 14]    2
14: [12, 16]    4
15: [13, 17]    4
16: [14, 18]    4
...
19: [17, 21]    4
20: [17, 23]    6
21: [18, 24]    6
...
26: [23, 29]    6
27: [23, 31]    8
28: [24, 32]    8
...
99: [95, 103]   8
100:[95, 105]   10
101:[96, 106]   10
...



The patched implementation returns ranges that increase in size
monotonically as the interval increases, to a maximum range of +/- 4 days
around the given interval.
