import requests

alarm_url = "https://open.feishu.cn/open-apis/bot/v2/hook/3d6bc1af-c96d-4f79-9dfc-65c6617ad525"
alarm_heads = {
    "Content-Type": "application/json"
}
alarm_data = {
    # "msg_type":"text",
    # "content": {
        # "text": "<at user_id='all'>所有人</at>今天我很快乐"
        # "text":"err: 123 \ndetailed information: 232434",
        # {
        "msg_type": "post",
        "content": {
                "post": {
                        "zh_cn": {
                                "title": "测试用例小助理",
                                "content": [
                                        [{
                                                        "tag": "text",
                                                        "text": "case : 001\n信息 : \t用户名admin\n\t密码 : RealAI@20221\n\tresult : 失败\n"
                                                },
                                                {
                                                        "tag": "a",
                                                        "text": "点击查看\n",
                                                        "href": "http://www.baidu.com"
                                                },
                                                {
                                                        "tag": "at",
                                                        "user_id": "all"
                                                }
                                        ]
                                ]
                        }
                }
        }
}
request = requests.post(url=alarm_url, json=alarm_data, headers=alarm_heads) 
print(request.text)
