tokens = [
    'INTEGER',
    'FLOAT',
    'BOOLEAN',
    'PLUS',
    'MINUS',
    'MULTIPLICATION',
    'POW',
    'DIVIDE',
    'LEFTOVER',
    'INT_DIVISION',
    'COMPARATOR',
    'L_PAREN',
    'R_PAREN',
    'L_SQUARE_PAREN',
    'R_SQUARE_PAREN',
    'UP_SCOPE',
    'DOWN_SCOPE',
    'IDENTIFIER',
    'COMMENT',
    'EOL',
    'INSTANCE',
    'METHOD_CALL_POINT',
    'COMA',
    'RESERVED_FUNC',
    'RESERVED_METHOD',
    'MAIN_FUNC',
    'PROCEDURE',
    'COLON',
    'pene',
   
]
FunctionDataSetters={
    'int':'int',
    'float':'float',
    'bool':'bool',
    'lista' : 'lista',

}

reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'for'   : 'FOR',
    'in'    : 'IN',
    'Step'  : 'STEP',
 }
reserved_function_names={
    'blink'      : 'BLINK',
    'delay'      : 'DELAY',
    'printLed'   : "PRINT_LED" ,
    'printLedX'  : 'PRINT_LED_X',
    'range'      : 'RANGE',
    'list'       : 'LIST',
    'type'       : 'TYPE',
    'len'        : 'LEN',
}
reserved_special_time={
    "'seg'":"'seg'",
    "'min'":"'min'",
    "'mil'":"'mil'",
    
}
reserved_special_object={
    "'F'":"'F'",
    "'C'":"'C'",
    "'M'": "'M'",
}

reserved_function_params={
    'BLINK'      : [['lista','int'],['int'],["RESERVED_SPECIAL_TIME"],['bool']],
    'DELAY'      : [['int'],["RESERVERD_SPECIAL_TIME"]],
    "PRINT_LED"  : [['int'],['int'],['bool']],
    'PRINT_LED_X': [["RESERVED_SPECIAL_OBJECT"],['int'],["lista"]],
    'RANGE'      : [["int"],["bool"]],
    'LIST'       : [['pene']],
    'TYPE'       : [['ANY']],
    'LEN'        : [["lista"]],
}

reserved_methods_names={
    'F'      :'F_METHOD',
    'T'      : 'T_METHOD',
    'Neg'    : 'NEG',
    'shapeF' : 'SHAPE_F',
    'shapeC' : 'SHAPE_C',
    'insert' : 'INSERT',
    'delete' : 'DELETE',
}

method_valid_type={
    'F_METHOD': ['lista','bool'],
    'T_METHOD': ['lista','bool'],
    'NEG'     : ['lista','bool'],
    'SHAPE_F' : ['lista'],
    'SHAPE_C' : ['lista'],
    'INSERT'  : ['lista'],
    'DELETE'  : ['lista'],
}