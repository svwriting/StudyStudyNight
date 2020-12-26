---
title: GCP上課相關筆記
tags: 書本
---

# GCP上課相關筆記

* [1130對話機器人(3/5) - HackMD](https://hackmd.io/v_CJ5TXtSROrTfODBmf4fw)

* [1207 對話機器人(4/5) - HackMD](https://hackmd.io/PcOA_kmhStWK6Ou30HxBZw)

* [1209對話機器人(5/5) - HackMD](https://hackmd.io/zhen_4h-RouaSTN5_iSrcg)

-----
1.	11/20  
2.	11/23 
3.	11/30: GCP:創帳號 無機構 帳單預警/ Cloud Storage/cloud shell 操作
4.	12/7:  GCP：Cloud Storage/cloud shell /IAM
5.	12/9: pipencv 套件管理/ GCP：Google computer Engine



## 白話名詞
* GCP(Google Cloud Platform)
->是 Google 在雲端上提供的一組產品與服務，讓您能夠在雲端上使用與 Google 相同的技術和基礎架構，預先準備好各式服務的基本元件，讓您能夠快速上手開發及使用。

* Cloud Storage
適用於各種不同規模企業的物件儲存空間，無論有多少資料，都能存放在這個空間裡，而且沒有任何資料擷取次數或頻率的限制。

	:::spoiler
	無限儲存空間
	沒有物件大小下限
	於世界各地皆可存取，且儲存空間位置遍布全球
	低延遲
	高耐用性 (99.999999999% 的年度耐用性)
	異地備援 (如果資料儲存在多地區或雙地區)
	:::

* GCE(Google-Compute-Engine)
->Google計算引擎可使用戶按需啟動虛擬機器（VM）。虛擬機可通過標準鏡像或用戶創建的自定義鏡像啟動。

* IAM(Cloud Identity and Access Management)
->有了 Cloud Identity and Access Management (IAM)，管理員就能授權哪些使用者可以對特定資源進行操作。Cloud IAM 能為您提供完整的掌控能力與可見度，讓您能夠集中管理 Google Cloud 資源。 

* GAE(Google App Engine)
->在全代管的無伺服器平台上建構具備高擴充性的應用程式。Google應用服務引擎是一個開發、代管網路應用程式的平台，使用Google管理的資料中心。
	:::spoiler
	從零開始將應用程式擴充至全球規模，不必費心管理基礎架構
	為開發人員省去管理伺服器及設定部署作業的負擔
	支援熱門的開發語言和多項開發人員工具，進而保持靈活性
	:::

```
GCP:
   Project:無機構
	帳單預警設定
		1.Cloud Storage儲存:檔案都是object 裝載東西叫bucket
		  建立值區(建立bucket)
			1.命名：不可重複 小寫
			2.選擇資料儲存
				位置類型：單或多
				選擇位置:離自己近的
			3.儲存空間級別
			4.存取權：精細 統一（90天內可更改，90天後就固定了）
		2.GCE租機器: serivce_account
		3.IAM權限: service_account +key 最高權限者才能加東西進來
			Cloud Shell:

```



## 共筆：
* [003_2020-11-30_第三天 - Google 文件](https://docs.google.com/document/d/1x_aoT9qqXHZMRYihvlLxRRB2dcUJj-w1o8WjjbaI6wQ/edit)
* [004-2020-1207-第四天 - Google 文件](https://docs.google.com/document/d/1F7hN_VAtn-VzZeO5l1wyhhMX6ebvimyFAXVwBYcRoTw/edit)

-----

* [GCP 網站何須勞師動眾 - GAE 也能快速實踐 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10200874)