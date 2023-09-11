# Multimixer-156
Code for Multimixer-156

To run the code complete the following,


Compile C files with: 
gcc -g *.c -c

Compile Assembly code / for Multimixer128 assembly code:
gcc -mfpu=neon -c Multimixer156.s -o Multimixer156.o

Link them together with: 
gcc -g -o output *.o

Run it by:
./output
