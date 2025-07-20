    call f1
    call f2
    halt

f1:
    println "in f1"
    dump 512, 12
    ret

f2:
    dump 512, 11
    println "in f2, calling f1"
    call f1
    dump 512, 11

    ret