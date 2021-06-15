#ifndef _COROUTINE_H
#define _COROUTINE_H

#include <ucontext.h>

#define CO_STACK_SIZE 16*4096

typedef void (*co_fn)(void);

static ucontext_t uctx_main;

typedef enum {
    CO_CREATE=0,
    CO_RUNNINE=1,
    CO_SUSPEND=2,
    CO_END=3
}CO_STATUS;

typedef struct {
    coroutine_t *c_main;
    coroutine_t *c_curr;
}sched_t;

typedef struct {
    ucontext_t ctx;
    CO_STATUS status;
}coroutine_t;

int create_coroutine(co_fn pfn)
{
    char* stack = (char *)malloc(CO_STACK_SIZE);

}

int sched() 
{

}

#endif