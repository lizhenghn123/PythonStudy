#! /usr/bin/env python
# -*- coding=utf-8 -*-
# date = 2015-04-28
import base64
import urllib2
import urllib
import json
import wave

# 测试百度语音识别云服务（需要注册）
# see http://yuyin.baidu.com/dev_sdk.php
# 结论：识别率有待提高啊

def get_token():
    URL = 'http://openapi.baidu.com/oauth/2.0/token?'
    params = urllib.urlencode({'grant_type': 'client_credentials',
                                'client_id': 'vNQLdYXnf7koRfj2U5fwQfsX',              # 这个需要自己注册
                                'client_secret': 'zws4xnrFiBEvWbNwcWtV9RZiN7A8lqN4'}) # 同上
    res = urllib2.Request(URL, params)
    response = urllib2.urlopen(res)
    data = response.read()
    data = json.loads(data)
    #print data
    #print data['access_token']
    return data['access_token']

def recog_speech(wav_file):
    try:
        wav_file = open(wav_file, 'rb')
    except IOError:
        print(u'文件错误')
        return
    wav_file = wave.open(wav_file)
    n_frames = wav_file.getnframes()
    frame_rate = wav_file.getframerate()
    #print(n_frames, frame_rate)
    if frame_rate not in (8000, 16000):  # 采样率，支持 8000 或者 16000
        print(u'不符合格式')
        return
    
    audio = wav_file.readframes(n_frames)
    seconds = n_frames/frame_rate+1
    minute = seconds/60 + 1
    #print minute, seconds
    
    for i in range(0, minute):            # 百度限制每次识别的语音时长不能超过 1 分钟
        sub_audio = audio[i*60*frame_rate:(i+1)*60*frame_rate]
        base_data = base64.b64encode(sub_audio)  # 必须进行base64编码
        data = {"format": "wav",          # 语音压缩的格式
                "token": get_token(),     # 开发者身份验证密钥
                "len": len(sub_audio),    # 原始语音长度，单位字节
                "rate": frame_rate,       # 采样率
                "speech": base_data,      # 真实的语音数据，需要进行base64编码
                "cuid": "B8-AC-6F-2D-7A-97",  # 用户id，推荐使用 mac 地址/手机IMEI等类似参数
                "channel": 1}             # 声道数，仅支持单声道，请填写 1
        data = json.dumps(data)           # json 格式
        req = urllib2.Request('http://vop.baidu.com/server_api',
                              data,
                              {'content-type': 'application/json'})  # 表单类型
        response = urllib2.urlopen(req)
        result = json.loads(response.read())
        # 如果成功，result = 
        # {\"err_no\":0,\"err_msg\":\"success.\",\"corpus_no\":\"15984125203285346378\",
        #  \"sn\":\"481D633F-73BA-726F-49EF-8659ACCC2F3D\",\"result\":[\"北京天气\"]}
        print result['result'][0].encode('utf-8')

if __name__ == '__main__':
    recog_speech('3s.wav')