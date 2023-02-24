# ContextPath

## 类定义
* 目录: src/core/binary_io.h
* 所属工程目标：lc-core

## 注释
LC默认的文件读写是在[Context](../runtime/context.md)指定的硬盘目录下读写，这可能是大多数情况的通用方案，但并不是全部。若您希望从其他途径获取文件（如网络，内存）等，那么编写一个继承自BinaryIO类的新类型是不错的选择。编写的实例可以通过[Device](../runtime/device.md)::set_io(BinaryIO *)设置，请注意，该指针的声明周期不由Device类型管理。