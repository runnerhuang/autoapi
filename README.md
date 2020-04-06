#  配置环境：
python 3.6以上即可  
如需自动打开测试报告，还需要在网上下载对应版本的Firefox浏览器驱动文件，将浏览器驱动文件放入python3目录下即可（当然你也得装火狐浏览器）
https://github.com/mozilla/geckodriver/releases
 
#  使用方法：
##  一. 自动化工程python所需依赖库
执行命令：  
pip install -r requirements.txt  


##  二．工程项目运行方法：

###  工程项目运行方法：

####  1.只运行某一个测试用例
python main.py -F '测试路径的文件路径' -N 001  

例子：  
python main.py -F 'TestCase//EATOJOY//BACKEND//PUSH' -N 001
意思是执行TestCase//EATOJOY//BACKEND//PUSH目录下001序号文件夹里的所有test cases，若不设置-N则运行该目录下所有用例

####  2.运行同一目录下的多个测试用例(运行多个的时候，必须将-N的值设置成0)

python main.py -F '测试路径的文件路径' -CL '1,2'  

例子：
python main.py -F 'TestCase//EATOJOY//BACKEND//PUSH' -CL '1，2'
意思是依次执行TestCase//EATOJOY//BACKEND//PUSH目录下001和002序号文件夹里的所有testcase  
ps：若要运行多个路径下的用例则用;隔开，如-F 'TestCase//xxx//xx1;TestCase//xxx//xx2'

###  运行参数介绍：
-F 必选，测试用例目录，约定一般放在TestCase目录下面，[目录命名规则](#jump)    
-N 可选，默认0(全部用例)，运行指定单个用例   
-CL 可选，默认空，运行多个用例 **【此参数与-N互斥，优先-N】**  
-TD 可选，默认1 （默认不执行teardown，0表示执行）  
-ENV 可选，默认test为测试环境，切换环境参数（项目配置中"项目名称_test.ini"代表项目测试环境的配置)   
-E 可选，默认0表示不发邮件，-E 1表示为发邮件（邮件接受人配置为项目ini文件中）  
-DR 可选，默认0表示不执行项目数据准备文件，-DR 1表示执行项目数据准备文件（项目准备的意思是执行用例前准备一些共用的数据，  
函数放在TestData文件夹下的"项目名称_dataReady"文件中）  
-RR 可选，默认为0表示为失败不重跑，-RR 1表示为用例失败后重跑一次，-RR 2表示为用例失败后重跑两次   
-LP 可选，默认0，循环执行，例如：-LP 1000 执行1000次


##  三.编写测试用例：
###  1.做API接口测试的相关人员对于写json的用例熟悉。

范例:  
```
{
	"input":{
			"method": "POST",
			"url":"http://XXXXX.XXXXX.com/",
			"rest": "XXXX/XXXX",
			"headers": {
				"token":"{{pre.token}}"
			},
			"param":{
				"phoneNumber":"XXXXXXXXXXX", 
				"password": "123456"
			}
	},
  "output":{ "msg": {"EQ":"【成功】"}, "dealer_token": {"TYPE":"str"}, "business_type_id": {"EQ":4}
      },
  "key": ["dealer_token"] 或者 "key": {key: value}
}
```

SQL范例：  
```
{
	"sql":{
	        "db":"dbpos",
	        "command": [
                "delete from 表名 where id = {{key.uid}}",
                "delete from 表名 where user_id = {{key.uid}}",
                "delete from 表名 where user_id = {{key.uid}}",
                "delete from 表名 where user_id = {{key.uid}}",
                "delete from 表名_record where user_id = {{key.uid}}"
            ]
            }
}
```

如果有select出现需要保存数据时，范例：  
```
{
	"sql":[
		"select id from 表名 where mobile = {{pre.User1}}"
	],
	"key": ["id"]
}
```
###  2.参数详解  

其中input是接口请求的部分,包括请求的地址(url+rest), headers在这里是会带上用户或商户登录后产生的token。
param为请求报文。  

output这里是为了检查每个返回值的类型/具体值/或者其他定义的校验值。如不需要校验可以不带或为空对象
可以直接具体到每个值  
例如：  
```
{
	"input":{
			"method": "GET",
			"url":"{{pre.XXXX_url}}",
			"rest": "ja/v1/test/sms/regist?",
			"headers":{"client": "android",
                        "Content-Type": "application/json"
				},
			"param":{
				"phone":"{{pre.User1}}", "code": "{{key.code}}"
			}
	},
  "output":{"code": {"ALLIN":[0,"1234"]},"msg":{"TYPE":"str"}, "data":{"TYPE":"dict"}，"data.code":{"EQ":"1234"} },
  "key":{"code":"data.code"},   # 将data.code返回保存为key值为code
  "sleep":5
}
```
{{pre.token}}:指的是在TestData/项目名_data文件中的preData数组里的变量值，用于保存一些可以重复使用的变量，例如token，url
{{key.code}}:指的是调用在本次执行的test cases中前几个测试步骤保存的key值  
key:为在当前步骤需要保存的某个返回key值对应的value, 如果保存之前已经有当前key值存在,当前的key,value对会被更新替换。如不需要保存key可以
不带此健或为空。  
"sleep":5:指的是睡眠5秒  


##  四.测试用例文件名命名：
###  1. <a id="jump">TestCase//项目名称//平台端//功能模块//测试用例名称 </a>
*示例：*  
**项目名称**：EATOJOY  
**平台端**：BACKEND（后台），VENDOR（商家端）   
**功能模块**：LOGIN（登录模块），PAY（支付模块）   
**测试用例名称**：LOGIN_001_登录正确的用户_异常/正常，尽量使用意思明切的命名  

###  2.测试步骤文件命名
001.json,002.json严格按照数字大小区分测试步骤顺序


##  五.新项目使用：
### 1.配置项目数据Config
   -  命名:项目名_环境.ini  
        ```如E肚仔测试test环境：eatojoy_test.ini```
   -  模块:project_info,test_db,email_info,url
   -  代码内调用配置   
举例:   
  ```
  from Config import config
  config.ReadConfig.get_project("version")
  ```
    
### 2.配置业务测试数据TestData
   -  命名:项目名_data.py  
        ```如E肚仔：eatojoy_data.py```
   -  创建一个preData字典，通过preData["xxx"]读取
   -  项目名_dataReady.py 项目运行前创建数据
   
### 3.配置公用模块函数ProjectPublic
   -  命名:项目名Public.py  
        ```如E肚仔：EatojoyPublic.py```
   -  模块:创建一个class，通过调用class的静态方法@staticmethod，如EatojoyPublic.CreateVendor  
   
### 4.编写用例TestCase
1.覆盖接口文档中能实现接口自动化的接口  
2.时间不充裕可以只覆盖所有接口能够请求成功的用例，有充裕的时间可以对接口进行一些参数的异常值分析，但是重要业务的接口要覆盖所有的情况，比如说支付的用例，支付失败的用例，重复支付的用例，超时支付的用例  
例如：
XXX参数为0，XXX参数为-1，XXX参数为int值的最大值，XXX参数为int值的最小值，XXX参数为int值的最大值+1，XXX参数为int值的最小值-1，XXX参数为float类型，XXX参数为string类型，XXX参数为空，XXX参数为空格等等  
3.尽量更多的覆盖到所有的业务场景，例如某个接口有一个参数有多种类型，就要把所有类型都走一遍  
例如：
商家拒单类型为：其他原因，商家拒单类型为：商家备料不足，商家拒单类型为：商家暂停营业，商家拒单类型为：商家订单超载，商家拒单类型为：无法按时出餐，商家拒单类型为：用户要求取消订单等等
### 5.公共函数
1.公共函数的执行
    001.json:
    
    无参数版本
   ```
   { 
  "public":  
    [
    {  "class": "ProjectPublic.HotelPublic.HotelPublic", 
    "function": "GetCodeLogin" 
    } 
    ]
    }
   ```
  
    有参数版本

   ```
   { 
  "public":  
    [
    {  "class": "ProjectPublic.HotelPublic.HotelPublic", 
    "function": "GetCodeLogin" ,
    "arg":"参数"
    } 
    ]
    }
   ```
   上述为执行公共函数,在ProjectPublic//HotelPublic路径下的HotelPublic类class的GetCodeLogin方法  
   另外一种写法，可以与http接口混合在还一起
   001.json:

   ```
   {
	"public":  
    {  "class": "ProjectPublic.HotelPublic.HotelPublic", 
    "function": "GetCodeLogin" 
    } ,
	"input": {
		"method": "POST",
		"url": "{{pre.hotel_url}}",
		"rest": "/reserve",
		"headers": {
			"Content-Type": "application/json",
            "client": "IOS",
            "token": "{{key.token}}"
		},
		"param": {
			"hotel_id": "{{pre.hotel_id}}",
			"room_type_id": "{{pre.room_type_id}}",
            "num": 1,
            "start": "{{pre.hotel_date_start}}",
            "end": "{{pre.hotel_date_end}}",
            "linkman": "hsm",
			"is_me": 0
		}
	},"key":{"order_id":"data.orderSn"}
    }

   ```
2.创建函数的执行
    001.json:
    
    无参数版本
   ```
   { 
  "new":  
    [
    {  "class": "Common.util", 
    "function": "random_11int" ，
    "key":"[phone]"
    } 
    ]
    }
   ```
  
    有参数版本

   ```
   { 
  "new":  
    [
    {  "class": "Common.util", 
    "function": "random_11int" , ，
    "key":"[phone]",
    "arg":"参数"
    } 
    ]
    }
   ```
   上述描述的是执行的是创建相关key值函数,在Common//util路径下的random_11int方法返回的值保存在phone中，
   在接下来的用例中使用{{key.phone}}调用  
   另外一种写法，可以与http接口混合一起  
   
   001.json:
   ```
      { 
     "new":  
    [
    {  "class": "Common.util", 
    "function": "random_11int"  ，
    "key":"[phone]"
    } 
    ]
    },
	"input": {
		"method": "POST",
		"url": "{{pre.hotel_url}}",
		"rest": "/reserve",
		"headers": {
			"Content-Type": "application/json",
            "client": "IOS",
            "token": "{{key.token}}"
		},
		"param": {
			"hotel_id": "{{pre.hotel_id}}",
			"room_type_id": "{{pre.room_type_id}}",
            "num": 1,
            "start": "{{pre.hotel_date_start}}",
            "end": "{{pre.hotel_date_end}}",
            "linkman": "hsm",
			"is_me": 0
		}
	},"key":{"order_id":"data.orderSn"}
    }

   ```