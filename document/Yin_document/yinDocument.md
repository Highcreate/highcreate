## Yin



#### DB

 - Table名
    -  inclubInfo
 - column名
   - matuyaId
     - ID
     - Primary key
     - データ形: int
   - matuyaData
     - 年月日
     - データ形: VARCHAR(0,100)
   - matuyaCategory	
     - カテゴリ
     - データ形: VARCHAR(0,100)
   - matuyaTitle
     - タイトル
     - データ形: VARCHAR(0,100)
   - matuyaContact
     - 宛先
     - データ形: VARCHAR(0,100)
   - matuyaText
     - テキスト
     - データ形: VARCHAR(0,200)

#### URL

 - 社内通知画面
   - http://127.0.0.1:8000/content/

 - 社内通知編集画面
   - http://127.0.0.1:8000/detail/1
   - p.s
     - http://127.0.0.1:8000/detail/1　1是id编号
 - 全部データ一览画面
   - http://127.0.0.1:8000/detail
 - 添加画面
   - http://127.0.0.1:8000/matuyaindex/ 
 - 削除画面
   - http://127.0.0.1:8000/matuyadelet/
  



#### HTML

- matuyaindex.html

  - 测试用可以添加数据 对送骨保密

- detail.html

  - 全てデータ一览

- content.html

  - 社内通知demo

- getdetail.html

  - 社内通知編集demo
  
- matuyaDelet.html 
 
  - 对送骨保密削除画面
     



#### views.py

- def
  - matuya_index
    - 对送骨保密画面
  - matuya_delet
    - 对送骨保密削除画面
  - content
    - 社内通知画面(据库第一个数据显示)
  - detail
    -  全てデータ一览画面
  - get_detail
    - 社内通知編集画面
    - p.s.
      - 与detail不同在于 右侧有编辑
      - 跳转原理: id在url后面追加 更具id查询
  - matuya_add
    - データ保存操作
  - delet
    - データ削除操作