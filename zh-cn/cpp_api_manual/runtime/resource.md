# Resource

## 类定义
* 目录: src/runtime/resource.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
Resource是所有资源类型的基类，其内部保留了一个uint64值作为指向后端的句柄，当该值为invalid_resource_handle，即uint64的最大值时，当前resource处于不可用状态。所有Resource的实例都保留了一份[DeviceInterface](device_interface.md)类型的shared_ptr引用，这是为了Device实例不会在所有resource都被销毁之前被销毁。
TEXT_END