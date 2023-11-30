\ Model Master2
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[0] + x[1] + x[2] + x[3] + x[4]
Subject To
 R0: 6 x[0] + 2 x[4] >= 25
 R1: 2 x[1] + 2 x[4] >= 30
 R2: 2 x[2] >= 14
 R3: x[3] >= 8
Bounds
End
