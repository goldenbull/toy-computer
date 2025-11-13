; input two numbers, save them in memory [0] and [1]
mov bp, 0
println "input x"
input [bp]
println "input y"
input [bp+1]

; add
mov ax, [bp]
add ax, [bp+1]
print [bp]
print " + "
print [bp+1]
print " = "
println ax

; sub
mov ax, [bp]
sub ax, [bp+1]
print [bp]
print " - "
print [bp+1]
print " = "
println ax

; mul
mov ax, [bp]
mul [bp+1]
print [bp]
print " * "
print [bp+1]
print " = "
println ax

; div
mov ax, [bp]
div [bp+1]
print [bp]
print " / "
print [bp+1]
print " = "
print ax
print " ... "
println dx

println "==== finished ===="
