\* _The_plant_center_problem_ *\
Minimize
OBJ: 1099 x_Atlanta_Boston + 245 x_Atlanta_Charlotte + 720 x_Atlanta_Chicago
 + 461 x_Atlanta_Cincinnati + 722 x_Atlanta_Detroit + 884 x_Atlanta_NewYork
 + 685 x_Atlanta_Pittsburgh + 555 x_Atlanta_StLouis + 1099 x_Boston_Atlanta
 + 867 x_Boston_Charlotte + 996 x_Boston_Chicago + 907 x_Boston_Cincinnati
 + 721 x_Boston_Detroit + 219 x_Boston_NewYork + 589 x_Boston_Pittsburgh
 + 1217 x_Boston_StLouis + 245 x_Charlotte_Atlanta + 867 x_Charlotte_Boston
 + 769 x_Charlotte_Chicago + 479 x_Charlotte_Cincinnati
 + 629 x_Charlotte_Detroit + 645 x_Charlotte_NewYork
 + 448 x_Charlotte_Pittsburgh + 715 x_Charlotte_StLouis
 + 720 x_Chicago_Atlanta + 996 x_Chicago_Boston + 769 x_Chicago_Charlotte
 + 296 x_Chicago_Cincinnati + 283 x_Chicago_Detroit + 790 x_Chicago_NewYork
 + 461 x_Chicago_Pittsburgh + 297 x_Chicago_StLouis + 461 x_Cincinnati_Atlanta
 + 907 x_Cincinnati_Boston + 479 x_Cincinnati_Charlotte
 + 296 x_Cincinnati_Chicago + 263 x_Cincinnati_Detroit
 + 667 x_Cincinnati_NewYork + 288 x_Cincinnati_Pittsburgh
 + 359 x_Cincinnati_StLouis + 722 x_Detroit_Atlanta + 721 x_Detroit_Boston
 + 629 x_Detroit_Charlotte + 283 x_Detroit_Chicago + 263 x_Detroit_Cincinnati
 + 614 x_Detroit_NewYork + 286 x_Detroit_Pittsburgh + 531 x_Detroit_StLouis
 + 884 x_NewYork_Atlanta + 219 x_NewYork_Boston + 645 x_NewYork_Charlotte
 + 790 x_NewYork_Chicago + 667 x_NewYork_Cincinnati + 614 x_NewYork_Detroit
 + 371 x_NewYork_Pittsburgh + 976 x_NewYork_StLouis + 685 x_Pittsburgh_Atlanta
 + 589 x_Pittsburgh_Boston + 448 x_Pittsburgh_Charlotte
 + 461 x_Pittsburgh_Chicago + 288 x_Pittsburgh_Cincinnati
 + 286 x_Pittsburgh_Detroit + 371 x_Pittsburgh_NewYork
 + 602 x_Pittsburgh_StLouis + 555 x_StLouis_Atlanta + 1217 x_StLouis_Boston
 + 715 x_StLouis_Charlotte + 297 x_StLouis_Chicago + 359 x_StLouis_Cincinnati
 + 531 x_StLouis_Detroit + 976 x_StLouis_NewYork + 602 x_StLouis_Pittsburgh
 + 15000 y_Atlanta + 50000 y_Boston + 45000 y_Charlotte + 10000 y_Chicago
 + 35000 y_Cincinnati + 30000 y_Detroit + 20000 y_NewYork + 40000 y_Pittsburgh
 + 25000 y_StLouis
Subject To
_C1: x_Atlanta_Chicago + x_Boston_Chicago + x_Charlotte_Chicago
 + x_Chicago_Chicago + x_Cincinnati_Chicago + x_Detroit_Chicago
 + x_NewYork_Chicago + x_Pittsburgh_Chicago + x_StLouis_Chicago = 1
_C10: 572000 x_Chicago_Atlanta + 610000 x_Chicago_Boston
 + 723000 x_Chicago_Charlotte + 2870000 x_Chicago_Chicago
 + 333000 x_Chicago_Cincinnati + 901000 x_Chicago_Detroit
 + 8450000 x_Chicago_NewYork + 306000 x_Chicago_Pittsburgh
 + 350000 x_Chicago_StLouis - 8610000 y_Chicago <= 0
_C11: 572000 x_Atlanta_Atlanta + 610000 x_Atlanta_Boston
 + 723000 x_Atlanta_Charlotte + 2870000 x_Atlanta_Chicago
 + 333000 x_Atlanta_Cincinnati + 901000 x_Atlanta_Detroit
 + 8450000 x_Atlanta_NewYork + 306000 x_Atlanta_Pittsburgh
 + 350000 x_Atlanta_StLouis - 1716000 y_Atlanta <= 0
_C12: 572000 x_NewYork_Atlanta + 610000 x_NewYork_Boston
 + 723000 x_NewYork_Charlotte + 2870000 x_NewYork_Chicago
 + 333000 x_NewYork_Cincinnati + 901000 x_NewYork_Detroit
 + 8450000 x_NewYork_NewYork + 306000 x_NewYork_Pittsburgh
 + 350000 x_NewYork_StLouis - 25350000 y_NewYork <= 0
_C13: 572000 x_StLouis_Atlanta + 610000 x_StLouis_Boston
 + 723000 x_StLouis_Charlotte + 2870000 x_StLouis_Chicago
 + 333000 x_StLouis_Cincinnati + 901000 x_StLouis_Detroit
 + 8450000 x_StLouis_NewYork + 306000 x_StLouis_Pittsburgh
 + 350000 x_StLouis_StLouis - 1050000 y_StLouis <= 0
_C14: 572000 x_Detroit_Atlanta + 610000 x_Detroit_Boston
 + 723000 x_Detroit_Charlotte + 2870000 x_Detroit_Chicago
 + 333000 x_Detroit_Cincinnati + 901000 x_Detroit_Detroit
 + 8450000 x_Detroit_NewYork + 306000 x_Detroit_Pittsburgh
 + 350000 x_Detroit_StLouis - 2703000 y_Detroit <= 0
_C15: 572000 x_Cincinnati_Atlanta + 610000 x_Cincinnati_Boston
 + 723000 x_Cincinnati_Charlotte + 2870000 x_Cincinnati_Chicago
 + 333000 x_Cincinnati_Cincinnati + 901000 x_Cincinnati_Detroit
 + 8450000 x_Cincinnati_NewYork + 306000 x_Cincinnati_Pittsburgh
 + 350000 x_Cincinnati_StLouis - 999000 y_Cincinnati <= 0
_C16: 572000 x_Pittsburgh_Atlanta + 610000 x_Pittsburgh_Boston
 + 723000 x_Pittsburgh_Charlotte + 2870000 x_Pittsburgh_Chicago
 + 333000 x_Pittsburgh_Cincinnati + 901000 x_Pittsburgh_Detroit
 + 8450000 x_Pittsburgh_NewYork + 306000 x_Pittsburgh_Pittsburgh
 + 350000 x_Pittsburgh_StLouis - 918000 y_Pittsburgh <= 0
_C17: 572000 x_Charlotte_Atlanta + 610000 x_Charlotte_Boston
 + 723000 x_Charlotte_Charlotte + 2870000 x_Charlotte_Chicago
 + 333000 x_Charlotte_Cincinnati + 901000 x_Charlotte_Detroit
 + 8450000 x_Charlotte_NewYork + 306000 x_Charlotte_Pittsburgh
 + 350000 x_Charlotte_StLouis - 2169000 y_Charlotte <= 0
_C18: 572000 x_Boston_Atlanta + 610000 x_Boston_Boston
 + 723000 x_Boston_Charlotte + 2870000 x_Boston_Chicago
 + 333000 x_Boston_Cincinnati + 901000 x_Boston_Detroit
 + 8450000 x_Boston_NewYork + 306000 x_Boston_Pittsburgh
 + 350000 x_Boston_StLouis - 1830000 y_Boston <= 0
_C19: 720 x_Atlanta_Chicago + 996 x_Boston_Chicago + 769 x_Charlotte_Chicago
 + 296 x_Cincinnati_Chicago + 283 x_Detroit_Chicago + 790 x_NewYork_Chicago
 + 461 x_Pittsburgh_Chicago + 297 x_StLouis_Chicago - z <= 0
_C2: x_Atlanta_Atlanta + x_Boston_Atlanta + x_Charlotte_Atlanta
 + x_Chicago_Atlanta + x_Cincinnati_Atlanta + x_Detroit_Atlanta
 + x_NewYork_Atlanta + x_Pittsburgh_Atlanta + x_StLouis_Atlanta = 1
_C20: 1099 x_Boston_Atlanta + 245 x_Charlotte_Atlanta + 720 x_Chicago_Atlanta
 + 461 x_Cincinnati_Atlanta + 722 x_Detroit_Atlanta + 884 x_NewYork_Atlanta
 + 685 x_Pittsburgh_Atlanta + 555 x_StLouis_Atlanta - z <= 0
_C21: 884 x_Atlanta_NewYork + 219 x_Boston_NewYork + 645 x_Charlotte_NewYork
 + 790 x_Chicago_NewYork + 667 x_Cincinnati_NewYork + 614 x_Detroit_NewYork
 + 371 x_Pittsburgh_NewYork + 976 x_StLouis_NewYork - z <= 0
_C22: 555 x_Atlanta_StLouis + 1217 x_Boston_StLouis + 715 x_Charlotte_StLouis
 + 297 x_Chicago_StLouis + 359 x_Cincinnati_StLouis + 531 x_Detroit_StLouis
 + 976 x_NewYork_StLouis + 602 x_Pittsburgh_StLouis - z <= 0
_C23: 722 x_Atlanta_Detroit + 721 x_Boston_Detroit + 629 x_Charlotte_Detroit
 + 283 x_Chicago_Detroit + 263 x_Cincinnati_Detroit + 614 x_NewYork_Detroit
 + 286 x_Pittsburgh_Detroit + 531 x_StLouis_Detroit - z <= 0
_C24: 461 x_Atlanta_Cincinnati + 907 x_Boston_Cincinnati
 + 479 x_Charlotte_Cincinnati + 296 x_Chicago_Cincinnati
 + 263 x_Detroit_Cincinnati + 667 x_NewYork_Cincinnati
 + 288 x_Pittsburgh_Cincinnati + 359 x_StLouis_Cincinnati - z <= 0
_C25: 685 x_Atlanta_Pittsburgh + 589 x_Boston_Pittsburgh
 + 448 x_Charlotte_Pittsburgh + 461 x_Chicago_Pittsburgh
 + 288 x_Cincinnati_Pittsburgh + 286 x_Detroit_Pittsburgh
 + 371 x_NewYork_Pittsburgh + 602 x_StLouis_Pittsburgh - z <= 0
_C26: 245 x_Atlanta_Charlotte + 867 x_Boston_Charlotte
 + 769 x_Chicago_Charlotte + 479 x_Cincinnati_Charlotte
 + 629 x_Detroit_Charlotte + 645 x_NewYork_Charlotte
 + 448 x_Pittsburgh_Charlotte + 715 x_StLouis_Charlotte - z <= 0
_C27: 1099 x_Atlanta_Boston + 867 x_Charlotte_Boston + 996 x_Chicago_Boston
 + 907 x_Cincinnati_Boston + 721 x_Detroit_Boston + 219 x_NewYork_Boston
 + 589 x_Pittsburgh_Boston + 1217 x_StLouis_Boston - z <= 0
_C3: x_Atlanta_NewYork + x_Boston_NewYork + x_Charlotte_NewYork
 + x_Chicago_NewYork + x_Cincinnati_NewYork + x_Detroit_NewYork
 + x_NewYork_NewYork + x_Pittsburgh_NewYork + x_StLouis_NewYork = 1
_C4: x_Atlanta_StLouis + x_Boston_StLouis + x_Charlotte_StLouis
 + x_Chicago_StLouis + x_Cincinnati_StLouis + x_Detroit_StLouis
 + x_NewYork_StLouis + x_Pittsburgh_StLouis + x_StLouis_StLouis = 1
_C5: x_Atlanta_Detroit + x_Boston_Detroit + x_Charlotte_Detroit
 + x_Chicago_Detroit + x_Cincinnati_Detroit + x_Detroit_Detroit
 + x_NewYork_Detroit + x_Pittsburgh_Detroit + x_StLouis_Detroit = 1
_C6: x_Atlanta_Cincinnati + x_Boston_Cincinnati + x_Charlotte_Cincinnati
 + x_Chicago_Cincinnati + x_Cincinnati_Cincinnati + x_Detroit_Cincinnati
 + x_NewYork_Cincinnati + x_Pittsburgh_Cincinnati + x_StLouis_Cincinnati = 1
_C7: x_Atlanta_Pittsburgh + x_Boston_Pittsburgh + x_Charlotte_Pittsburgh
 + x_Chicago_Pittsburgh + x_Cincinnati_Pittsburgh + x_Detroit_Pittsburgh
 + x_NewYork_Pittsburgh + x_Pittsburgh_Pittsburgh + x_StLouis_Pittsburgh = 1
_C8: x_Atlanta_Charlotte + x_Boston_Charlotte + x_Charlotte_Charlotte
 + x_Chicago_Charlotte + x_Cincinnati_Charlotte + x_Detroit_Charlotte
 + x_NewYork_Charlotte + x_Pittsburgh_Charlotte + x_StLouis_Charlotte = 1
_C9: x_Atlanta_Boston + x_Boston_Boston + x_Charlotte_Boston
 + x_Chicago_Boston + x_Cincinnati_Boston + x_Detroit_Boston
 + x_NewYork_Boston + x_Pittsburgh_Boston + x_StLouis_Boston = 1
Bounds
 z free
Binaries
x_Atlanta_Atlanta
x_Atlanta_Boston
x_Atlanta_Charlotte
x_Atlanta_Chicago
x_Atlanta_Cincinnati
x_Atlanta_Detroit
x_Atlanta_NewYork
x_Atlanta_Pittsburgh
x_Atlanta_StLouis
x_Boston_Atlanta
x_Boston_Boston
x_Boston_Charlotte
x_Boston_Chicago
x_Boston_Cincinnati
x_Boston_Detroit
x_Boston_NewYork
x_Boston_Pittsburgh
x_Boston_StLouis
x_Charlotte_Atlanta
x_Charlotte_Boston
x_Charlotte_Charlotte
x_Charlotte_Chicago
x_Charlotte_Cincinnati
x_Charlotte_Detroit
x_Charlotte_NewYork
x_Charlotte_Pittsburgh
x_Charlotte_StLouis
x_Chicago_Atlanta
x_Chicago_Boston
x_Chicago_Charlotte
x_Chicago_Chicago
x_Chicago_Cincinnati
x_Chicago_Detroit
x_Chicago_NewYork
x_Chicago_Pittsburgh
x_Chicago_StLouis
x_Cincinnati_Atlanta
x_Cincinnati_Boston
x_Cincinnati_Charlotte
x_Cincinnati_Chicago
x_Cincinnati_Cincinnati
x_Cincinnati_Detroit
x_Cincinnati_NewYork
x_Cincinnati_Pittsburgh
x_Cincinnati_StLouis
x_Detroit_Atlanta
x_Detroit_Boston
x_Detroit_Charlotte
x_Detroit_Chicago
x_Detroit_Cincinnati
x_Detroit_Detroit
x_Detroit_NewYork
x_Detroit_Pittsburgh
x_Detroit_StLouis
x_NewYork_Atlanta
x_NewYork_Boston
x_NewYork_Charlotte
x_NewYork_Chicago
x_NewYork_Cincinnati
x_NewYork_Detroit
x_NewYork_NewYork
x_NewYork_Pittsburgh
x_NewYork_StLouis
x_Pittsburgh_Atlanta
x_Pittsburgh_Boston
x_Pittsburgh_Charlotte
x_Pittsburgh_Chicago
x_Pittsburgh_Cincinnati
x_Pittsburgh_Detroit
x_Pittsburgh_NewYork
x_Pittsburgh_Pittsburgh
x_Pittsburgh_StLouis
x_StLouis_Atlanta
x_StLouis_Boston
x_StLouis_Charlotte
x_StLouis_Chicago
x_StLouis_Cincinnati
x_StLouis_Detroit
x_StLouis_NewYork
x_StLouis_Pittsburgh
x_StLouis_StLouis
y_Atlanta
y_Boston
y_Charlotte
y_Chicago
y_Cincinnati
y_Detroit
y_NewYork
y_Pittsburgh
y_StLouis
End
