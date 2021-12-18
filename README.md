# Bing Wallpaper

> :sparkles: GitHub Action 自动抓取必应壁纸

从 2021.09.08 日开始

目前发现一个问题是 Github Actions 分配来的主机不是中国ip，得到的壁纸都是国际版的。


---
2021.12.16 必应搜索遭到屏蔽，国内部分地区已无法访问
解决方法是系统 hosts 文件添加以下内容：

```
13.107.21.200 cn.bing.com
204.79.197.200 cn.bing.com
```
