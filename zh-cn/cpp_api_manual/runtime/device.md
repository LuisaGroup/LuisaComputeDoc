# Device

## 类定义
* 目录: src/runtime/device.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
Device是连接计算后端最基础的类型，其内部所有API都是上下文无关且线程安全的，且不提供具体计算命令的提交（计算命令的提交需参考[Stream](stream.md), Device通常由Context::create_device生成实例。作为[DeviceInterface](device_interface.md)类的包装类，它内部会持有一份shared_ptr引用。
TEXT_END