import requests
import json
import ast
from random import choice
class TuLin(object):
	def __init__(self,city,text=None,img_url=None,province=None,street=None):
		self.all_key = [
			'b2c05bbcc375412f8621e433648748fc',
			'233301805efc4e32a95c95bf5de7af4a',
			'e623e8acef674f36ad6ccd9b8f9934d3',
			'ea284a3fb5914c6498dcbf4eeb772aab',
			'9adec2d2c4fc4de4bb186c6e1e5119c8'
		]
		self.key = choice(self.all_key)

		self.url = 'http://openapi.tuling123.com/openapi/api/v2'
		self.data = {
				"reqType":0,
			    "perception": {
			        "inputText": {
			            "text": text
			        },
			        "inputImage": {
			            "url": img_url
			        },
			        "selfInfo": {
			            "location": {
			                "city": city,
			                "province": province,
			                "street": street
			            }
			        }
			    },
			    "userInfo": {
			        "apiKey": self.key,
			        "userId": "wechat"
			    }
			}
		self.data = json.dumps(self.data)

	def send_request(self):
		response = requests.post(self.url,data=self.data)
		dict = ast.literal_eval(response.text)
		print(dict['intent']['code'])
		if dict['intent']['code'] != 10004:
			self.all_key.remove(self.key)
			self.key = choice(self.all_key)
			self.send_request()
		return response.text
	# {"intent":{"code":4003},"results":[{"groupType":0,"resultType":"text","values":{"text":"请求次数超限制!"}}]}
	def run(self):
		response  = self.send_request()
		print(response)


if __name__ == '__main__':
		city = input("请输入你的地址(这个是必填的)\n")
		print('文字和图片地址必须填一个')
		text = input('请输入你要发送的文字,(可以选择不填)\n')
		img_url = input('请输入你要发送的图片地址,(可以选择不填)\n')
		province = input("可以选择不填,请输入你的省份(可以选择不填)\n")
		street = input('可以选择不填,请输入你的街道\n')
		tl = TuLin(city=city,text=text,img_url=img_url,province=province,street=street)
		tl.run()

