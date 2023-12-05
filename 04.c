    #include <stdio.h> // printf
    #include <stdlib.h> // strtol
    #include <string.h> // strchr

    #define __ { // pythonize syntax
    #define _ }

    int read( char* s, int* a ) __ int n=0; char* q;
      for(char* p=s;;p=q) __
        int x=(int)strtol(p,&q,10);
        if(q==p) break;
        a[n++]=x; _
      return n; _

    int isin( int x, int* a, int n ) __
      for(int i=0;i<n;++i)
        if(x==a[i]) return 1;
      return 0; _

    int sum( int* a, int n ) __ int s=0;
      for(int i=0;i<n;++i) s+=a[i];
      return s; _

    int main() __ int n=0, p=0; // number of lines, point counter (part 1)
      int q[200], w[50], m[50]; // line counters (part 2), win numbers, my numbers
      for(int i=0;i<sizeof(q)/sizeof(*q);++i) q[i]=1;
      FILE* fp=fopen("04.dat","rt");
      for(char s[150];fgets(s,sizeof(s)-1,fp);++n) __
        int nw = read( strchr(s,':')+1, w );
        int nm = read( strchr(s,'|')+1, m );
        int found=0;
        for(int i=0;i<nm;++i) __
          if(isin(m[i],w,nw)) ++found; _
        if(found) __
          p += 1<<(found-1);
          for(int j=n+1;j<n+1+found;++j) __
            q[j] += q[n]; _ _ _
      fclose(fp);
      printf("%d %d\n",p,sum(q,n)); _
