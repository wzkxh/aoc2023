#include <stdio.h> // printf
#include <stdlib.h> // strtol strtod
#include <string.h> // strchr strcat
#include <math.h> // sqrt ceil floor

#define __ { // pythonize syntax
#define _ }

int read( char* s, int* a ) __ int n=0; char* q;
  for(char* p=s;;p=q) __
    int x=(int)strtol(p,&q,10);
    if(q==p) break;
    a[n++]=x; _
  return n; _

double cat_to_double( int* t, int nt ) __ char o[10]; char s[30]="";
  for(int i=0;i<nt;++i) sprintf(o,"%d",t[i]), strcat(s,o);
  return strtod(s,0); _

int main() __
  int t[10], d[10];
  FILE* fp=fopen("06.dat","rt");
  char s[150];
  fgets(s,sizeof(s)-1,fp);
  int nt = read( strchr(s,':')+1, t );
  fgets(s,sizeof(s)-1,fp);
  int nd = read( strchr(s,':')+1, d );
  fclose(fp);
  int r=1;
  for(int i=0;i<nt;++i) __ int s=0;
    for(int v=0;v<=t[i];++v) s += (t[i]-v)*v > d[i];
    r *= s; _
  double p=cat_to_double(t,nt), q=cat_to_double(d,nd);
  double a=p/2.0, b=sqrt(a*a-q);
  printf("%d %.0f\n",r,floor(a+b)-ceil(a-b)+1.0); _

