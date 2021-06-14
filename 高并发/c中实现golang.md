# 如何在C语言中实现Golang

## Golang介绍

Golang语言2007年诞生于Google,Google发明这门语言的目的是什么呢?

### 从语言层面直面问题

传统的语言c++, java, python等,都和其使用的计算环境无关.  
随着多核处理器、网络化系统、大规模计算集群的发展以及Web编程模型的发展,这些传统语言虽然也能应付,但都没有直面面对这些问题.  
此外,程序规模也发生了变化:今天的服务器程序由数千万行代码组成,由成百上千的程序员编写,每天都在更新.  
更糟糕的是,构建时间,即使是在大型编译集群上,也已经延长到了几分钟甚至几小时.

为了解决上述问题,Go语言诞生了.Go提升了在新计算环境下的生产力,比如:Go提供了内置的并发和垃圾回收.  
Go的设计还考虑了软件包的依赖管理,软件架构的可扩展性以及组件间边界的健壮性.  

Go语言是为了解决实际遇到的问题而诞生的,因此虽然从语言层面可能并没有多少突破和创新,但是在工程上还是很有活力.

#### 思考

基于Go的诞生背景,我们可能会提出疑问:在原有语言基础上能否也提供类似Go的解决方案,至少在C中能否做到?  
带着上述思考,[COROUTINE项目](https://github.com/happyAnger6/treasure_house.git)诞生了,希望通过此项目,一方面可以提高C在现代计算环境中的生产力,另一方面也可以对Go的实现以及Go对现代环境编程的思考有所理解.

## coroutine项目介绍

[项目地址](https://github.com/happyAnger6/treasure_house/tree/master/src/coroutine)  
目前还在treasure_house中,由于目前只有我一个人在开发,后面会拆单独仓.


目前项目刚刚起步,初步实现了用户态协程的创建和调度功能,下一步需要实现运行库及相关asyncio api.  
一个人的能力和时间毕竟有限,希望有兴趣的小伙伴一起来参与.

### 实现说明(持续更新中)

#### COROUTINE状态

corouting有3种状态, RUNNALBE, RUNNING, WAITING.

+ WAITING: corouting暂停并等待一些条件以继续运行.比如:系统调用,同步操作(原子或锁操作),这种延迟是性能差的根源.
+ RUNNABLE: corouting具备运行条件正在等待分配processor以执行指令
+ RUNNING: corouting已经分配到processor,并正在上面执行指令


#### 上下文切换

##### 原理

corouting在用户态进行上下文切换,上下文主要包括:堆栈,寄存器(IP, SP等).  
上下文切换主要通过<ucontext.h>中定义的getcontext, setcontext, makecontext, swapcontext实现.

##### 时机

+ corouting主动调用coroutine_yield(),如果有其它待运行的coroutine则主动让出processor
+ 协程库asyncio API选择合适的时机进行上下文切换,如调用阻塞API,如corouting_sleep. 
+ 如果你在协程中执行cpu密集型操作或直接调用阻塞的C api,那么会影响当前processor的调度和运行.

#### asyncio

+ asyncio提供一系列api用于在协程环境中编写并发代码.
+ asyncio是coroutine框架提供的api可以用于实现高性能网络服务器,数据库连接库,分布式任务队列等.
+ asyncio适合IO密集型和高级别的结构化网络程序
