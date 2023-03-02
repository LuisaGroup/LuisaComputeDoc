# Image

## 类定义
* 目录: src/runtime/image.h
* 所属工程目标：lc-runtime

## 注解
HTML_BEGIN
Image类型代表2D的数据结构，由于平台限制，Image类型不能够使用自定义的结构体类型，而是仅提供float, uint32_t, int32_t作为基础类型。注意，Image<float2>这类写法是错误的，Image只支持标量类型，对于其实际存储格式，由传入的PixelStorage枚举值控制，在DSL模块中所有读取和写入都将强制使用4通道向量格式，如float4, int4等。
HTML_END