# Stream

## 类定义
* 目录: src/runtime/command_buffer.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
CommandBuffer类型是为了满足Stream类型无法达成的多次录制指令集中提交的功能。通常其实例由Stream::command_buffer()创建，在销毁前，必须保证其内部所有命令已经被提交。使用CommandBuffer提交命令的方法与[Stream](stream.md)接近。
TEXT_END