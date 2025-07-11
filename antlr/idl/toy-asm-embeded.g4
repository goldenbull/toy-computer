grammar toy_asm;

@header {
from .computer import *
}

program returns [Program val]
@init
{
$val = Program()
}
    : ( datatypeDef  {$val.datatypes.append($datatypeDef.val)}
        | structDef  {$val.structures.append($structDef.val)}
        | classDef {$val.classes.append($classDef.val)}
      )+
    ;

datatypeDef returns [DatatypeDef val]
@init
{
$val = DatatypeDef()
}
    : (Comment {$val.comment += $Comment.text})+ (enumEntry {$val.enumEntries.append($enumEntry.val)})*
     'typedef' datatype {$val.datatype=$datatype.text} Id {$val.name=$Id.text} ('[' ChrLen {$val.chrlen = int($ChrLen.text)} ']')? ';'
    ;

enumEntry returns [EnumEntry val]
@init
{
$val = EnumEntry()
}
    : Comment {$val.comment=$Comment.text} '#define' Id {$val.name=$Id.text} literal {$val.literal=$literal.text}
    ;

structDef returns [StructDef val]
@init
{
$val = StructDef()
}
    : Comment {$val.comment=$Comment.text} 'struct' Id {$val.name=$Id.text} '{' (field {$val.fields.append($field.val)})+ '}' ';'
    ;

field returns [FieldDef val]
@init
{
$val = FieldDef()
}
    : Comment {$val.comment=$Comment.text} datatype {$val.datatype=$datatype.text} Id {$val.name=$Id.text} ';'
    ;

classDef returns [ClassDef val]
@init
{
$val = ClassDef()
}
    : Comment* 'class' Id? classname=Id {$val.name=$classname.text}
     '{' (classBody {if $classBody.val: $val.functions.append($classBody.val)})+ '}' ';'
    ;

classBody returns [FunctionDef val]
    : function {$val=$function.val}
    | 'public:'
    | 'protected:'
    ;

function returns [FunctionDef val]
@init
{
$val = FunctionDef()
}
    : (Comment {$val.comment += $Comment.text})* (FuncPrefix {$val.prefix=$FuncPrefix.text})?
      datatype {$val.datatype=$datatype.text} Id {$val.name=$Id.text} '(' ')' funcTail
    | (Comment {$val.comment += $Comment.text})* (FuncPrefix {$val.prefix=$FuncPrefix.text})?
      datatype {$val.datatype=$datatype.text} Id {$val.name=$Id.text} '(' paramList {$val.parameters=$paramList.val} ')' funcTail
    ;

paramList returns [val]
@init
{
$val = []
}
    : p1=param {$val.append($p1.val)} ( ',' p2=param {$val.append($p2.val)} )*
    ;

param returns [Param val]
@init
{
$val = Param()
}
    : datatype {$val.datatype=$datatype.text} Id {$val.name=$Id.text} ('[]' {$val.is_array=True})? ( '=' literal )?
    ;

FuncPrefix
    : 'virtual'
    | 'static'
    ;

funcTail
    : '{' '}' ';'?
    | '=' '0' ';'
    | ';'
    ;

datatype
    : Id
    | 'const' datatype
    | datatype '*'
    | '~'
    ;

Id  : [a-zA-Z] ([a-zA-Z0-9]|'_')*
    ;


ChrLen
    : [0-9]+
    ;


literal
    :   StringLiteral
    |   booleanLiteral
    ;

booleanLiteral
    :   'true'
    |   'false'
    ;

StringLiteral
    :  '"' ~["]* '"'
    |  '\'' ~[']* '\''
    ;

WS  : [ \r\t\u000C\n]+ -> skip ;

Comment
    : '//' ~[\n]* '\n'
    ;
