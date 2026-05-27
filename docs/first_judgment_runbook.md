# 第一条判断 · 单日执行清单

> 唯一目标:今天选 1 家公司,跑完四条证据线,往 `judgment_tracker.csv` 填进**第一条**带证据链和锁死阈值的预登记判断。
> 一家就好。不是三家,不是十五家。过了这一条,项目才算出生。

预计总耗时:**约 5–6 小时**(含掐表测 LinkedIn 那条线的真实成本)。可拆成上午/下午两段。

---

## 规矩(开工前读一遍,贴在屏幕边上)

- **今天不优化任何模板、不编 watchlist、不加文件。** 只跑一家、填一条。任何"先把 X 完善一下"的念头都是拖延的伪装。
- 选出的方向哪怕是 `TBD / Stable` 也算成功 —— 重点是**走完流程 + 锁死一个可证伪标准**,不是逼出一个戏剧性结论。
- 判断没把握就降置信度,**不要为了好看而拔高**。低置信的诚实判断 > 高置信的硬凑。

---

## 第 0 步 · 选这一家(20 分钟)

不要纠结。从默认 15 家里按这三条快速挑:

1. **你最熟的那家**(降低学习成本,第一次跑流程别给自己加难度)。
2. **最近 12 个月有明显事件**的(换帅 / 重组 / 大裁员 / 高调扩张)—— 有波动才有拐点可抓,全程平静的公司第一次跑没意思。
3. **财报会 transcript 好找**的(大盘 SaaS 基本都有)。

> 选定就**写下来,不许反悔**。选择本身不值得花一小时。

---

## 第 1 步 · 证据线三:管理层语言(45 分钟)

**先做这条,因为它最干净、零合规风险、最容易建立手感。**

- 找最近 **2–3 次**财报电话会 transcript(Seeking Alpha / Motley Fool / 公司 IR 页免费版)。
- 如果常规入口被 403 / JS 动态加载挡住,不要立刻判定"没有 transcript"。按这个 fallback 顺序试:
  1. 搜索公司 IR 直链:`site:<IR domain> transcript <company> <quarter> <year> pdf`。有些 IR 页会把 PDF 放在 `encrypt/files/...` 这类深层路径,页面抓不到但搜索索引能暴露直链。
  2. 试静态 transcript 镜像源,优先 `TickerTrends`、`Alpha Spread`、`StockAnalysis`。这些页面对普通 HTTP 客户端通常比 Seeking Alpha / Investing / Yahoo 更友好。
  3. 记录"访问失败"本身,但只作为 source availability note,不要把它当成项目不可做的结论。
- TSMC / TSMC ADR (`TSM`) 的 2026Q1 已验证可用入口:
  - 官方事件页: `https://investor.tsmc.com/english/quarterly-results/teleconference`
  - 官方 PDF 直链可被搜索索引打开,但本机 `Invoke-WebRequest` 可能 403:`https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/3cef85204275f94fd111485cfdf4adb3c0263c45/TSMC%201Q26%20Transcript.pdf`
  - 可脚本访问镜像:`https://tickertrends.io/transcripts/TSM/Q1-earnings-transcript-2026`
  - 可脚本访问镜像:`https://www.alphaspread.com/security/twse/2330/investor-relations/earnings-call/q1-2026`
- 只读两样:
  1. 用词重心有没有从"增长 / 扩张"**转向**"效率 / 纪律 / 聚焦"?(或反过来)
  2. 面对分析师尖锐提问(尤其关于人员、流失、竞争),是正面回答还是回避?
- 记到卡模板的「管理层语言」那条:Signal 五选一 + What changed + Why it matters + transcript 链接。

---

## 第 2 步 · 证据线二:员工评价趋势(45 分钟)

- 打开 Glassdoor(可补 Comparably / Indeed)。
- **不看当前分数,看走向**:综合分近几季的曲线,尤其"对管理层信心""业务前景"两个分项 + CEO 认可度。
- 翻最近 **20–30 条**评价,记高频词有没有漂移(如从"使命感"→"重组/不确定",或反向)。
- 记到卡模板的「员工评价趋势」那条。

---

## 第 3 步 · 证据线一:关键人才流向(掐表!预算 90 分钟,到点就停)

> **这是今天最重要的实验。** 不只是为了这家公司,是为了测出这条线的**真实时间成本** —— 这个数字会重新定义你到底能覆盖几家。

- 开个计时器。**手工**看 LinkedIn(自动抓取对 LinkedIn 行不通,别试)。
- 这一家具体追踪哪些岗位 —— 边查边记下来,这就是你 watchlist 的第一行,**让它从真实需求里长出来**:
  - VP 及以上、Staff/Principal 级工程、核心产品负责人、关键业务线 leader。
  - 谁来了、谁走了、走去了哪(尤其去竞品)、入职/离职大概时间。
- 高管离职**单独记**,和普通员工流动分开。
- 把 LinkedIn 当**方向性样本**,不是普查 —— 别追求完整,追求"够不够支撑一个方向判断"。
- **90 分钟一到就停**,记下:
  - 实际看了几家岗位、几个人?
  - 信号够不够清楚?
  - **这家花了 X 分钟 → 推算你一周手工盯得过来几家**(这个数字今天必须得出来)。
- 记到卡模板的「关键人才流向」那条。

---

## 第 4 步 · 证据线四:红旗 / 外部(20 分钟)

- 这条最轻。Google News 搜:公司名 + lawsuit / layoff / SEC / investigation。
- 顺手把这家的 **Google Alert** 设上(对应 `google_alert_queries.csv`)。
- 多数情况记"无 / 轻微"即可。出大事才细看。
- 记到卡模板的「红旗 / 外部」那条。

---

## 第 5 步 · 下方向结论 + 锁死可证伪标准(40 分钟)⭐ 核心

四条线汇总后,填卡模板顶部和 Falsifiable Record 块:

- **方向**:Improving / Stable / Deteriorating / Mixed —— 拿不准就 Stable 或 Mixed,**不强凑**。
- **一句话判断**:点出"数字还没反应、但 X 在变"这种领先信号(如果有)。
- **置信度**:低 / 中 / 高 —— 第一次,诚实点,多半是"中"或"低"。
- **难度标签**:显而易见 / 有争议 / 反共识(防只下安全注用)。
- **锁死这五个字段(发出即不可改):**

| 字段 | 要求 | 例 |
|---|---|---|
| Primary Metric | **唯一一个**客观指标,禁止"A 或 B 或 C" | 下季 Glassdoor "业务前景"分项 |
| Threshold | 一个明确数值 | 跌破 50% |
| Deadline | 一个明确日期 | 至 2026 Q3 财报 |
| Difficulty | 上面的难度标签 | 有争议 |
| Status | 此刻一律 `Open` | Open |

> **结案规则提醒**:用运营/基本面事件结案,**别用股价**(踩投顾线 + 噪音大)。方向对但时机晚于 deadline = 失手。

---

## 第 6 步 · 填进 tracker,填上那行空白(15 分钟)🎯

把上面的内容写进 `judgment_tracker.csv` 的第二行。14 列对应填:

```
Judgment ID  → 001
Publish Date → 今天
Company / Ticker → 你选的那家
Direction / Confidence / Difficulty → 上一步定的
Primary Metric / Threshold / Deadline → 上一步锁死的
Status → Open
Resolution Date / Outcome Notes → 留空(到期才填)
Source Links → 四条线的链接
```

> **这一行被填上的瞬间,CultureRadar 才真正开始。** 在此之前,脚手架做得再完整,项目都还在起跑线前。

---

## 收工自检(5 分钟)

- [ ] tracker.csv 第二行不再是空的
- [ ] 这条判断有唯一主指标 + 阈值 + 截止日 + 来源 + 时间戳(五要素齐)
- [ ] 没用任何 buy/sell/hold/目标价措辞
- [ ] 记下了 LinkedIn 这条线的**真实耗时**和**可覆盖家数推算**
- [ ] watchlist 第一行(这家的关键岗位)在跑的过程中自然记下来了

全勾 → 今天成功。明天再选第二家,或先消化。**不要今天就想着扩到 15 家。**

---

## 一句话

> 今天不需要新增任何文件、功能、脚本。从 0 到 1 只需要你坐下来,花几小时,把第一条真实判断填进那行空白。那一刻之前,一切都是准备;那一刻之后,项目开始呼吸。
