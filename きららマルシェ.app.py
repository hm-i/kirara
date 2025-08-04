import streamlit as st

# ==================
# 🔐 ログイン情報
# ==================
USERNAME = "Syny"
PASSWORD = "jpd"  # パスワードを変更

def check_login():
    st.title("🔐 ログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
        else:
            st.error("ユーザー名またはパスワードが違います")

# 初回は認証状態を False に
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 未認証ならログイン表示
if not st.session_state["authenticated"]:
    check_login()
    st.stop()

# ==================
# 🎵 アプリ本体
# ==================
st.title("♬ダンス練習チェッカー(まちかね・単独)")

# 全メンバー（事前入力）
all_members = ["ゆう", "まこ", "ちさと", "こゆき", "ひな", "しおん", "そら", "なるみ",  "ひまり",
               "ひじり", "まい", "ゆー", "あんな"]

# 曲とメンバーの対応表
songs = {
    "": {"", "", "", "", "", "", "", "", ""},
    "": {"ひな", "しおん", "ゆう", "まあや", "こゆ","ひじり","ありさ"},
    "": {"こゆ", "ともか", "ちさと", "しおん","ありさ"},
    "": {"しおん", "ちさと", "ともか", "はるか", "ひじり", "ゆう", "そら", "なるみ"},
    "": {"ひまり", "ちさと", "まこ", "こゆき", "まい", "はる"},
    "": {"しおん", "まこ", "こゆき"},
    "": {"まこ", "ちさと", "あんな", "ゆう", "なるみ", "そら", "ありさ"},
    "": {"まあや", "ちさと", "なるみ", "ゆう", "ひな"},
    "": {"しおん", "ともか", "ありさ", "そら", "ひな"},
    "": {"はる", "ひじり", "あんな", "ひまり", "そら", "なるみ", "ゆー", "まい"},
    "": {"はるか", "こゆき", "まい", "ゆー", "しおん", "そら", "ひまり"},
    "": {"はるか", "ひじり", "ゆう", "あんな", "ゆー", "そら", "なるみ", "ちさと", "まあや"},
}

# ----------------------
# ✅ 出席メンバー選択
# ----------------------
st.markdown("## ✅ 出席メンバーを選択")

if "selected_members" not in st.session_state:
    st.session_state.selected_members = set()

cols = st.columns(3)

for idx, member in enumerate(all_members):
    col = cols[idx % 3]
    checked = member in st.session_state.selected_members
    new_val = col.checkbox(member, value=checked, key=member)
    if new_val and not checked:
        st.session_state.selected_members.add(member)
    elif not new_val and checked:
        st.session_state.selected_members.remove(member)

selected_members = st.session_state.selected_members

st.write(f"選択中のメンバー: {', '.join(sorted(selected_members))}")


# ----------------------
# 📊 出席ランキング（上位順）
# ----------------------
ranking = []
for song, members in songs.items():
    attending = members & selected_members
    rate = len(attending) / len(members) if members else 0
    ranking.append((song, len(attending), len(members), rate))

ranking.sort(key=lambda x: x[3], reverse=True)  # 出席率でソート

st.markdown("---")
st.markdown("## 🏆 出席率ランキング（高い順）")
for song, count, total, rate in ranking:
    st.write(f"🎵 **{song}**：{count} / {total}人 出席（{rate:.0%}）")


# ----------------------
# 📋 各曲の出席状況
# ----------------------
st.markdown("---")
st.markdown("## 📋 曲ごとの出席状況")

for song, members in songs.items():
    attending = members & selected_members
    absent = members - selected_members

    st.subheader(f"🎵 {song}")
    st.write(f"👥 全体人数: {len(members)}")
    st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
    st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")

    st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")
