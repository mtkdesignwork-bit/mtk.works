"""BASEの出品画像（編集代行・オリジナルテーマ 各6枚）のHTMLを作る。
文章は ../base-listing-images.txt をもとにしている。
作ったあと bash render.sh で PNG にする。"""
from pathlib import Path

HERE = Path(__file__).parent
MELLOW = "file:///Users/mituki.o/Desktop/mellow/images/"

# 線のアイコン（48×48）
ICONS = {
    "palette": '<path d="M24 6a18 18 0 1 0 0 36c2.5 0 3.5-1.6 3.5-3.2 0-2.6-2.2-3.2-2.2-5.3 0-1.8 1.4-3 3.2-3H33a9 9 0 0 0 9-9C42 12.4 34 6 24 6z"/><circle cx="15" cy="21" r="2.4"/><circle cx="21" cy="14" r="2.4"/><circle cx="30" cy="14" r="2.4"/><circle cx="35" cy="21" r="2.4"/>',
    "box": '<path d="M6 15l18-9 18 9v18l-18 9-18-9z"/><path d="M6 15l18 9 18-9M24 24v18"/>',
    "tag": '<path d="M6 24V8a2 2 0 0 1 2-2h16l18 18-18 18z"/><circle cx="15" cy="15" r="3"/>',
    "truck": '<path d="M4 12h24v20H4zM28 19h8l6 7v6H28z"/><circle cx="12" cy="35" r="4"/><circle cx="34" cy="35" r="4"/>',
    "doc": '<path d="M12 4h17l9 9v31H12z"/><path d="M29 4v9h9M18 22h14M18 29h14M18 36h9"/>',
    "plug": '<rect x="6" y="6" width="15" height="15" rx="3"/><rect x="27" y="6" width="15" height="15" rx="3"/><rect x="6" y="27" width="15" height="15" rx="3"/><path d="M34.5 28v13M28 34.5h13"/>',
    "search": '<circle cx="21" cy="21" r="13"/><path d="M31 31l11 11"/>',
    "phone": '<rect x="14" y="4" width="20" height="40" rx="4"/><path d="M21 38h6"/>',
    "chat": '<path d="M6 10a4 4 0 0 1 4-4h28a4 4 0 0 1 4 4v18a4 4 0 0 1-4 4H20l-9 8v-8h-1a4 4 0 0 1-4-4z"/><path d="M15 17h18M15 23h11"/>',
    "brush": '<path d="M38 6L20 24l4 4L42 10z"/><path d="M20 24c-6 0-8 4-8 8 0 3-2 5-6 6 8 3 16 1 18-6z"/>',
    "image": '<rect x="5" y="9" width="38" height="30" rx="3"/><circle cx="16" cy="19" r="4"/><path d="M5 34l11-10 9 8 6-5 12 9"/>',
    "edit": '<path d="M10 38l3-10 20-20 7 7-20 20z"/><path d="M29 12l7 7"/>',
    "file": '<path d="M10 4h20l8 8v32H10z"/><path d="M30 4v8h8"/><path d="M17 26l5 5 9-10"/>',
    "id": '<rect x="4" y="10" width="40" height="28" rx="3"/><circle cx="16" cy="22" r="5"/><path d="M8 33c1.5-4 4.5-6 8-6s6.5 2 8 6M28 20h10M28 27h10"/>',
    "shop": '<path d="M6 18l4-10h28l4 10"/><path d="M6 18c0 3 2.5 5 6 5s6-2 6-5c0 3 2.5 5 6 5s6-2 6-5c0 3 2.5 5 6 5s6-2 6-5"/><path d="M9 23v19h30V23"/><path d="M20 42V31h8v11"/>',
    "key": '<circle cx="15" cy="24" r="8"/><path d="M23 24h19M36 24v7M42 24v5"/>',
    "lock": '<rect x="9" y="20" width="30" height="22" rx="3"/><path d="M15 20v-6a9 9 0 0 1 18 0v6M24 29v5"/>',
    "yen": '<path d="M14 6l10 15 10-15M24 21v21M15 26h18M15 33h18"/>',
    "check": '<circle cx="24" cy="24" r="18"/><path d="M15 24l6 6 12-12"/>',
    "sad": '<circle cx="24" cy="24" r="18"/><circle cx="18" cy="20" r="1.6"/><circle cx="30" cy="20" r="1.6"/><path d="M17 33c2-3 4.5-4 7-4s5 1 7 4"/>',
    "clock": '<circle cx="24" cy="24" r="18"/><path d="M24 13v12h9"/>',
    "hourglass": '<path d="M12 5h24M12 43h24M15 5c0 10 9 13 9 19s-9 9-9 19M33 5c0 10-9 13-9 19s9 9 9 19"/>',
    "copy": '<rect x="14" y="14" width="26" height="28" rx="3"/><path d="M10 34H8V6h24v4"/>',
    "megaphone": '<path d="M6 20v8h7l15 9V11l-15 9z"/><path d="M34 18c2 1.5 3 3.5 3 6s-1 4.5-3 6M13 28l3 11h5l-3-11"/>',
    "user": '<circle cx="24" cy="16" r="8"/><path d="M8 42c2-9 8-13 16-13s14 4 16 13"/>',
    "globe": '<circle cx="24" cy="24" r="18"/><path d="M6 24h36M24 6c5 5 7.5 11 7.5 18S29 37 24 42c-5-5-7.5-11-7.5-18S19 11 24 6z"/>',
    "plus": '<circle cx="24" cy="24" r="18"/><path d="M24 15v18M15 24h18"/>',
}


def icon(name, size=48, color=None):
    style = f' style="stroke:{color}"' if color else ""
    return f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 48 48"{style}>{ICONS[name]}</svg>'


def phone(x, y, w, src, scroll=0, z=1):
    """BASEテーマのプレビュー（幅390px）をスマホの枠に入れる"""
    inner = w - 28
    k = inner / 390
    h = round(844 * k)
    return (
        f'<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;z-index:{z}">'
        f'<div class="notch"></div>'
        f'<div class="screen" style="width:{inner}px;height:{h}px">'
        f'<iframe src="preview/{src}" width="390" height="{844 + scroll}" scrolling="no" '
        f'style="transform:translateY({-scroll * k}px) scale({k})"></iframe>'
        f'</div></div>'
    )


def page(name, css, body):
    html = (
        '<!doctype html>\n<html lang="ja"><head><meta charset="utf-8">'
        '<link rel="stylesheet" href="common.css">\n<style>\n' + css + '\n</style></head>\n<body>\n' + body + '\n</body></html>\n'
    )
    (HERE / f"{name}.html").write_text(html, encoding="utf-8")


TITLE_CSS = """
.top-title { position:absolute; left:0; top:140px; width:1220px; text-align:center; }
.top-title .eyebrow { display:block; margin-bottom:14px; }
"""


def top_title(eyebrow, title):
    return f'<div class="top-title"><span class="eyebrow">{eyebrow}</span><h2 class="h2">{title}</h2><div class="rule"></div></div>'


# 共通の部品：お悩みカード、できることカード、進め方の3ステップ、料金表

WORRY_CSS = """
.worries { position:absolute; left:110px; top:330px; width:1000px; display:flex; flex-direction:column; gap:26px; }
.worry { position:relative; display:flex; align-items:center; gap:28px; padding:30px 40px; font-size:31px; line-height:1.5; }
.worry:nth-child(2) { margin-left:90px; }
.worry .icon { flex:none; width:60px; height:60px; stroke:var(--ink-soft); }
.worry::after { content:""; position:absolute; left:70px; bottom:-14px; width:28px; height:28px; background:var(--card); transform:rotate(45deg); }
.arrow-down { position:absolute; left:0; width:1220px; display:flex; justify-content:center; }
.arrow-down span { display:block; width:46px; height:46px; border-right:3px solid var(--gold); border-bottom:3px solid var(--gold); transform:rotate(45deg); margin-top:-26px; }
.answer { position:absolute; left:110px; width:1000px; padding:36px 40px; text-align:center;
  background:linear-gradient(135deg, #b38d4e, #8c6630); color:#fff; border-radius:22px;
  font-family:var(--mincho); font-weight:600; font-size:40px; letter-spacing:0.06em; box-shadow:0 14px 34px rgba(120,90,50,0.25); }
"""


def worries(items):
    return '<div class="worries">' + "".join(
        f'<div class="worry card">{icon("sad")}<span>{t}</span></div>' for t in items
    ) + "</div>"


FEATURE_CSS = """
.features { position:absolute; left:70px; width:1080px; display:grid; gap:22px; }
.feature { display:flex; align-items:center; gap:22px; padding:26px 28px; }
.feature .num { flex:none; width:84px; height:84px; border-radius:50%; background:var(--bg-deep); display:flex; align-items:center; justify-content:center; }
.feature .num .icon { width:48px; height:48px; }
.feature b { display:block; font-family:var(--mincho); font-size:30px; font-weight:600; line-height:1.4; }
.feature small { display:block; margin-top:6px; font-size:21px; color:var(--ink-soft); line-height:1.5; }
.pill { position:absolute; left:0; width:1220px; display:flex; justify-content:center; }
.pill span { padding:16px 40px; border-radius:999px; border:2px solid var(--gold); color:var(--gold); background:rgba(251,248,244,0.8);
  font-family:var(--mincho); font-weight:600; font-size:30px; letter-spacing:0.06em; }
"""


def features(items):
    out = ""
    for ic, title, sub in items:
        sub_html = f"<small>{sub}</small>" if sub else ""
        out += f'<div class="feature card"><div class="num">{icon(ic)}</div><div><b>{title}</b>{sub_html}</div></div>'
    return out


STEP_CSS = """
.steps { position:absolute; left:60px; width:1100px; display:flex; align-items:stretch; }
.step { flex:1; position:relative; padding:68px 26px 34px; text-align:center; }
.step .no { position:absolute; top:-34px; left:50%; transform:translateX(-50%); width:68px; height:68px; border-radius:50%;
  background:linear-gradient(135deg, #b38d4e, #8c6630); color:#fff; font-family:var(--mincho); font-size:32px; font-weight:600;
  display:flex; align-items:center; justify-content:center; box-shadow:0 8px 18px rgba(120,90,50,0.25); }
.step .icon { width:84px; height:84px; margin:0 auto 18px; display:block; }
.step b { display:block; font-family:var(--mincho); font-weight:600; font-size:31px; line-height:1.45; }
.step small { display:block; margin-top:14px; font-size:22px; line-height:1.6; color:var(--ink-soft); }
.step-arrow { flex:none; width:44px; display:flex; align-items:center; justify-content:center; }
.step-arrow span { width:22px; height:22px; border-top:3px solid var(--gold); border-right:3px solid var(--gold); transform:rotate(45deg); }
"""


def steps(items):
    parts = []
    for i, (ic, title, sub) in enumerate(items, 1):
        sub_html = f"<small>{sub}</small>" if sub else ""
        parts.append(f'<div class="step card"><div class="no">{i}</div>{icon(ic)}<b>{title}</b>{sub_html}</div>')
    return '<div class="steps">' + '<div class="step-arrow"><span></span></div>'.join(parts) + "</div>"


PRICE_CSS = """
.price { position:absolute; left:110px; width:1000px; padding:44px 60px; text-align:center; }
.price .label { font-family:var(--mincho); font-size:30px; color:var(--ink-soft); letter-spacing:0.1em; }
.price .yen { font-family:var(--mincho); font-weight:600; font-size:110px; line-height:1.15; letter-spacing:0.02em; }
.price .yen span { font-size:46px; margin-left:6px; }
.price .chips { display:flex; justify-content:center; gap:16px; margin-top:12px; }
.price .chips span { padding:10px 26px; border-radius:999px; background:var(--mint-soft); color:#2f7d6d; font-size:24px; font-weight:600; }
.options { position:absolute; left:110px; width:1000px; padding:34px 60px; }
.options h3 { font-family:var(--mincho); font-size:30px; font-weight:600; margin-bottom:12px; display:flex; align-items:center; gap:14px; }
.options h3::before { content:""; width:8px; height:30px; background:var(--gold); border-radius:4px; }
.options li { list-style:none; display:flex; align-items:baseline; gap:14px; padding:16px 0; border-bottom:1px dashed var(--line); font-size:27px; }
.options li:last-child { border-bottom:0; }
.options li .dots { flex:1; }
.options li b { font-family:var(--mincho); font-size:32px; font-weight:600; color:var(--gold); }
.options li small { display:block; font-size:19px; color:var(--ink-soft); margin-top:4px; }
"""


def price_card(top, amount, chips):
    chip_html = "".join(f"<span>{c}</span>" for c in chips)
    return (f'<div class="price card" style="top:{top}px"><div class="label">基本料金</div>'
            f'<div class="yen">{amount}<span>円</span></div><div class="chips">{chip_html}</div></div>')


def options_card(top, extra_style=""):
    return (f'<div class="options card" style="top:{top}px;{extra_style}"><h3>オプション</h3><ul>'
            '<li><span>商品登録の追加（5件）</span><span class="dots"></span><b>＋3,000円</b></li>'
            '<li><span>修正の追加（1回）</span><span class="dots"></span><b>＋2,000円</b></li>'
            '<li><span>独自ドメインの設定<small>ドメインの購入と代金はお客様のご負担です</small></span><span class="dots"></span><b>＋3,000円</b></li>'
            '</ul></div>')


SAFE_STEPS = [
    ("id", "開設と本人確認は<br>ご自身で", "振込口座など、<br>ご本人の情報は<br>私は触りません"),
    ("shop", "作っている間も<br>ショップはそのまま", "仕上がりは<br>画面の画像で<br>ご確認いただきます"),
    ("key", "納品後に<br>パスワードを変更", "変更すれば、<br>私はログイン<br>できなくなります"),
]


# ───────── 1. 既存テーマの編集代行 ─────────

page("base-edit-1", """
.script { position:absolute; left:70px; top:140px; font-size:54px; transform:rotate(-6deg); }
.tagline { position:absolute; left:74px; top:212px; display:inline-block; padding:10px 26px; border-radius:999px;
  background:var(--ink); color:#fff; font-size:26px; letter-spacing:0.08em; }
.title { position:absolute; left:66px; top:282px; font-size:104px; line-height:1.2; }
.sub { position:absolute; left:74px; top:680px; font-size:30px; }
.badges { position:absolute; left:52px; top:860px; display:flex; gap:18px; }
.badges .badge { width:190px; height:190px; font-size:27px; }
.badges .badge svg { width:44px; height:44px; margin-bottom:6px; }
.glow { position:absolute; right:-120px; top:120px; width:760px; height:900px; border-radius:50%;
  background:radial-gradient(closest-side, rgba(255,255,255,0.75), transparent); }
.caption { position:absolute; right:60px; top:1020px; font-size:19px; color:var(--ink-soft); }
""", f"""
<div class="glow"></div>
<div class="script">BASE Shop</div>
<div class="tagline">ハンドメイド作家さん向け</div>
<h1 class="h1 title">BASE<br><span class="gold-text">ショップ、</span><br>整えます</h1>
<p class="lead sub">今のテーマで、作品の雰囲気が<br>伝わるショップに。</p>
<div class="badges">
  <div class="badge">{icon("yen")}<span>15,000円</span></div>
  <div class="badge">{icon("box")}<span>商品登録<br>5件込み</span></div>
  <div class="badge">{icon("palette")}<span>無料・有料<br>テーマOK</span></div>
</div>
{phone(670, 150, 300, "category.html", 0, 1)}
{phone(895, 400, 290, "item.html", 0, 2)}
""")

page("base-edit-2", TITLE_CSS + WORRY_CSS + """
.answer { top:930px; }
.arrow-down { top:870px; }
""", f"""
{top_title("WORRIES", "こんなお悩み、ありませんか？")}
{worries(["ショップを開いたけれど、<br>なんだか素人っぽく見える", "設定することが多くて、<br>途中で止まっている", "作品はあるのに、<br>ショップづくりに時間がとれない"])}
<div class="arrow-down"><span></span></div>
<div class="answer">作品の雰囲気が伝わるショップに整えます</div>
""")

page("base-edit-3", TITLE_CSS + FEATURE_CSS + """
.features { top:320px; grid-template-columns:1fr 1fr; }
.feature:last-child { grid-column:1 / 3; justify-self:center; width:530px; }
.pill { top:1040px; }
""", f"""
{top_title("SERVICE", "基本料金でできること")}
<div class="features">{features([
    ("palette", "テーマの設定と<br>色・文字・並び方の調整", ""),
    ("box", "商品登録 5件", "6件目からは5件ごとに＋3,000円"),
    ("truck", "カテゴリ・送料・<br>お支払い方法の設定", ""),
    ("doc", "特定商取引法・<br>プライバシーポリシー", "表記の入力（内容はお客様がご用意）"),
    ("plug", "便利な機能（Apps）の<br>追加と、検索の設定", ""),
    ("phone", "スマホでの<br>見え方の確認", ""),
    ("chat", "使い方のご説明と<br>2週間の質問対応", ""),
])}</div>
<div class="pill"><span>無料テーマ・有料テーマのどちらでもOK</span></div>
""")

page("base-edit-4-draft", TITLE_CSS + """
.sub { position:absolute; left:0; top:300px; width:1220px; text-align:center; }
.slot { position:absolute; display:flex; align-items:center; justify-content:center; text-align:center;
  border:3px dashed var(--gold-light); border-radius:24px; color:var(--gold); font-size:26px; line-height:1.6; background:rgba(251,248,244,0.6); }
""", f"""
{top_title("SAMPLE", "たとえば、こんなショップに")}
<p class="note sub">BASEの無料テーマで整えた例です</p>
<!-- テストショップで無料テーマを整えたら、下の2つの枠を画面の画像（img）に差し替える -->
<div class="slot" style="left:80px;top:380px;width:740px;height:520px">ここにPCの画面<br>（テストショップで無料テーマを整えた例）</div>
<div class="slot" style="left:860px;top:330px;width:280px;height:600px">ここに<br>スマホの画面</div>
""")

page("base-edit-5", TITLE_CSS + STEP_CSS + """
.steps { top:470px; }
.foot { position:absolute; left:110px; top:950px; width:1000px; padding:28px 36px; display:flex; align-items:center; gap:22px; font-size:24px; line-height:1.6; }
.foot .icon { flex:none; width:56px; height:56px; }
""", f"""
{top_title("FLOW", "ログイン情報を<br>預けるのが不安な方へ")}
{steps(SAFE_STEPS)}
<div class="foot card">{icon("lock")}<span>ログイン情報のやりとりは、ココナラのトークルームの中だけで行います。</span></div>
""")

page("base-edit-6", TITLE_CSS + PRICE_CSS + """
.next { position:absolute; left:110px; top:962px; width:1000px; height:150px; padding:0 40px; display:flex; align-items:center; gap:26px;
  border:2px solid var(--gold-light); border-radius:22px; background:rgba(251,248,244,0.75); }
.price { padding:30px 60px; }
.price .yen { font-size:92px; }
.options { padding:24px 60px; }
.options li { padding:12px 0; }
.next .text { flex:1; font-size:25px; line-height:1.6; color:var(--ink-soft); }
.next .text b { display:block; font-family:var(--mincho); font-size:33px; font-weight:600; color:var(--ink); }
.next .go { width:26px; height:26px; border-top:3px solid var(--gold); border-right:3px solid var(--gold); transform:rotate(45deg); margin-right:10px; }
.next .thumb { width:110px; height:130px; border-radius:16px; overflow:hidden; flex:none; }
.next .thumb iframe { border:0; transform-origin:0 0; transform:scale(0.282); }
""", f"""
{top_title("PRICE", "料金")}
{price_card(320, "15,000", ["商品登録 5件込み", "修正 2回込み"])}
{options_card(612)}
<div class="next">
  <div class="thumb"><iframe src="preview/index.html" width="390" height="487" scrolling="no"></iframe></div>
  <div class="text">デザインから作りたい方は<b>BASEのオリジナルテーマ制作へ</b></div>
  <div class="go"></div>
</div>
""")


# ───────── 2. オリジナルテーマ制作 ─────────

page("base-original-1", """
.scene { position:absolute; left:-12px; top:345px; width:1245px; height:895px;
  background:url("../ポートフォリオメロウ.png") 0 0 / 1245px auto no-repeat;
  -webkit-mask-image:linear-gradient(180deg, transparent 0, #000 90px); }
.script { position:absolute; left:70px; top:122px; font-size:56px; transform:rotate(-6deg); }
.title { position:absolute; left:70px; top:176px; font-size:66px; line-height:1.3; }
.sub { position:absolute; left:860px; top:200px; padding-left:30px; border-left:2px solid var(--ink-soft); font-size:26px; line-height:1.9; }
.badges { position:absolute; top:372px; left:0; width:1220px; display:flex; justify-content:center; gap:34px; }
.badges .badge { width:182px; height:182px; font-size:22px; }
.badges .badge svg { width:40px; height:40px; margin-bottom:4px; }
""", f"""
<div class="scene"></div>
<div class="script">Original Theme</div>
<h1 class="h1 title"><span class="gold-text">BASEっぽくない、</span><br>あなただけのショップに</h1>
<p class="lead sub">ハンドメイド作家さんの<br>BASEテーマ制作</p>
<div class="badges">
  <div class="badge">{icon("brush")}<span>デザインから<br>作ります</span></div>
  <div class="badge">{icon("yen")}<span>40,000円</span></div>
  <div class="badge">{icon("edit")}<span>写真・文章を<br>自分で変更OK</span></div>
</div>
""")

page("base-original-2", TITLE_CSS + """
.chips { position:absolute; left:70px; top:300px; width:1080px; display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
.chip { padding:16px 20px; display:flex; align-items:center; gap:14px; font-size:23px; line-height:1.5; }
.chip .icon { flex:none; width:44px; height:44px; stroke:var(--ink-soft); }
.label { position:absolute; top:448px; width:330px; text-align:center; font-family:var(--mincho); font-weight:600; font-size:28px; }
.label small { display:block; font-family:var(--gothic); font-weight:400; font-size:20px; color:var(--ink-soft); margin-top:2px; }
.mid-arrow { position:absolute; left:563px; top:730px; width:94px; height:94px; border-radius:50%;
  background:linear-gradient(135deg, #b38d4e, #8c6630); display:flex; align-items:center; justify-content:center; box-shadow:0 10px 24px rgba(120,90,50,0.3); z-index:3; }
.mid-arrow span { width:24px; height:24px; border-top:4px solid #fff; border-right:4px solid #fff; transform:rotate(45deg); margin-left:-8px; }
/* よくあるテンプレートの見本（灰色の箱で描く） */
.tpl { position:absolute; left:210px; top:525px; width:280px; height:498px; background:#1c1b1b; border-radius:46px; padding:12px; box-shadow:0 26px 50px rgba(60,40,20,0.22); }
.tpl .screen { width:100%; height:100%; background:#fff; border-radius:36px; overflow:hidden; padding:44px 16px 0; }
.tpl .bar { height:22px; width:50%; background:#d9d9d9; border-radius:4px; margin-bottom:14px; }
.tpl .hero { height:120px; background:#e6e6e6; border-radius:6px; margin-bottom:14px; }
.tpl .grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.tpl .grid div { height:96px; background:#ececec; border-radius:6px; background-size:cover; background-position:center; filter:grayscale(0.2); }
.tpl .line { height:10px; background:#e3e3e3; border-radius:4px; margin-top:8px; }
.answer { position:absolute; left:110px; top:1042px; width:1000px; padding:20px 30px; text-align:center;
  background:linear-gradient(135deg, #b38d4e, #8c6630); color:#fff; border-radius:20px;
  font-family:var(--mincho); font-weight:600; font-size:32px; letter-spacing:0.05em; }
""", f"""
{top_title("WORRIES", "こんなお悩み、ありませんか？")}
<div class="chips">
  <div class="chip card">{icon("copy")}<span>テンプレートだと、<br>どのショップも同じに見える</span></div>
  <div class="chip card">{icon("chat")}<span>作品の背景や想いまで<br>伝えたい</span></div>
  <div class="chip card">{icon("hourglass")}<span>でも、ホームページを<br>別に作るのは大変</span></div>
</div>
<div class="label" style="left:185px">よくあるテンプレート<small>写真を並べるだけ</small></div>
<div class="label" style="left:705px">オリジナルテーマ<small>作品の世界観まで伝わる</small></div>
<div class="tpl"><div class="screen">
  <div class="bar"></div><div class="hero"></div>
  <div class="grid">
    <div style="background-image:url('{MELLOW}product-bowl.jpg')"></div>
    <div style="background-image:url('{MELLOW}product-plate.jpg')"></div>
    <div style="background-image:url('{MELLOW}product-mamezara.jpg')"></div>
    <div style="background-image:url('{MELLOW}feature-stack.jpg')"></div>
  </div>
  <div class="line" style="width:80%"></div><div class="line" style="width:60%"></div>
</div></div>
<div class="mid-arrow"><span></span></div>
{phone(747, 525, 245, "index.html")}
<div class="answer">BASEのまま、作品の世界観が伝わるショップに</div>
""")

page("base-original-3", TITLE_CSS + FEATURE_CSS + """
.features { top:320px; grid-template-columns:1fr 1fr; gap:24px; }
.feature { padding:30px 30px; min-height:200px; }
.pill { top:1030px; }
""", f"""
{top_title("SERVICE", "基本料金でできること")}
<div class="features">{features([
    ("brush", "作品に合わせた<br>オリジナルデザイン", "トップ・商品一覧・商品ページ・<br>作家紹介・お問い合わせ"),
    ("phone", "スマホでもパソコンでも<br>見やすく", ""),
    ("edit", "写真や文章を<br>あとから自分で変えられる", "BASEの「デザイン」画面から"),
    ("box", "商品登録 5件<br>送料・お支払い方法の設定", "6件目からは5件ごとに＋3,000円"),
    ("search", "便利な機能（Apps）の<br>追加と、検索の設定", ""),
    ("file", "デザインの控えのお渡し<br>2週間の質問対応", ""),
])}</div>
<div class="pill"><span>ページの構成は「トップ・商品・作家紹介」の形です</span></div>
""")

page("base-original-4", TITLE_CSS + """
.sub { position:absolute; left:0; top:300px; width:1220px; text-align:center; }
.cap { position:absolute; top:1040px; width:330px; text-align:center; font-family:var(--mincho); font-weight:600; font-size:28px; }
""", f"""
{top_title("SAMPLE", "制作サンプル")}
<p class="note sub">陶芸作家の架空ブランド「mellow」</p>
{phone(75, 360, 330, "index.html")}
{phone(445, 360, 330, "item.html")}
{phone(815, 360, 330, "about.html")}
<div class="cap" style="left:75px">トップ</div>
<div class="cap" style="left:445px">商品ページ</div>
<div class="cap" style="left:815px">作家紹介</div>
""")

page("base-original-5", TITLE_CSS + """
/* BASEの「デザイン」画面の見本（実際の画面ではなく図） */
.admin { position:absolute; left:520px; top:330px; width:630px; padding:0; overflow:hidden; }
.admin .head { padding:18px 26px; background:#3b3b3b; color:#fff; font-size:22px; letter-spacing:0.08em; }
.admin .row { padding:14px 26px; border-bottom:1px solid #eee; }
.admin .row label { display:block; font-size:19px; color:var(--ink-soft); margin-bottom:8px; }
.admin .field { display:flex; align-items:center; gap:14px; }
.admin .img { width:110px; height:70px; border-radius:8px; background:url('file:///Users/mituki.o/Desktop/mellow/images/fv-photo.jpg') center/cover; }
.admin .btn { padding:8px 18px; border:1px solid #ccc; border-radius:8px; font-size:19px; color:#555; }
.admin .input { flex:1; padding:12px 16px; border:1px solid #ccc; border-radius:8px; font-size:21px; color:var(--ink); background:#fff; }
.admin .hl { outline:4px solid var(--gold); outline-offset:-4px; border-radius:8px; }
.link { position:absolute; left:440px; top:455px; width:80px; height:4px; background:var(--gold); }
.link::before { content:""; position:absolute; left:-10px; top:-8px; width:20px; height:20px; border-radius:50%; background:var(--gold); }
.list { position:absolute; left:520px; top:792px; width:630px; display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.list div { display:flex; align-items:center; gap:14px; padding:20px 22px; font-size:24px; line-height:1.4; }
.list .icon { flex:none; width:42px; height:42px; }
.foot { position:absolute; left:520px; top:1058px; width:630px; text-align:center; font-family:var(--mincho); font-weight:600; font-size:30px; color:var(--gold); }
""", f"""
{top_title("EDIT", "公開後も、自分で変えられます")}
{phone(90, 320, 340, "index.html")}
<div class="link"></div>
<div class="admin card">
  <div class="head">デザイン（BASEの管理画面）</div>
  <div class="row hl"><label>トップのメイン写真</label><div class="field"><div class="img"></div><span class="btn">画像を変更</span></div></div>
  <div class="row"><label>キャッチコピー</label><div class="field"><span class="input">今日をまるく、やわらかく。</span></div></div>
  <div class="row"><label>お知らせ</label><div class="field"><span class="input">新作のマグを12月に発売します</span></div></div>
</div>
<div class="list">
  <div class="card">{icon("image")}<span>トップの写真と<br>キャッチコピー</span></div>
  <div class="card">{icon("megaphone")}<span>お知らせ</span></div>
  <div class="card">{icon("user")}<span>作家紹介の<br>写真と文章</span></div>
  <div class="card">{icon("plus")}<span>商品の追加</span></div>
</div>
<div class="foot">BASEの「デザイン」画面から、いつでも</div>
""")

page("base-original-6", TITLE_CSS + STEP_CSS + PRICE_CSS + """
.top-title { top:128px; }
.steps { top:330px; transform:scale(0.86); transform-origin:50% 0; }
.step { padding:60px 20px 26px; }
.price { display:flex; align-items:center; justify-content:center; gap:36px; padding:26px 50px; }
.price .yen { font-size:86px; }
.price .chips { flex-direction:column; margin-top:0; gap:10px; }
.options { padding:22px 60px; }
.options li { padding:11px 0; font-size:25px; }
""", f"""
{top_title("FLOW &amp; PRICE", "進め方と料金")}
{steps(SAFE_STEPS)}
{price_card(690, "40,000", ["商品登録 5件込み", "修正 3回込み"])}
<div class="options card" style="top:885px;padding-top:14px;padding-bottom:10px"><ul>
  <li><span>商品登録の追加（5件）</span><span class="dots"></span><b>＋3,000円</b></li>
  <li><span>修正の追加（1回）</span><span class="dots"></span><b>＋2,000円</b></li>
  <li><span>独自ドメインの設定（ドメイン代はお客様）</span><span class="dots"></span><b>＋3,000円</b></li>
</ul></div>
""")



# ───────── 3. 静的サイト（1ページのブランドサイト）─────────
# 文章は ../lp-listing-images.txt。1枚目は lp-eyecatch.html（手で組んだもの）

def phone_img(x, y, w, src):
    """スクリーンショット（1170×2532）をスマホの枠に入れる"""
    inner = w - 28
    h = round(inner * 2532 / 1170)
    return (f'<div class="phone" style="left:{x}px;top:{y}px;width:{w}px">'
            f'<div class="notch"></div><div class="screen" style="width:{inner}px;height:{h}px">'
            f'<img src="../{src}" style="width:100%;display:block"></div></div>')


page("lp-2", TITLE_CSS + WORRY_CSS + """
.worries { top:320px; gap:22px; }
.worry { padding:24px 40px; font-size:29px; }
.arrow-down { top:830px; }
.answer { top:862px; font-size:33px; padding:28px 20px; letter-spacing:0.03em; }
.who { position:absolute; left:0; top:1032px; width:1220px; display:flex; justify-content:center; gap:14px; }
.who span { padding:10px 24px; border-radius:999px; background:rgba(251,248,244,0.9); border:1px solid var(--line); font-size:23px; color:var(--ink-soft); }
""", f"""
{top_title("WORRIES", "こんなお悩み、ありませんか？")}
{worries(["Instagramだけだと投稿が流れてしまい、<br>作品の魅力が伝わりにくい", "BASEやminneにショップはあるけれど、<br>見てもらうだけで購入につながらない", "ホームページはほしいけれど、<br>毎月の費用や管理が不安"])}
<div class="arrow-down"><span></span></div>
<div class="answer">作品の魅力を伝えて、ショップへつなぐサイトを作ります</div>
<div class="who"><span>ハンドメイド作家さん</span><span>小さなブランド</span></div>
""")

page("lp-compare", TITLE_CSS + """
.h2 { font-size:50px; }
.cols { position:absolute; left:90px; top:320px; width:1040px; display:grid; grid-template-columns:1.08fr 1fr; gap:24px; align-items:start; }
.col { padding:30px 34px 22px; }
.col h3 { font-family:var(--mincho); font-weight:600; font-size:32px; text-align:center; padding-bottom:18px; border-bottom:1px solid var(--line); }
.col li { list-style:none; display:flex; align-items:center; gap:16px; min-height:96px; padding:12px 0; border-bottom:1px dashed var(--line); font-size:26px; line-height:1.45; }
.col li:last-child { border-bottom:0; }
.col li .icon { flex:none; width:40px; height:40px; }
.col.us { box-shadow:inset 0 0 0 3px var(--gold); }
.col.us h3 { color:var(--gold); }
.col.us li { font-weight:600; }
.col.wp li { color:var(--ink-soft); }
.col.wp li .icon { stroke:var(--ink-soft); }
.answer { position:absolute; left:90px; top:872px; width:1040px; padding:26px 20px; text-align:center;
  background:linear-gradient(135deg, #b38d4e, #8c6630); color:#fff; border-radius:22px;
  font-family:var(--mincho); font-weight:600; font-size:32px; line-height:1.5; letter-spacing:0.03em; box-shadow:0 14px 34px rgba(120,90,50,0.25); }
.sub-note { position:absolute; left:0; top:1042px; width:1220px; text-align:center; font-size:22px; color:var(--ink-soft); }
""", f"""
{top_title("COMPARE", "そのサイト、WordPressが必要ですか？")}
<div class="cols">
  <div class="col card us"><h3>1ページのホームページ</h3><ul>
    <li>{icon("yen")}<span>毎月の保守費用 0円</span></li>
    <li>{icon("check")}<span>システムの更新なし</span></li>
    <li>{icon("megaphone")}<span>お知らせはInstagramで</span></li>
    <li>{icon("chat")}<span>変更は必要なときだけ依頼</span></li>
  </ul></div>
  <div class="col card wp"><h3>WordPressのサイト</h3><ul>
    <li>{icon("yen")}<span>サーバー代 月1,000円前後</span></li>
    <li>{icon("plug")}<span>システムの更新が必要</span></li>
    <li>{icon("edit")}<span>自分で更新できる</span></li>
    <li>{icon("copy")}<span>ページを増やしやすい</span></li>
  </ul></div>
</div>
<div class="answer">魅力を伝えてショップへつなぐ1ページなら、<br>シンプルな形で十分です</div>
<p class="sub-note">サイトの住所（ドメイン）の代金は、どちらも別にかかります</p>
""")

page("lp-3", TITLE_CSS + FEATURE_CSS + """
.features { top:320px; grid-template-columns:1fr 1fr; gap:20px; }
.feature { padding:22px 26px; min-height:170px; }
""", f"""
{top_title("SERVICE", "基本料金でできること")}
<div class="features">{features([
    ("doc", "ページの順番<br>（構成）を考える", "購入に進みやすい順番に"),
    ("brush", "オリジナルの<br>デザイン", "ブランドの色や雰囲気に合わせて"),
    ("phone", "スマホでもパソコンでも<br>見やすく", ""),
    ("edit", "キャッチコピーや<br>紹介文を一緒に整える", "箇条書きのメモからでOK"),
    ("shop", "ショップへのボタンを<br>購入に進みやすい位置に", "SNS、お問い合わせへのボタンも"),
    ("search", "検索やSNSで<br>シェアされたときの表示", ""),
    ("globe", "インターネットに<br>公開するまでの設定", ""),
    ("check", "修正 3回まで", ""),
])}</div>
""")

page("lp-4", TITLE_CSS + """
.sub { position:absolute; left:0; top:300px; width:1220px; text-align:center; }
.cap { position:absolute; top:985px; width:300px; text-align:center; font-family:var(--mincho); font-weight:600; font-size:28px; line-height:1.3; }
.cap small { display:block; font-family:var(--gothic); font-weight:400; font-size:20px; color:var(--ink-soft); margin-top:4px; }
""", f"""
{top_title("SAMPLE", "制作サンプル")}
<p class="note sub">架空のブランドで作ったサイトです</p>
{phone(110, 350, 300, "nail-1.html")}
{phone_img(460, 350, 300, "mellow_sp.png")}
{phone_img(810, 350, 300, "nagi_sp.png")}
<div class="cap" style="left:110px">QUIET QUIRK<small>ネイルチップ作家</small></div>
<div class="cap" style="left:460px">mellow<small>陶芸作家</small></div>
<div class="cap" style="left:810px">NAGI<small>宿泊施設</small></div>
""")

page("lp-5", TITLE_CSS + STEP_CSS + """
.steps { top:330px; left:110px; width:1000px; display:grid; grid-template-columns:1fr 1fr; gap:56px 30px; }
.step { padding:56px 24px 26px; }
.step .icon { width:64px; height:64px; margin-bottom:12px; }
.step b { font-size:29px; }
.step small { margin-top:10px; font-size:21px; }
.foot { position:absolute; left:110px; top:975px; width:1000px; padding:24px 34px; display:flex; align-items:center; gap:22px; font-size:23px; line-height:1.6; }
.foot .icon { flex:none; width:52px; height:52px; }
.foot b { color:var(--gold); }
""", f"""
{top_title("DELIVERY", "サイトは、あなたのものです")}
<div class="steps">
  <div class="step card"><div class="no">1</div>{icon("user")}<b>アカウントと住所は<br>お客様のお名前で</b><small>取引が終わっても、そのまま使えます</small></div>
  <div class="step card"><div class="no">2</div>{icon("key")}<b>ログイン情報は<br>制作中だけお預かり</b><small>トークルームの中でやりとりします</small></div>
  <div class="step card"><div class="no">3</div>{icon("lock")}<b>納品後に<br>パスワードを変更</b><small>私はログインできなくなります</small></div>
  <div class="step card"><div class="no">4</div>{icon("edit")}<b>公開後の変更は<br>必要なときだけご依頼</b><small>1回1,000円〜、月額料金なし</small></div>
</div>
<div class="foot card">{icon("yen")}<span>かかる費用は、サイトの住所の代金<b>（年1,500〜2,000円ほど）</b>。<br>サイトを置く場所（Cloudflare）は現在無料です。</span></div>
""")

page("lp-6", TITLE_CSS + PRICE_CSS + """
.price { display:flex; align-items:center; justify-content:center; gap:36px; padding:30px 50px; }
.price .chips { flex-direction:column; margin-top:0; gap:10px; }
.flow { position:absolute; left:110px; top:820px; width:1000px; padding:30px 40px; }
.flow h3 { font-family:var(--mincho); font-size:30px; font-weight:600; margin-bottom:22px; display:flex; align-items:center; gap:14px; }
.flow h3::before { content:""; width:8px; height:30px; background:var(--gold); border-radius:4px; }
.flow ol { list-style:none; display:flex; align-items:flex-start; justify-content:space-between; }
.flow li { display:flex; flex-direction:column; align-items:center; gap:8px; font-size:20px; text-align:center; line-height:1.4; width:120px; }
.flow li i { width:44px; height:44px; border-radius:50%; background:var(--bg-deep); color:var(--gold); font-style:normal; font-family:var(--mincho); font-weight:600; font-size:22px; display:flex; align-items:center; justify-content:center; }
.flow .sep { width:16px; height:16px; border-top:2px solid var(--gold-light); border-right:2px solid var(--gold-light); transform:rotate(45deg); margin-top:14px; }
""", f"""
{top_title("PRICE &amp; FLOW", "料金と流れ")}
{price_card(320, "30,000", ["1ページ", "修正 3回込み"])}
<div class="options card" style="top:540px;padding-top:24px;padding-bottom:16px"><h3>オプション</h3><ul>
  <li><span>ページの追加（1ページ）</span><span class="dots"></span><b>＋8,000円</b></li>
  <li><span>制作中の修正の追加（1回）</span><span class="dots"></span><b>＋2,000円</b></li>
</ul></div>
<div class="flow card"><h3>制作の流れ</h3><ol>
  <li><i>1</i>ご相談<br>（無料）</li><span class="sep"></span>
  <li><i>2</i>質問<br>シート</li><span class="sep"></span>
  <li><i>3</i>ページの<br>順番</li><span class="sep"></span>
  <li><i>4</i>デザイン<br>制作</li><span class="sep"></span>
  <li><i>5</i>ご確認<br>修正</li><span class="sep"></span>
  <li><i>6</i>公開<br>納品</li>
</ol></div>
""")



# ───────── 4. WordPressのサイト制作 ─────────
# 文章は ../wp-listing-images.txt

page("wp-1", """
.scene { position:absolute; left:-12px; top:345px; width:1245px; height:895px;
  background:url("../ポートフォリオ凪.png") 0 0 / 1245px auto no-repeat;
  -webkit-mask-image:linear-gradient(180deg, transparent 0, #000 170px); }
.script { position:absolute; left:70px; top:122px; font-size:56px; transform:rotate(-6deg); }
.title { position:absolute; left:70px; top:180px; font-size:60px; line-height:1.32; }
.sub { position:absolute; left:860px; top:200px; padding-left:30px; border-left:2px solid var(--ink-soft); font-size:26px; line-height:1.9; }
.badges { position:absolute; top:372px; left:0; width:1220px; display:flex; justify-content:center; gap:34px; }
.badges .badge { width:182px; height:182px; font-size:22px; }
.badges .badge svg { width:40px; height:40px; margin-bottom:4px; }
""", f"""
<div class="scene"></div>
<div class="script">WordPress</div>
<h1 class="h1 title"><span class="gold-text">世界観が伝わる、</span><br>自分で更新できるサイトに</h1>
<p class="lead sub">個人で活動する方の<br>WordPressサイト制作</p>
<div class="badges">
  <div class="badge">{icon("yen")}<span>50,000円</span></div>
  <div class="badge">{icon("doc")}<span>トップ＋<br>3ページ</span></div>
  <div class="badge">{icon("edit")}<span>自分で更新<br>OK</span></div>
</div>
""")

page("wp-2", TITLE_CSS + WORRY_CSS + """
.answer { top:930px; font-size:31px; padding:36px 16px; letter-spacing:0.03em; }
.arrow-down { top:870px; }
""", f"""
{top_title("WORRIES", "こんなお悩み、ありませんか？")}
{worries(["お知らせや作品を、<br>自分で更新できるサイトがほしい", "SNSだけでなく、<br>検索からも見つけてもらいたい", "テンプレートのままだと、<br>自分らしさが出ない"])}
<div class="arrow-down"><span></span></div>
<div class="answer">世界観はそのままに、自分で更新できるサイトを作ります</div>
""")

page("wp-3", TITLE_CSS + FEATURE_CSS + """
.features { top:320px; grid-template-columns:1fr 1fr; gap:20px; }
.feature { padding:22px 26px; min-height:170px; }
""", f"""
{top_title("SERVICE", "基本料金でできること")}
<div class="features">{features([
    ("doc", "トップ＋下層3ページ", "例：プロフィール、作品紹介など"),
    ("brush", "オリジナルの<br>デザイン", "あなたの色や雰囲気に合わせて"),
    ("megaphone", "お知らせ（ブログ）の<br>機能", ""),
    ("chat", "お問い合わせ<br>フォーム", ""),
    ("phone", "スマホでもパソコンでも<br>見やすく", ""),
    ("plug", "WordPressの設置と<br>初期設定、SSL", ""),
    ("lock", "検索・セキュリティ・<br>バックアップの設定", ""),
    ("file", "操作マニュアルと、<br>納品後1か月の質問対応", ""),
])}</div>
""")

page("wp-4", TITLE_CSS + """
.sub { position:absolute; left:0; top:300px; width:1220px; text-align:center; }
.cap { position:absolute; top:985px; width:300px; text-align:center; font-family:var(--mincho); font-weight:600; font-size:28px; }
""", f"""
{top_title("SAMPLE", "制作サンプル")}
<p class="note sub">架空の宿ブランド「NAGI」をWordPressのオリジナルテーマにしました</p>
{phone(110, 350, 300, "nagi-top.html")}
{phone(460, 350, 300, "nagi-stays.html")}
{phone(810, 350, 300, "nagi-news.html")}
<div class="cap" style="left:110px">トップ</div>
<div class="cap" style="left:460px">宿の一覧</div>
<div class="cap" style="left:810px">お知らせ</div>
""")

page("wp-5", TITLE_CSS + """
/* WordPressの投稿画面の見本（実際の画面ではなく図） */
.admin { position:absolute; left:520px; top:330px; width:630px; padding:0; overflow:hidden; }
.admin .head { padding:18px 26px; background:#23282d; color:#fff; font-size:22px; letter-spacing:0.08em; }
.admin .row { padding:14px 26px; border-bottom:1px solid #eee; }
.admin .row label { display:block; font-size:19px; color:var(--ink-soft); margin-bottom:8px; }
.admin .input { display:block; padding:12px 16px; border:1px solid #ccc; border-radius:8px; font-size:21px; color:var(--ink); background:#fff; }
.admin .area { height:90px; line-height:1.6; }
.admin .btnrow { padding:14px 26px; text-align:right; }
.admin .pub { display:inline-block; padding:10px 28px; border-radius:8px; background:var(--gold); color:#fff; font-size:21px; }
.link { position:absolute; left:440px; top:455px; width:80px; height:4px; background:var(--gold); }
.link::before { content:""; position:absolute; left:-10px; top:-8px; width:20px; height:20px; border-radius:50%; background:var(--gold); }
.list { position:absolute; left:520px; top:775px; width:630px; display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.list div { display:flex; align-items:center; gap:14px; padding:18px 22px; font-size:24px; }
.list .icon { flex:none; width:42px; height:42px; }
.cost { position:absolute; left:520px; top:955px; width:630px; padding:20px 26px; font-size:21px; line-height:1.7; border:2px solid var(--gold-light); border-radius:18px; background:rgba(251,248,244,0.75); }
.cost b { font-family:var(--mincho); font-size:24px; color:var(--gold); display:block; }
""", f"""
{top_title("EDIT", "公開後も、自分で更新できます")}
{phone(90, 320, 340, "nagi-news.html")}
<div class="link"></div>
<div class="admin card">
  <div class="head">新規投稿（WordPressの管理画面）</div>
  <div class="row"><label>タイトル</label><span class="input">新作のお知らせ</span></div>
  <div class="row"><label>本文</label><span class="input area">12月に新しい作品を発売します。</span></div>
  <div class="btnrow"><span class="pub">公開</span></div>
</div>
<div class="list">
  <div class="card">{icon("megaphone")}<span>お知らせの投稿</span></div>
  <div class="card">{icon("edit")}<span>文章の変更</span></div>
  <div class="card">{icon("image")}<span>写真の変更</span></div>
  <div class="card">{icon("plus")}<span>記事の追加</span></div>
</div>
<div class="cost"><b>かかる費用</b>サーバー代 月1,000円前後<br>ドメイン代 年1,500〜2,000円ほど</div>
""")

page("wp-6", TITLE_CSS + STEP_CSS + PRICE_CSS + """
.top-title { top:128px; }
.steps { top:330px; transform:scale(0.86); transform-origin:50% 0; }
.step { padding:60px 20px 26px; }
.price { display:flex; align-items:center; justify-content:center; gap:36px; padding:26px 50px; }
.price .yen { font-size:86px; }
.price .chips { flex-direction:column; margin-top:0; gap:10px; }
.options li { padding:11px 0; font-size:25px; }
""", f"""
{top_title("FLOW &amp; PRICE", "進め方と料金")}
{steps([
    ("user", "ご契約は<br>お客様のお名前で", "サーバーとドメインは<br>取引のあとも<br>そのまま使えます"),
    ("key", "ログイン情報は<br>制作中だけお預かり", "やりとりは<br>トークルームの<br>中だけで行います"),
    ("lock", "納品後に<br>パスワードを変更", "変更すれば、<br>私はログイン<br>できなくなります"),
])}
{price_card(690, "50,000", ["トップ＋3ページ", "修正 3回込み"])}
<div class="options card" style="top:885px;padding-top:18px;padding-bottom:14px"><ul>
  <li><span>ページの追加（1ページ）</span><span class="dots"></span><b>＋8,000円</b></li>
  <li><span>修正の追加（1回）</span><span class="dots"></span><b>＋2,000円</b></li>
</ul></div>
""")



# ───────── 5. WordPressの月額保守 ─────────
# 文章は ../wp-maintenance-images.txt

page("maint-1", """
.scene { position:absolute; left:-12px; top:345px; width:1245px; height:895px;
  background:url("../ポートフォリオ凪.png") 0 0 / 1245px auto no-repeat;
  -webkit-mask-image:linear-gradient(180deg, transparent 0, #000 170px); }
.script { position:absolute; left:70px; top:122px; font-size:56px; transform:rotate(-6deg); }
.title { position:absolute; left:70px; top:180px; font-size:64px; line-height:1.32; }
.badges { position:absolute; top:372px; left:0; width:1220px; display:flex; justify-content:center; gap:34px; }
.badges .badge { width:182px; height:182px; font-size:22px; }
.badges .badge svg { width:40px; height:40px; margin-bottom:4px; }
""", f"""
<div class="scene"></div>
<div class="script">Maintenance</div>
<h1 class="h1 title"><span class="gold-text">作ったあとも、安心を。</span><br>WordPressの月額保守</h1>
<div class="badges">
  <div class="badge">{icon("yen")}<span>月額<br>3,500円</span></div>
  <div class="badge">{icon("lock")}<span>更新・<br>バックアップ</span></div>
  <div class="badge">{icon("edit")}<span>月1回の<br>修正つき</span></div>
</div>
""")

page("maint-2", TITLE_CSS + WORRY_CSS + """
.answer { top:930px; font-size:34px; padding:36px 16px; letter-spacing:0.03em; }
.arrow-down { top:870px; }
""", f"""
{top_title("WORRIES", "こんなお悩み、ありませんか？")}
{worries(["更新の通知が出ているけれど、<br>押すのが怖い", "エラーでサイトが見られなくなったら<br>どうしよう", "文章や写真を少し直したいときに、<br>気軽に頼みたい"])}
<div class="arrow-down"><span></span></div>
<div class="answer">更新とバックアップを、毎月おまかせください</div>
""")

page("maint-3", TITLE_CSS + STEP_CSS + FEATURE_CSS + """
.cycle { position:absolute; left:70px; top:330px; width:1080px; display:flex; align-items:stretch; }
.cycle .item { flex:1; padding:64px 10px 26px; text-align:center; position:relative; }
.cycle .no { position:absolute; top:-30px; left:50%; transform:translateX(-50%); width:60px; height:60px; border-radius:50%;
  background:linear-gradient(135deg, #b38d4e, #8c6630); color:#fff; font-family:var(--mincho); font-size:28px; font-weight:600;
  display:flex; align-items:center; justify-content:center; }
.cycle .icon { width:66px; height:66px; display:block; margin:0 auto 12px; }
.cycle b { display:block; font-family:var(--mincho); font-weight:600; font-size:27px; line-height:1.4; }
.cycle .sep { flex:none; width:36px; display:flex; align-items:center; justify-content:center; }
.cycle .sep span { width:18px; height:18px; border-top:3px solid var(--gold); border-right:3px solid var(--gold); transform:rotate(45deg); }
.again { position:absolute; left:0; top:605px; width:1220px; text-align:center; font-family:var(--mincho); font-size:27px; color:var(--gold); font-weight:600; letter-spacing:0.08em; }
.features { top:670px; grid-template-columns:1fr; left:210px; width:800px; gap:16px; }
.feature { padding:18px 26px; }
.feature .num { width:70px; height:70px; }
.feature .num .icon { width:40px; height:40px; }
""", f"""
{top_title("MONTHLY", "毎月やること")}
<div class="cycle">
  <div class="item card"><div class="no">1</div>{icon("copy")}<b>バックアップ</b></div>
  <div class="sep"><span></span></div>
  <div class="item card"><div class="no">2</div>{icon("plug")}<b>本体・テーマ・<br>プラグインの更新</b></div>
  <div class="sep"><span></span></div>
  <div class="item card"><div class="no">3</div>{icon("phone")}<b>表示の確認</b></div>
  <div class="sep"><span></span></div>
  <div class="item card"><div class="no">4</div>{icon("doc")}<b>作業のご報告</b></div>
</div>
<div class="again">この流れを、毎月くり返します</div>
<div class="features">{features([
    ("chat", "お問い合わせフォームの動作の確認", ""),
    ("edit", "かんたんな修正 月1回", "文章や写真の差し替え1〜2か所"),
    ("user", "使い方のご質問", "トークルームで受付"),
])}</div>
""")

page("maint-4", TITLE_CSS + PRICE_CSS + """
.price { display:flex; align-items:center; justify-content:center; gap:30px; padding:30px 40px; }
.price .label { white-space:nowrap; }
.safe-list { position:absolute; left:110px; top:560px; width:1000px; display:flex; flex-direction:column; gap:18px; }
.safe-item { display:flex; align-items:center; gap:24px; padding:24px 34px; }
.safe-item .icon { flex:none; width:60px; height:60px; }
.safe-item b { display:block; font-family:var(--mincho); font-size:29px; font-weight:600; line-height:1.4; }
.safe-item small { display:block; margin-top:4px; font-size:22px; color:var(--ink-soft); line-height:1.5; }
""", f"""
{top_title("PRICE", "料金と安心の仕組み")}
<div class="price card" style="top:320px"><div class="label">月額</div><div class="yen">3,500<span>円</span></div><div class="chips" style="flex-direction:column;margin-top:0"><span>定期購入</span></div></div>
<div class="safe-list">
  <div class="safe-item card">{icon("key")}<div><b>お客様のパスワードはお預かりしません</b><small>保守用のアカウントを作って作業します</small></div></div>
  <div class="safe-item card">{icon("check")}<div><b>解約は定期購入を止めるだけ</b><small>サイトはそのまま残ります</small></div></div>
  <div class="safe-item card">{icon("file")}<div><b>私が制作したWordPressサイトが対象です</b><small>サイトの作りがわかっているので、更新で不具合が出ても直せます</small></div></div>
</div>
""")

print("ok")
