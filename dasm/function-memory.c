#include <stdio.h>

typedef struct
{
    int x;
    int y;
    char id[9];
} Point;

Point f1(Point pt, int dx, int dy)
{
    Point ret = pt;
    ret.x += dx;
    ret.y += dy;
    return ret;
}

Point f2(Point pt, int dx, int dy)
{
    Point ret;
    ret.x = pt.x + dx;
    ret.y = pt.y + dy;
    return ret;
}

Point f3(Point* pt, int dx, int dy)
{
    Point ret;
    ret.x = pt->x + dx;
    ret.y = pt->y + dy;
    return ret;
}

int f4(Point* pt, int dx, int dy, Point* ret)
{
    ret->x = pt->x + dx;
    ret->y = pt->y + dy;
    return 1;
}

int main()
{
    printf("sizeof(Point) = %d\n", sizeof(Point));
    
    Point pt;
    pt.x = 100;
    pt.y = 200;

    Point ret1 = f1(pt, 1, 2);
    printf("%d %d\n", ret1.x, ret1.y);

    Point ret2 = f2(pt, 2, 4);
    printf("%d %d\n", ret2.x, ret2.y);

    Point ret3 = f3(&pt, 3, 6);
    printf("%d %d\n", ret3.x, ret3.y);

    Point ret4;
    int success = f4(&pt, 4, 8, &ret4);
    printf("%d %d\n", ret4.x, ret4.y);

    return 0;
}