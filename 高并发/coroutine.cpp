#include <ucontext.h>

using coroutine_context = ucontext_t;
using coroutine_fn = void* (*func)(void *);

class Coroutine{
private:
    coroutine_context ctx;
public:
    Coroutine(coroutine_fn cfn, void *ctx)
};

