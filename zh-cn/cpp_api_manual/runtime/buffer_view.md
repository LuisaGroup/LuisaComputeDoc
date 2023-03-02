# BufferView

## 类定义
* 目录: src/runtime/buffer.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
BufferView实例会指向[Buffer](buffer.md)实例，并保留一份偏移和体积，这方便前端语言进行引用传递和，类型转换和二次处理，如切分。
TEXT_END