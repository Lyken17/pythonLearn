#include <stdio.h>

union{
    float   f;
    long    i;
}u, v, w;

int main(int argc, char *argv[])
{
    int e1, e2, ee;
    unsigned long   m1, m2, mm, nh, nl;

    for(;;){
        scanf("%f", &u.f);
        e1=(u.i>>23)&0xFF;
        m1=(u.i&0x7FFFFF)|0x800000;
        printf("%u -- %lX\n", e1, m1);
        scanf("%f", &v.f);
        e2=(v.i>>23)&0xFF;
        m2=(v.i&0x7FFFFF)|0x800000;
        printf("%u -- %lX\n", e2, m2);
        w.f=u.f*v.f;
        ee=(w.i>>23)&0xFF;
        mm=(w.i&0x7FFFFF)|0x800000;
        printf("%u -- %lX\t:%f\n", ee, mm, w.f);

        e1=(e1+e2-127); nh=nl=0;
        while(m2!=0){
            nl>>=1; if(nh&1)nl|=0x80000000;
            nh>>=1; if(m2&1)nh+=m1;
            m2>>=1;
        }
        nh+=(nl>>31);   //四舍五入
        while(nh&0xFF000000){
            nh>>=1; e1++;
        }
        //? while(m1&0x00800000==0){m1<<=1; e1--;}
        printf("%u -- %lX\t%lX\n", e1, nh, nl);
        w.i=((u.i^v.i)&0x80000000)|((long)e1<<23)|(nh&0x7FFFFF);
        printf("%f * %f = %f\n\n", u.f, v.f, w.f);

        if(getch()==27) break;
    }
    return 0;
}
