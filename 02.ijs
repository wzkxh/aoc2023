t=: cutLF CR-.~fread'02.dat'

i=: [:".5}.({.~i.&':') NB. get id
p=: _3(([:".>@{.)*'rgb'=[:{.@>1&{)\[:;:(}.~(1+i.&':')) NB. process line

echo +/(i*([:*./12 13 14>:[:>./p))&> t
echo +/([:*/[:>./p)&> t

exit 0

