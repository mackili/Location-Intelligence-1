\* Problem_1 *\
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
 + 100000 y_Atlanta + 100000 y_Boston + 100000 y_Charlotte + 100000 y_Chicago
 + 100000 y_Cincinnati + 100000 y_Detroit + 100000 y_NewYork
 + 100000 y_Pittsburgh + 100000 y_StLouis
Subject To
_C1: x_Atlanta_Chicago + x_Boston_Chicago + x_Charlotte_Chicago
 + x_Chicago_Chicago + x_Cincinnati_Chicago + x_Detroit_Chicago
 + x_NewYork_Chicago + x_Pittsburgh_Chicago + x_StLouis_Chicago = 1
_C10: x_Chicago_Chicago - y_Chicago <= 0
_C11: x_Atlanta_Chicago - y_Atlanta <= 0
_C12: x_NewYork_Chicago - y_NewYork <= 0
_C13: x_StLouis_Chicago - y_StLouis <= 0
_C14: x_Detroit_Chicago - y_Detroit <= 0
_C15: x_Cincinnati_Chicago - y_Cincinnati <= 0
_C16: x_Pittsburgh_Chicago - y_Pittsburgh <= 0
_C17: x_Charlotte_Chicago - y_Charlotte <= 0
_C18: x_Boston_Chicago - y_Boston <= 0
_C19: x_Chicago_Atlanta - y_Chicago <= 0
_C2: x_Atlanta_Atlanta + x_Boston_Atlanta + x_Charlotte_Atlanta
 + x_Chicago_Atlanta + x_Cincinnati_Atlanta + x_Detroit_Atlanta
 + x_NewYork_Atlanta + x_Pittsburgh_Atlanta + x_StLouis_Atlanta = 1
_C20: x_Atlanta_Atlanta - y_Atlanta <= 0
_C21: x_NewYork_Atlanta - y_NewYork <= 0
_C22: x_StLouis_Atlanta - y_StLouis <= 0
_C23: x_Detroit_Atlanta - y_Detroit <= 0
_C24: x_Cincinnati_Atlanta - y_Cincinnati <= 0
_C25: x_Pittsburgh_Atlanta - y_Pittsburgh <= 0
_C26: x_Charlotte_Atlanta - y_Charlotte <= 0
_C27: x_Boston_Atlanta - y_Boston <= 0
_C28: x_Chicago_NewYork - y_Chicago <= 0
_C29: x_Atlanta_NewYork - y_Atlanta <= 0
_C3: x_Atlanta_NewYork + x_Boston_NewYork + x_Charlotte_NewYork
 + x_Chicago_NewYork + x_Cincinnati_NewYork + x_Detroit_NewYork
 + x_NewYork_NewYork + x_Pittsburgh_NewYork + x_StLouis_NewYork = 1
_C30: x_NewYork_NewYork - y_NewYork <= 0
_C31: x_StLouis_NewYork - y_StLouis <= 0
_C32: x_Detroit_NewYork - y_Detroit <= 0
_C33: x_Cincinnati_NewYork - y_Cincinnati <= 0
_C34: x_Pittsburgh_NewYork - y_Pittsburgh <= 0
_C35: x_Charlotte_NewYork - y_Charlotte <= 0
_C36: x_Boston_NewYork - y_Boston <= 0
_C37: x_Chicago_StLouis - y_Chicago <= 0
_C38: x_Atlanta_StLouis - y_Atlanta <= 0
_C39: x_NewYork_StLouis - y_NewYork <= 0
_C4: x_Atlanta_StLouis + x_Boston_StLouis + x_Charlotte_StLouis
 + x_Chicago_StLouis + x_Cincinnati_StLouis + x_Detroit_StLouis
 + x_NewYork_StLouis + x_Pittsburgh_StLouis + x_StLouis_StLouis = 1
_C40: x_StLouis_StLouis - y_StLouis <= 0
_C41: x_Detroit_StLouis - y_Detroit <= 0
_C42: x_Cincinnati_StLouis - y_Cincinnati <= 0
_C43: x_Pittsburgh_StLouis - y_Pittsburgh <= 0
_C44: x_Charlotte_StLouis - y_Charlotte <= 0
_C45: x_Boston_StLouis - y_Boston <= 0
_C46: x_Chicago_Detroit - y_Chicago <= 0
_C47: x_Atlanta_Detroit - y_Atlanta <= 0
_C48: x_NewYork_Detroit - y_NewYork <= 0
_C49: x_StLouis_Detroit - y_StLouis <= 0
_C5: x_Atlanta_Detroit + x_Boston_Detroit + x_Charlotte_Detroit
 + x_Chicago_Detroit + x_Cincinnati_Detroit + x_Detroit_Detroit
 + x_NewYork_Detroit + x_Pittsburgh_Detroit + x_StLouis_Detroit = 1
_C50: x_Detroit_Detroit - y_Detroit <= 0
_C51: x_Cincinnati_Detroit - y_Cincinnati <= 0
_C52: x_Pittsburgh_Detroit - y_Pittsburgh <= 0
_C53: x_Charlotte_Detroit - y_Charlotte <= 0
_C54: x_Boston_Detroit - y_Boston <= 0
_C55: x_Chicago_Cincinnati - y_Chicago <= 0
_C56: x_Atlanta_Cincinnati - y_Atlanta <= 0
_C57: x_NewYork_Cincinnati - y_NewYork <= 0
_C58: x_StLouis_Cincinnati - y_StLouis <= 0
_C59: x_Detroit_Cincinnati - y_Detroit <= 0
_C6: x_Atlanta_Cincinnati + x_Boston_Cincinnati + x_Charlotte_Cincinnati
 + x_Chicago_Cincinnati + x_Cincinnati_Cincinnati + x_Detroit_Cincinnati
 + x_NewYork_Cincinnati + x_Pittsburgh_Cincinnati + x_StLouis_Cincinnati = 1
_C60: x_Cincinnati_Cincinnati - y_Cincinnati <= 0
_C61: x_Pittsburgh_Cincinnati - y_Pittsburgh <= 0
_C62: x_Charlotte_Cincinnati - y_Charlotte <= 0
_C63: x_Boston_Cincinnati - y_Boston <= 0
_C64: x_Chicago_Pittsburgh - y_Chicago <= 0
_C65: x_Atlanta_Pittsburgh - y_Atlanta <= 0
_C66: x_NewYork_Pittsburgh - y_NewYork <= 0
_C67: x_StLouis_Pittsburgh - y_StLouis <= 0
_C68: x_Detroit_Pittsburgh - y_Detroit <= 0
_C69: x_Cincinnati_Pittsburgh - y_Cincinnati <= 0
_C7: x_Atlanta_Pittsburgh + x_Boston_Pittsburgh + x_Charlotte_Pittsburgh
 + x_Chicago_Pittsburgh + x_Cincinnati_Pittsburgh + x_Detroit_Pittsburgh
 + x_NewYork_Pittsburgh + x_Pittsburgh_Pittsburgh + x_StLouis_Pittsburgh = 1
_C70: x_Pittsburgh_Pittsburgh - y_Pittsburgh <= 0
_C71: x_Charlotte_Pittsburgh - y_Charlotte <= 0
_C72: x_Boston_Pittsburgh - y_Boston <= 0
_C73: x_Chicago_Charlotte - y_Chicago <= 0
_C74: x_Atlanta_Charlotte - y_Atlanta <= 0
_C75: x_NewYork_Charlotte - y_NewYork <= 0
_C76: x_StLouis_Charlotte - y_StLouis <= 0
_C77: x_Detroit_Charlotte - y_Detroit <= 0
_C78: x_Cincinnati_Charlotte - y_Cincinnati <= 0
_C79: x_Pittsburgh_Charlotte - y_Pittsburgh <= 0
_C8: x_Atlanta_Charlotte + x_Boston_Charlotte + x_Charlotte_Charlotte
 + x_Chicago_Charlotte + x_Cincinnati_Charlotte + x_Detroit_Charlotte
 + x_NewYork_Charlotte + x_Pittsburgh_Charlotte + x_StLouis_Charlotte = 1
_C80: x_Charlotte_Charlotte - y_Charlotte <= 0
_C81: x_Boston_Charlotte - y_Boston <= 0
_C82: x_Chicago_Boston - y_Chicago <= 0
_C83: x_Atlanta_Boston - y_Atlanta <= 0
_C84: x_NewYork_Boston - y_NewYork <= 0
_C85: x_StLouis_Boston - y_StLouis <= 0
_C86: x_Detroit_Boston - y_Detroit <= 0
_C87: x_Cincinnati_Boston - y_Cincinnati <= 0
_C88: x_Pittsburgh_Boston - y_Pittsburgh <= 0
_C89: x_Charlotte_Boston - y_Charlotte <= 0
_C9: x_Atlanta_Boston + x_Boston_Boston + x_Charlotte_Boston
 + x_Chicago_Boston + x_Cincinnati_Boston + x_Detroit_Boston
 + x_NewYork_Boston + x_Pittsburgh_Boston + x_StLouis_Boston = 1
_C90: x_Boston_Boston - y_Boston <= 0
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
