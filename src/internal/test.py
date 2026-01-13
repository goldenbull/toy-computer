from internal.grammar.compiler import Compiler

if __name__ == '__main__':
    source_code="""
line1:
line11: jmp 
    
    line2
    
line2: add ax, 0
    
    call 
    
    
    no_func
err1: jmp 
    
    
    err_place

    line111: nop
    """
    result = Compiler.compile(source_code)
