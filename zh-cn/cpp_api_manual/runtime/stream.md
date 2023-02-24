# Stream

## 类定义
* 目录: src/runtime/stream.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
Stream类型是处理计算命令的基本类型，通常其实例由Device::create_stream()创建，它会将命令录制以流的形式录制下，并在流结束时提交，在以下伪代码中：
auto callback = [](){ };
stream << cmd0 << cmd1 << callback << cmd2 << cmd3
首先cmd0与cmd1会被录制到stream中，并在语句结束后自动提交到后端异步执行（在cmd0和cmd1被执行结束后，callback会被后端在异步线程中调用），与此同时cmd2, cmd3会被录制并提交给后端，其中每一条命令的执行顺序都是严格保证的，但是如果这些命令之间没有互相依赖的资源，LC将会自动将其列为并行任务以获得最大的性能提升，同时，由于提交命令本身有一定的性能开销，最佳的实践是一次性尽可能提交更多的命令。
在实际应用中，可能存在不能一个语句提交所有命令的情况，这种时候[CommandList](command_list.md)可以满足多次录制并集中提交的需求。
TEXT_END