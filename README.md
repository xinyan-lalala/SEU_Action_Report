# SEU_Action_Report
![Stars](https://img.shields.io/github/stars/quzard/SEU_Action_Report.svg)
![Forks](https://img.shields.io/github/forks/quzard/SEU_Action_Report.svg)

**利用GitHub的action进行健康上报**

支持定时上报以及start上报（star一下自己fork后的项目就会启动上报action）

**fork后记得添加变量，并去Actions那Enable Workflow。可以star一下自己fork后的项目测试action是否可以正常启动**

如有使用问题，请发issue![issue](/img/4.png)

## 使用步骤

Ⅰ. **首先 fork 本项目到自己的仓库**![fork](/img/1.png)

- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `去Actions那Enable Workflow`


Ⅱ. **进入自己 fork 的仓库，点击 Settings-> Secrets-> New repository secret，它们将作为配置项，在应用启动时传入程序。**

**例如下图。添加 其中1 个 Secrets，其名称为ID，值为一卡通号**

![Secrets](/img/5.png)

**所有的可用Secrets及说明**

![Secrets](/img/2.png)

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| ID         | 一卡通号                                                     |
| PASSWORD   | 一卡通密码                                                   |
| NAME       | 姓名（可选）                                                 |
| KU         | 酷推的Skey（可选）可用于qq推送上报通知。学习链接https://cp.xuthus.cc/ |
| SERVERCHAN | 新版server酱的Skey（可选）可用于微信推送上报通知。学习链接https://sct.ftqq.com/ |

Ⅲ. **如果需要修改上报时间，修改.github/workflows/auto_temperature.yml**
![cron](/img/3.png)


## Stargazers over time
[![Stargazers over time](https://starchart.cc/Quzard/SEU_Action_Report.svg)](https://starchart.cc/Quzard/SEU_Action_Report)
