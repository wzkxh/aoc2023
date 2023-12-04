t=: ((}.~(1+i.&':'))&>) cutLF CR-.~fread'04.dat'

f=: [:+/#@[>i.
echo +/2^_1+ (#~>&0) ([:".rplc&('|';'f'))"1 t

exit 0

