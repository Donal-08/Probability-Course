#include<stdio.h>
#include<stdlib.h>

// Part 1 Mutually exclusive -> pr_ab = 0
void verify_part_1(float pr_a, float pr_a_plus_b,float e){
    float pr_b ;
    int pr_ab = 0;
    pr_b = pr_a_plus_b - pr_b - pr_ab;
    if(abs(pr_b - 0.1)<e)
    printf("Solution to part (i) verified.\n");
    else 
    printf("not verified\n");
}

// Part 2 Independent  -> pr_ab = pr_a*pr_b
void verify_part_2(float pr_a, float pr_a_plus_b,float e){
    float pr_b, pr_ab;
    pr_ab = pr_a * pr_b;
    pr_b = pr_a - pr_ab - pr_a_plus_b;

    if(abs(pr_b - 0.2)<e)
    printf("Solution to part (ii) verified.\n") ;    
}

int main()
{
    float pr_a = 0.5, pr_a_plus_b = 0.6;
    float e = 10e-6;
    verify_part_1(pr_a,pr_a_plus_b,e);
    verify_part_2(pr_a,pr_a_plus_b,e);
    
}
