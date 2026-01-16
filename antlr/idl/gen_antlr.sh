# java -jar ../antlr-4.13.2-complete.jar -Dlanguage=Python3 -o ../../src/internal/grammar -encoding UTF-8 -visitor toy_asm.g4
# java -jar ../antlr-4.13.2-complete.jar -Dlanguage=CSharp -o ../../src/cs/grammar -encoding UTF-8 -visitor toy_asm.g4
java -jar ../antlr-4.13.2-complete.jar -Dlanguage=TypeScript -o ../../src/web_frontend/src/libs/grammar -encoding UTF-8 -visitor -no-listener toy_asm.g4
