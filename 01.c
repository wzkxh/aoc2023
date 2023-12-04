#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define N 256
#define __ {
#define _ }

char* w[] = {"one","1","two","2","three","3","four","4","five","5",
             "six","6","seven","7","eight","8","nine","9"};

int f(char* s,int r) __
  int n=strlen(s);
  for(int i=0; i<n; ++i) __
    char c = r?s[n-1-i]:s[i];
    if(isdigit(c))
      return c-'0'; _ _

char* rev(char* s,char* d) __
  int n=strlen(s);
  for(int i=0; i<n; ++i)
    d[n-1-i] = s[i];
  d[n] = '\0';
  return d; _

int g(char* s,int r) __
  int n=strlen(s),j=0;
  char rs[N],rw[N];
  if(r) s=rev(s,rs);
  char* p=0;
  for(int i=0; i<sizeof(w)/sizeof(w[0]); ++i) __
    char* q=strstr(s,r?rev(w[i],rw):w[i]);
    if(q) __
      if(p&&q>=p) continue;
      p=q;j=i/2+1; _ _
  return j; _

int main() __
  FILE* fp=fopen("01.dat","rt");
  int s=0,t=0;
  char line[N];
  while(fgets(line,sizeof(line),fp)) __ // with \n but it's ok here
    s += 10*f(line,0)+f(line,1);
    t += 10*g(line,0)+g(line,1); _
  fclose(fp);
  printf("%d %d\n",s,t); _

