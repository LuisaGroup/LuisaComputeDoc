# CommandList

## 类定义
* 目录: src/runtime/command_list.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
CommandList类型是被[Stream](stream.md)类型用于收集和提交命令的子类型，其本身可以单独工作，收集命令和回调并提交。当您希望在多处收集命令，并集中提交到某个[Stream](stream.md)时，可以单独使用CommandList。
CommandList的提交伪代码如下：
// 将命令和回调收集进CommandList
command_list << cmd0 << callback << cmd1;
// 提交收集的命令和回调
stream << command_list.commit();
请注意，与Stream严格保证顺序不同的点在于，CommandList类会独立存放命令和回调，提交时只有所有命令都被执行完毕，才会开始执行回调。因此在本例中，实际的执行顺序是cmd0, cmd1, callback，而非直观的cmd0, callback, cmd1 。这是十分容易混淆的点，但我们认为这是正确的设计。因为当您决定使用CommandList而非Stream时，意味着commit操作是一个十分谨慎的操作（如在游戏引擎的应用中，可能一个Stream每一帧只应提交一次，更多的提交可能导致致命的Bug），那么CommandList类理应与任何Stream脱开关系。这意味着只有在主动调用commit时，才会将所有操作一次性提交，而由于异构编程的特殊性，回调只有在所有被提交的命令执行结束后才可以被调用。
TEXT_END