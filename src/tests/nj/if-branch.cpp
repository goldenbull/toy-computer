if(a>b)
{
    // code block 1
}
else
{
    // code block 2
}

cmp a,b
jle _block2

// block1
jmp _end_if

_block2:

// block2

_end_if:
...