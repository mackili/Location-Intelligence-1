\* Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.008 BeefPercent + 0.013 ChickenPercent
 + 0.01 PorkPercent
Subject To
FatRequirement: 0.1 BeefPercent + 0.08 ChickenPercent + 0.09 PorkPercent >= 6
FibreRequirement: 0.005 BeefPercent + 0.001 ChickenPercent + 0.004 PorkPercent
 <= 2
MineralRequirement: 0.01 BeefPercent + 0.005 ChickenPercent
 + 0.007 PorkPercent >= 0.5
PercentagesSum: BeefPercent + ChickenPercent + PorkPercent = 100
ProteinRequirement: 0.2 BeefPercent + 0.1 ChickenPercent + 0.15 PorkPercent
 >= 8
SaltRequirement: 0.005 BeefPercent + 0.002 ChickenPercent + 0.003 PorkPercent
 <= 0.4
VitaminRequirement: 0.02 BeefPercent + 0.01 ChickenPercent + 0.015 PorkPercent
 >= 1
Bounds
 0 <= ChickenPercent
Generals
ChickenPercent
End
