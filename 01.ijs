t =: cutLF CR-.~fread'01.dat'

a =: ;:' one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9'

0 : 0
e =: [:+/(>:<.-:i.18)*a&((>@[E.'_',])"0 _)
f =: '123456789'&([:{.]#~9>i.)
g =: {.&(>&0#[)&e
h =: {:&(>&0#[)&e
echo +/".&(f,f&|.)&> t
echo +/((10*g)+h)&> t
)

echo +/{{".({.,{:)y#~9>'123456789'i.y}}&> t
echo +/{{((10*{.)+{:)(>&0#[)+/(>:<.-:i.18)*a{{(>x)E.'_',y}}"0 _ y}}&> t

NB. maybe use I. a E. y

exit 0
