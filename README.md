#youdao
基于Python 在控制台下查单词的小工具，基于有道词典API。
受<https://github.com/Flowerowl/ici> 启发，用requests 库和有道的API 写一遍练习一下。

###1.运行效果
支持中文，句子翻译

	$ yd keyword
![截图1](./pic1.png)

	$ yd
		input a word: 饺子
![截图2](./pic2.png)


###2.安装

	sudo python setup.py install
安装好后在控制台直接调用yd 或者 yd keyword 即可

###3.设置自己的API key
一个key 每分钟只能发起1000次请求，可以去有道自行申请一个API key，地址：
<http://fanyi.youdao.com/openapi?path=data-mode>

修改youdao.py 中如下部分即可

	params = {
        'keyfrom': 'longcwang',
        'key': '131895274',
        'type': 'data',
        'doctype': 'json',
        'version': '1.1',
        'q': 'query'
	    }