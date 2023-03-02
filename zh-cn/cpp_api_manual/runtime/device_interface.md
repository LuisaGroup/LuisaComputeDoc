# DeviceInterface

## 类定义
* 目录: src/runtime/device_interface.h
* 所属工程目标：lc-runtime

## 注解
TEXT_BEGIN
DeviceInterface类型是前端提供给后端的接口类，后端会保证这个类型内所有的函数实现都是线程安全的。通常您只需要直接使用[Device](device.md)类型就可以完成操作，不需要手动操作这里面的方法，但对于其他非C++的语言绑定（如我们已经提供的Python方案），就需要直接使用这个类型里的方法。
TEXT_END