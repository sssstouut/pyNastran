'ASSIGN OUTPUT2='myMatrix.op2','
'    UNIT=15'
'$'
'SOL 100'
'DIAG 8,44'
'COMPILE USERDMAP'
'ALTER 2'
'DMIIN DMI,DMINDX/A,B,MYDOF,,,,,,,/ $'
'MPYAD A,B,/ATB/1///$'
'MPYAD B,A,/BTA/1///$'
'OUTPUT2 A,B,ATB,BTA,MYDOF//0/15$'
'CEND'
