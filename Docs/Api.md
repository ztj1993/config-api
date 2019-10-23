# 接口文档

## 快速预览
```
初始配置：/init
加载数据：/<cursor_id>/load/<data_type>
设置数据：/<cursor_id>/set/<data_type>
追加数据：/<cursor_id>/append/<data_type>
删除数据：/<cursor_id>/unset
获取数据：/<cursor_id>/get/<data_type>
输出数据：/<cursor_id>/set/<data_type>
```

## 详细说明

### 初始配置
- 接口路径：/init
- 返回数据：游标编号 (cursor_id)

### 加载数据
- 接口路径：/<cursor_id>/load/<data_type>
- 返回数据：ok

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
data_type|path|是|数据类型，支持 json, yaml
-|data|是|数据

### 设置数据
- 接口路径：/<cursor_id>/set/<data_type>
- 返回数据：ok

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
data_type|path|是|数据类型，支持 json, yaml, str, bool
key|query|是|键
-|data|是|数据

### 追加数据
- 接口路径：/<cursor_id>/append/<data_type>
- 返回数据：ok

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
data_type|path|是|数据类型，支持 json, yaml, str, bool
key|query|是|键
-|data|是|数据

### 删除数据
- 接口路径：/<cursor_id>/unset
- 返回数据：ok

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
key|query|是|键

### 获取数据
- 接口路径：/<cursor_id>/set/<data_type>
- 返回数据：根据 <data_type> 返回

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
data_type|path|是|数据类型，支持 json, yaml, str
key|query|是|键

### 输出数据
- 接口路径：/<cursor_id>/set/<data_type>
- 返回数据：根据 <data_type> 返回

参数名|类型|必填|说明
---|---|---|---
cursor_id|path|是|游标编号
data_type|path|是|数据类型，支持 json, yaml
