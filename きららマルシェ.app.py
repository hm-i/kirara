import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(夏祭り2026)")

# 全メンバー（事前入力）
all_members = [
    "しおん","そら","なるみ","まこ", "こゆ", "まあや","ひまり", "ゆう", "あんな", "はるか","ともか","くるみ","りえる","あやか","まひろ","みお","まゆか","ほのか","みさき","れいこ","まゆこ",
    "ハルカ","ひな","あゆみ","ゆりな","あやみ","さな"
]

# 曲とメンバーの対応表（一般曲）
songs = {
    "ポニーテールとシュシュ": {"しおん","そら","なるみ","まこ", "こゆ", "まあや","れいこ","ゆう", "あんな", "はるか","さな","まゆか","りえる","あやか","まひろ","みお"},
    "サマーとはキミと私なりっ!!": {"しおん","そら","なるみ","まこ", "こゆ", "まあや","ひまり","ゆう", "あんな", "はるか","れいこ","ゆりな"},
    "ナツマトペ": {"まひろ","そら","なるみ","ほのか", "ひな", "あやみ","さな","りえる", "あんな", "はるか"},
    "Super Summer": {"みさき","そら","まこ", "こゆ", "まあや","ひまり", "ゆう", "あんな","ともか"},
    "WHAT IS LOVE?": {"しおん","そら","まひろ","まこ", "まゆか", "みさき","ハルカ", "あゆみ", "ともか"},
    "アイドルライフスターターパック": {"しおん", "みお", "ハルカ", "ゆりな", "あやみ",
                                         "さな", "りえる", "くるみ", "ともか"},
    "恋愛決壊警報": {"はるか", "ゆう", "こゆき", "くるみ", "ひな", "ほのか"},
    "僕らのユリイカ": { "ひまり", "まこ", "ゆう","まゆこ","まあや","ともか"},
    "ブルーハワイレモン": {"そら", "まゆこ", "ひまり", "れいこ", "まこ", "あんな", "はるか","まゆか","ともか","あやか","まあや","さな"},
    "ぷりきゅきゅ": {"ひまり", "まひろ", "みさき", "あんな", "あゆみ", "あやか", "はるか", "ゆう"},
    "SWEET STEP": {"ゆりな", "あゆみ", "ひな", "ほのか", "はるか", "あんな", "ひまり"},
    "らぶげっちゅ": {"ゆー", "みお", "くるみ", "ゆう", "はるか","ひまり","あんな"},
    "｢君の音だったんだ｣": {"あやか","そら","なるみ","まゆか", "こゆ", "まあや","ひまり", "ゆー", "あんな", "はるか","まゆこ","ハルカ"}
}

song_leaders = {
    "ポニーテールとシュシュ": "そら",
    "サマーとはキミと私なりっ!!": "しおん",
    "ナツマトペ": "なるみ",
    "Super Summer": "まこ",
    "WHAT IS LOVE?": "まこ",
    "アイドルライフスターターパック": "ともか",
    "恋愛決壊警報": "こゆ",
    "僕らのユリイカ": "まあや",
    "ブルーハワイレモン": "あんな",
    "ぷりきゅきゅ": "ひまり",
    "SWEET STEP": "ひまり",
    "らぶげっちゅ": "はるか",
    "｢君の音だったんだ｣":"ゆう"
}


# ========================
# ✅ 出席メンバーの選択
# ========================
st.markdown("## ✅ 出席メンバーを選択")

if "selected_members" not in st.session_state:
    st.session_state.selected_members = set()

# ------------------------
# 全選択ボタン
# ------------------------
if st.button("✅ 全てを選択"):
    st.session_state.selected_members = set(all_members)

# （任意）全解除ボタン
if st.button("❌ 全て解除"):
    st.session_state.selected_members = set()

# ------------------------
# 個別チェック
# ------------------------
cols = st.columns(3)

new_selected = set()

for idx, member in enumerate(all_members):
    col = cols[idx % 3]

    checked = member in st.session_state.selected_members

    val = col.checkbox(
        member,
        value=checked,
        key=f"member_{member}"
    )

    if val:
        new_selected.add(member)

# 状態更新
st.session_state.selected_members = new_selected

selected_members = st.session_state.selected_members

st.write(
    f"選択中のメンバー: {', '.join(sorted(selected_members)) or '（未選択）'}"
)

# ========================
# 📊 出席率ランキング表示
# ========================



# ========================
# 📊 通常曲の出席率ランキング
# ========================
st.markdown("---")
st.markdown("## 🏆 通常曲の出席率ランキング（高い順）")
ranking = []

# きららの曲を除外
filtered_songs = {k: v for k, v in songs.items() if "【スイパラ】" not in k}

for song, members in filtered_songs.items():
    attending = members & selected_members
    rate = len(attending) / len(members) if members else 0
    ranking.append((song, len(attending), len(members), rate))

ranking.sort(key=lambda x: x[3], reverse=True)

for song, count, total, rate in ranking:
    leader = song_leaders.get(song, "未設定")
    leader_status = "出席" if leader in selected_members else "不在"

    if leader == "未設定":
        st.write(f" **{song}**：{count} / {total}人 出席（{rate:.0%}）")
    else:
        st.write(f"**{song}**（曲責: {leader}（{leader_status}））：{count} / {total}人 出席（{rate:.0%}）")

# ========================
# 📋 通常曲の詳細出席状況
# ========================
st.markdown("---")
st.markdown("## 📋 曲ごとの出席状況（出席率順）")

for song, _, _, _ in ranking:
    members = filtered_songs[song]
    attending = members & selected_members
    absent = members - selected_members
    leader = song_leaders.get(song, "未設定")
    leader_status = "出席" if leader in selected_members else "不在"

    if leader == "未設定":
        st.subheader(f" {song}")
    else:
        st.subheader(f" {song}（曲責: {leader}（{leader_status}））")

    st.write(f"👥 全体人数: {len(members)}")
    st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
    st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")
    st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")











