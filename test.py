from bootstrap import *
table1 = ConformalBlockTable(3, 15, 15, 1, 3, odd_spins = True)
table2 = ConvolvedBlockTable(table1, symmetric = True)
table3 = ConvolvedBlockTable(table1)
N = 3.0
table_list = [table2, table3]
vec1 = [[0, 1], [1, 1], [1, 0]]
vec2 = [[1, 1], [1.0 - (2.0 / N), 1], [-(1.0 + (2.0 / N)), 0]]
vec3 = [[1, 1], [-1, 1], [1, 0]]
info = [[vec1, 0, 0], [vec2, 0, 1], [vec3, 1, 2]]
sdp = SDP(0.52, table_list, vector_types = info)
result = sdp.bisect(0.7, 1.8, 0.01, [0, 0])
print result
