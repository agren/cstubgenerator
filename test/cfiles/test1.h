/*
	This multiline comment
	should be removed.
*/

/* asdf */

/* 1 */  /* a will be removed if ? isn't used in the regexp */

#ifndef TEST1_H_
#define TEST1_H_

#include <stdint.h>
// This single line comment should be removed.

typedef uint16_t test1_t;

void test1_func(test1_t arg1, uint8_t arg2, volatile unsigned short int arg3);
volatile const uint8_t test1_func(test1_t arg);

#endif
