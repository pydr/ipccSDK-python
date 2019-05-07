## ipccSDK-python Demo

---

 <img src="https://img.shields.io/badge/python-3.0-blue.svg">

ipcc呼叫中心sdk



### interpretation

----

| API               | 说明                       |
| ----------------- | -------------------------- |
| out_call          | 发起通用外呼               |
| notify            | 发起通知型呼叫（语音通知） |
| hungup            | 挂机                       |
| play              | 播放语音文件/TTS           |
| stop_play         | 通知播放当前语音/TTS       |
| transfer          | 呼叫转接                   |
| multi_play        | 播放多段语音/TTS           |
| upload_voice_file | 上传语音文件               |



### Before you begin

---
- 需要自己准备好回调URL

- 向腾讯云申请开通 ```云呼叫中心``` 功能

- 记录腾讯云分配的测试号码及appid

- 呼叫中心采用ip白名单及appid鉴权机制，故您需要向腾讯云提供能的测试/生产环境的ip


### Usage

---

#### Installation

```bash
$> cd ipccSDK-python
$> python setup.py install
$> pip install -r requirements.txt
```

#### Example

修改```example.py``` 代码中的配置

```python
appid = "turing-test"  # 申请的appid
host = "http://172.17.0.10"  # 分配的ipcc server
number = "9512345" # 分配的测试号码
```

运行 ```example.py```

```bash
$> python example.py
```



### Documentation

---

<a href="https://cloud.tencent.com/document/api/679/14499">中文文档</a>



### Quick Start

---

#### 创建ipcc client

```python
from ipcc.client import Client
client = Client(host, appid)
```

#### 发起通用呼叫

```python
client.out_call(number, "13800138000")
```

#### 发起通知型呼叫

```python
client.notify(number, "13800138000", "我的梦想是世界和平")
```

#### 挂机

```python
client.hungup(callid)
```

#### 播放语音/TTS

```python
# flag=1为播放录音文件模式，对应voice需传入语音文件路径
# flag=0为播放tts模式，对应voice需传入文本
client.play(callid, flag, voice)
```

#### 停止当前播放

```python
client.stop_play(callid)
```

#### 转接

```python
client.transfer(callid, called, voice)
```

#### 上传录音文件

```python
client.upload_voice_file(file_path, file_name)
```



### ipcc事件回调

---

ipcc处理事件之后会有相应的通知事件回调到调用服务器， 开发者可根据具体需求对事件进行处理。具体可参照ipccSDK-python/server/server.py中的相应代码进行开发。

#### Callback url

```
POST /v1/ipcc/callback
```

