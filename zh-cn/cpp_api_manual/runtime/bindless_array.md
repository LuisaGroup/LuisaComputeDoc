# BindlessArray

## 类定义
* 目录: src/runtime/bindless_array.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
BindlessArray类型提供了在Kernel中随机读取访问一个资源的能力。如通过整数格式的索引直接读取某个未作为参数绑定的Buffer或Image类。注意，BindlessArray的所有更新都需要经过[CommandList](command_list.md)并提交进[Stream](stream.md)，因此对其元素的操作均需要延迟执行，且BindlessArray::update()操作不是线程安全的，您需要保证在录制update指令时，没有另一个线程正在操作当前的实例。
TEXT_END