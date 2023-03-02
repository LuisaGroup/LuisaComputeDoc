# Buffer

## 类定义
* 目录: src/runtime/buffer.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
Buffer是基础的数据结构，它代表一个一维的定长数组结构，出于平台兼容性考虑，Buffer使用的类型要求必须体积和对齐在4字节以上，可以通过[Device](device.md)::create_buffer函数创建实例。对一个Buffer进行切分或类型转换是可以接受的，这类操作会返回[BufferView](buffer_view.md)。
TEXT_END