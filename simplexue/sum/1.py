#!/usr/bin/env python3.4

def printnum(a,b,c,d,e,f,g,h,i,j):
    tmp = min(a,d,f,g,j)
    if tmp==a:
        print(a,b,c,d,c,e,f,e,h,g,h,i,j,i,b)
    elif tmp==d:
        print(d,c,e,f,e,h,g,h,i,j,i,b,a,b,c)
    elif tmp==f:
        print(f,e,h,g,h,i,j,i,b,a,b,c,d,c,e)
    elif tmp==g:
        print(g,h,i,j,i,b,a,b,c,d,c,e,f,e,h)
    elif tmp==j:
        print(j,i,b,a,b,c,d,c,e,f,e,h,g,h,i)
for a in range(1,11):
    for b in range(1,11):
        if b==a:
            continue
        for c in range(1,11):
            if c in [a,b]:
                continue
            for d in range(1,11):
                if d in [a,b,c]:
                    continue
                for e in range(1,11):
                    if e in [a,b,c,d]:
                        continue
                    for f in range(1,11):
                        if f in [a,b,c,d,e]:
                            continue
                        for g in range(1,11):
                            if g in [a,b,c,d,e,f]:
                                continue
                            for h in range(1,11):
                                if h in [a,b,c,d,e,f,g]:
                                    continue
                                for i in range(1,11):
                                    if i in [a,b,c,d,e,f,g,h]:
                                        continue
                                    for j in range(1,11):
                                        if j in [a,b,c,d,e,f,g,h,i]:
                                            continue
                                        if a+b+c==d+c+e==f+e+h==g+h+i==j+i+b:
                                            printnum(a,b,c,d,e,f,g,h,i,j)
