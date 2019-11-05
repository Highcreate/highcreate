## YinDemoMemo


#### DB
 - Table名
    -  inclubInfo
 - column名
   - matuyaId
     - 名: ID
     - Primary key
     - データ形: int
   - matuyaData
     - 名: 年月日
     - データ形: VARCHAR(0,100)
   - matuyaCategory	
     - 名: カテゴリ
     - データ形: VARCHAR(0,100)
   - matuyaTitle
     - 名: タイトル
     - データ形: VARCHAR(0,100)
   - matuyaContact
     - 名: 宛先
     - データ形: VARCHAR(0,100)
      - 设计有问题
   - matuyaText
     - 名: テキスト
     - データ形: VARCHAR(0,200)


#### URL
 - 社内通知編集画面
   - http://127.0.0.1:8000/detail/1
   - p.s
     - http://127.0.0.1:8000/detail/1　1是id编号
 - 全部データ一览画面
   - http://127.0.0.1:8000/detail
 - 添加画面
   - http://127.0.0.1:8000/matuyaindex/ 
 - 全部データ一览画面
   - http://127.0.0.1:8000/detail


#### HTML
- detail.html
  - 全てデータ一览

- getdetail.html
  - 社内通知編集
 
- getdetails.html
 - 社内通知详细
 
   
- matuyaindex.html
  - 测试用可以添加数据


#### views.py
- def
  - matuya_index
    - 对送骨保密画面
  - detail
    -  全てデータ一览画面
  - get_detail
    - 社内通知編集画面
    - p.s.
      - 与detail不同在于 右侧有编辑
      - 跳转原理: id在url后面追加 更具id查询
  - data_add
    - データ保存操作
  - data_delete
    - データ削除操作
    
#### AngularJS
- 表达式
  - {$  $}
