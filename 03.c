#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define N 256 // max rows/cols (140 in my input)
#define __ {  // pythonize syntax
#define _ }

char t[N][N]; // yes, static and global :) must be enough for this task

int in_d(int k,int* kk,int n) __ // search in "dictionary"
  for(int i=0;i<n;++i)
    if(kk[i]==k) return i;
  return -1; _

int good(int i,int j) __ // return three values
  for(int ii=i-1;ii<=i+1;++ii)
    for(int jj=j-1;jj<=j+1;++jj) __ char c = t[ii][jj];
      if(!isdigit(c)&&c!='.') return (ii*1000+jj)*1000+c; _
  return 0; _

int s1=0,s2=0; // results of part 1, 2

int main() __ int n; // lines are 0,1..140,141=n; each 142=m chars
  FILE* fp=fopen("03.dat","rt");
  for(n=1;fgets(&t[n][1],N-1,fp);++n) t[n][0]=strchr(&t[n][1],'\n')[0]='.';
  fclose(fp);
  int m=strlen(t[1]); memset(t,'.',m); t[0][m]='\0'; strcpy(t[n],t[0]);

  int fk[1000]; // dictionary - fk,fv,fn:  found gears, or rather first number
  int fv[1000]; // (369 items in my case)  of it (i,j)->n
  int fn=0; // length of fk:fv
  for(int i=1;i<n;++i) __ int v; // value of number
    int n=0; // flag 'in number'
    int g=0; // flag 'good', i.e. adjacent, for part 1
    int k=0; // coords of adjacent star, for part 2
    for(int j=1;j<m;++j) __ // check last '.' - it'll be ok b/c next is '.' too
      if(isdigit(t[i][j])) __
        if(!n) n=1, v=0;
        v=v*10+t[i][j]-'0';
        int z = good(i,j); // has adjacent?
        if(z) __ g=1;
          if(z%1000=='*') k=z/1000; _ _ // coords of that star
      else __
        if(n) __ // just scanned a number
          if(g) __ // and it was 'good'
            s1+=v; g=0;
            if(k) __
              int x=in_d(k,fk,fn); // has already coords k in dictionary
              if(x>=0) s2+=fv[x]*v; // then accumulate product for part 2
              else { fk[fn]=k; fv[fn]=v; ++fn; } // else add to dictionary
              k=0; _ _
          n=0; _ _ _
  }
  printf("%d %d\n",s1,s2); _
