import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(夏祭り2026)")

# 全メンバー
all_members = [
    "しおん","そら","なるみ","まこ", "こゆ", "まあや",
    "ひまり", "ゆう", "あんな", "はるか","ともか",
    "くるみ","りえる","あやか","まひろ","みお",
    "まゆか","ほのか","みさき","れいこ","まゆこ",
    "ハルカ","ひな","あゆみ","ゆりな","あやみ","さな"
]

# 曲データ
songs = {
    "ポニーテールとシュシュ": {
        "しおん","そら","なるみ","まこ", "こゆ", "まあや",
        "れいこ","ゆう", "あんな", "はるか","さな",
        "まゆか","りえる","あやか","まひろ","みお"
    },

    "サマーとはキミと私なりっ!!": {
        "しおん","そら","なるみ","まこ", "こゆ", "まあや",
        "ひまり","ゆう", "あんな", "はるか","れいこ","ゆりな"
    },

    "ナツマトペ": {
        "まひろ","そら","なるみ","ほのか",
        "ひな", "あやみ","さな","りえる",
        "あんな", "はるか"
    },

    "Super Summer": {
        "みさき","そら","まこ", "こゆ",
        "まあや","ひまり", "ゆう",
        "あんな","ともか"
    },

    "WHAT IS LOVE?": {
        "しおん","そら","まひろ","まこ",
        "まゆか", "みさき","ハルカ",
        "あゆみ", "ともか"
    },

    "アイドルライフスターターパック": {
        "しおん", "みお", "ハルカ",
        "ゆりな", "あやみ","さな",
        "りえる", "くるみ", "ともか"
    },

    "恋愛決壊警報": {
        "はるか", "ゆう", "こゆ",
        "くるみ", "ひな", "ほのか"
    },

    "僕らのユリイカ": {
        "ひまり", "まこ", "ゆう",
        "まゆこ","まあや","ともか"
    },

    "ブルーハワイレモン": {
        "そら", "まゆこ", "ひまり",
        "れいこ", "まこ", "あんな",
        "はるか","まゆか","ともか",
        "あやか","まあや","さな"
    },

    "ぷりきゅきゅ": {
        "ひまり", "まひろ", "みさき",
        "あんな", "あゆみ", "あやか",
        "はるか", "ゆう"
    },

    "SWEET STEP": {
        "ゆりな", "あゆみ", "ひな",
        "ほのか", "はるか",
        "あんな", "ひまり"
    },

    "らぶげっちゅ": {
        "みお", "くるみ", "ゆう",
        "はるか","ひまり","あんな"
    },

    "｢君の音だったんだ｣": {
        "あやか","そら","なるみ",
        "まゆか", "こゆ", "まあや",
        "ひまり", "あんな","ゆう"
        "はるか","まゆこ","ハルカ"
    }
}

# 曲責
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
# ✅ 出席メンバー選択
# ========================

st.markdown("## ✅ 出席メンバーを選択")

# 初期化
if "selected_members" not in st.session_state:
    st.session_state.selected_members = set()

# ------------------------
# ボタン
# ------------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ 全てを選択"):

        st.session_state.selected_members = set(all_members)

        # checkbox状態も更新
        for member in all_members:
            st.session_state[f"member_{member}"] = True

with col2:
    if st.button("❌ 全て解除"):

        st.session_state.selected_members = set()

        # checkbox状態も更新
        for member in all_members:
            st.session_state[f"member_{member}"] = False

# ------------------------
# 個別チェック
# ------------------------

cols = st.columns(3)

for idx, member in enumerate(all_members):

    col = cols[idx % 3]

    checked = col.checkbox(
        member,
        key=f"member_{member}"
    )

    if checked:
        st.session_state.selected_members.add(member)
    else:
        st.session_state.selected_members.discard(member)

selected_members = st.session_state.selected_members

st.write(
    f"選択中のメンバー: "
    f"{', '.join(sorted(selected_members)) or '（未選択）'}"
)

# ========================
# 📊 出席率ランキング
# ========================

st.markdown("---")
st.markdown("## 🏆 通常曲の出席率ランキング（高い順）")

ranking = []

for song, members in songs.items():

    attending = members & selected_members

    rate = len(attending) / len(members) if members else 0

    ranking.append((
        song,
        len(attending),
        len(members),
        rate
    ))

ranking.sort(key=lambda x: x[3], reverse=True)

for song, count, total, rate in ranking:

    leader = song_leaders.get(song, "未設定")

    leader_status = (
        "出席"
        if leader in selected_members
        else "不在"
    )

    st.write(
        f"**{song}**"
        f"（曲責: {leader}（{leader_status}））"
        f"：{count} / {total}人 出席（{rate:.0%}）"
    )

# ========================
# 📋 詳細出席状況
# ========================

st.markdown("---")
st.markdown("## 📋 曲ごとの出席状況")

for song, _, _, _ in ranking:

    members = songs[song]

    attending = members & selected_members

    absent = members - selected_members

    leader = song_leaders.get(song, "未設定")

    leader_status = (
        "出席"
        if leader in selected_members
        else "不在"
    )

    st.subheader(
        f"{song}"
        f"（曲責: {leader}（{leader_status}））"
    )

    st.write(f"👥 全体人数: {len(members)}")
    st.write(f"🙋‍♀️ 出席人数: {len(attending)}")

    st.write(
        f"✅ 出席: "
        f"{'、'.join(sorted(attending)) or 'なし'}"
    )

    st.write(
        f"❌ 不在: "
        f"{'、'.join(sorted(absent)) or 'なし'}"
    )
