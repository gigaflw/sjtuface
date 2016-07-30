# sjtuface

SJTU 2016暑期社会实践项目

人脸识别系统

使用face++ api

语言：python2

---
usage:

  首先复制`apikey.cfg.example`到`apikey.cfg`

  然后修改其中的`API_KEY`和`API_SECRET`为正确的值

  然后

  \# to initialize/reconstruct database
  
  $ python main.py -i
  
  \# to identify face
  
  $ python main.py -f < path-to-your-image >

e.g.

  在`sjtuface/database`下存有用来构建数据库的照片
  
  在`sjtuface/target`下存有需要识别的照片`1.jpg`
  
  则
  
  $ python main.py -i -f target/1.jpg
  
  将初始化数据库同时对`target/1.jpg`这张图片进行识别
