cstubgenerator
==============
Generates .c files from header files. Each function declared in the header file while get an empty function definition the resulting output file.

##Requirements
###pycparser
Handles parsing of the files
See https://github.com/eliben/pycparser on how to install.

##Usage
usage: cstubgenerator.py [-h] file.h [file.h ...]

##Example
`./cstubgenerator test1.h`

Feeding in the file test1.h:
```c
#ifndef TEST1_H_
#define TEST1_H_

#include <stdint.h>

typedef uint16_t test1_t;

void test1_func(test1_t arg1, uint8_t arg2, volatile unsigned short int arg3);
volatile const uint8_t test1_func(test1_t arg);

#endif
```
produce the following file test1.c:
```c
// Automatically generated from: test1.h

#include "test1.h"

void test1_func(test1_t arg1, uint8_t arg2, unsigned short int volatile arg3) { // test1.h:18

}

uint8_t volatile const test1_func(test1_t arg) { // test1.h:19

}

```
