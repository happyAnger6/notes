# TCP

## tcp连接的建立与终止

### mss最大报文分组

+ UDP很容易导致IP分片
+ TCP试图避免分片,但对于应用程序来说几乎不可能强迫TCP发送一个需要进行分片的长报文段

