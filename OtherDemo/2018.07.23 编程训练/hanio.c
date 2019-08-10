//
//  main.c
//  tryC
//
//  Created by Jianming Shi on 2018/7/21.
//  Copyright © 2018年 Jianming Shi. All rights reserved.
//
/*
时间复杂度：
 F(n) = F(n-1) + 1 + F(n-1)
      = 2*F(n-1) + 1
 => O(2^n)
 次数：2^n-1
 证明：
 https://blog.csdn.net/u010480899/article/details/61413343
 */

#include <stdio.h>
int cnt = 0;

void hanio(int n, char from, char by, char to)
{
    if (1 == n)
    {
        printf("%c-->%c\n", from, to);
        cnt += 1;
        return;
    }
    hanio(n-1, from, to, by);
    hanio(1, from, by, to);
    hanio(n-1, by, from, to);
}

int main(int argc, const char * argv[]) {
    int n = 3;
    hanio(n, 'A', 'B', 'C');
    printf("%d\n", cnt);
    return 0;
}
