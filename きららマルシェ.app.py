import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(夏祭り2026)")

# 全メンバー（事前入力）
all_members = [
    "しおん","そら","なるみ","まこ", "こゆ", "まあや","ひまり",
    "ゆー", "あんな", "はるか","ともか","くるみ","りえる","あやか","まひろ","みお","まゆか","ほのか","みさき","れいこ","まゆこ",
    "ハルカ","ひな","あゆみ","ゆりな","あやみ","さな"
]

# 曲とメンバーの対応表（一般曲）
songs = {
    "ラブ♡タップ【尼涼祭】": {"まこ", "ゆー", "ひじり", "あんな", "そら"},
    "Pixel Ribbon【尼涼祭】": {"ちさと", "なるみ", "まい", "あんな", "ひじり", "そら"},
    "マッシュ・ド・アート【尼涼祭】": {"ひまり", "ひじり", "ちさと", "あんな"},
    "POP IN 2【尼涼祭】": {"ひじり", "ゆー", "ちさと"},
    "シンデレラマインド【尼涼祭】": {"ひまり", "ちさと", "まい", "なるみ", "そら"},
    "What Is Love?【まちかね】": {"しおん", "まい", "まあや", "なるみ", "ひまり",
                            "ちさと", "ゆー", "まこ", "ともか"},
    "ラブソングに襲われる【まちかね】": {"ちさと", "ともか", "あんな", "そら", "まこ", "しおん", "なるみ", "まあや", "ひじり", "ひな"},
    "バチモリーナ【まちかね】": {"はるか", "ひじり", "ひな", "あんな", "しおん", "ちさと","なるみ","まあや","ともか"},
    "ブルーハワイレモン【まちかね】": {"そら", "こゆ", "ひまり", "ゆー", "まこ", "あんな", "はるか","ひじり","ともか","なるみ","まあや","ひな"},
    "超特急逃走中【まちかね】": {"ちさと", "ひじり", "まい", "あんな", "そら", "ひな", "こゆ", "ゆー", "ともか", "なるみ"},
    "盛れミ・アモーレ【まちかね】": {"ともか", "そら", "ゆー", "まこ", "しおん", "あんな", "ひまり"},
    "かわいいメモリアル【まちかね】": {"ゆー", "ひな", "なるみ", "こゆ", "ひじり","ちさと"},
    "都営大江戸線の六本木駅で抱きしめて【まちかね】": {"ともか", "なるみ", "まあや", "ひな"},
    "special spell【まちかね】": {"はるか", "そら", "しおん", "ちさと"},
    "キスミ―パティシエ【まちかね】": {"ひまり", "そら", "あんな", "まい", "はるか", "ちさと", "ひな"},
    "ラブコード【まちかね】": {"まあや", "はるか", "ひじり", "そら", "あんな","ともか","なるみ"},
    "キューにストップできません！【まちかね】": {"ゆー", "はるか", "まい", "ひまり", "あんな", "そら", "ちさと","ひじり"},
    "はちゃめちゃわちゃライフ！【まちかね】": {"ゆー","まい", "なるみ", "ひまり","ちさと", "あんな", "はるか", },
    "feel my rhythm【まちかね】": {"しおん", "まあや","ひまり", "まこ",  "ともか"},
    "アザトカワイイ【単独】": {"しおん", "ひな", "こゆ", "まあや", "なるみ","ひじり", "ちさと", "ゆー", "あんな", "まこ",  "ともか", "そら"},
    "パレオはエメラルド【単独】": {"ひな", "まあや", "なるみ", "ゆー",  "まこ", "ともか", "そら"},
    "ひたむきシンデレラ【単独】": { "まい","なるみ", "ひまり","ちさと", "ゆー", "あんな", "はるか", "ともか"},
    "レべチかわいい！【単独】": {"しおん", "まい", "ひまり","ひじり", "ゆー", "あんな", "そら"},
    "シャウトシャトル【単独】": {"しおん","まあや", "なるみ", "あんな","ひじり", "はるか", "そら"},
    "バカデカボイスで好きって叫べ【単独】": { "しおん", "ひな",  "なるみ",  "ひじり", "あんな", "はるか", "そら"},
    "キュンとクラフト【単独】": {"まい", "まあや", "なるみ", "ひじり", "ちさと", "ともか", "あんな", "はるか", "そら"},
    "君とたこやきLove恋め【単独】": { "しおん", "ひまり","ゆー", "ともか", "はるか", "そら","ひな"}, 
    "ラストノートしか知らない【単独】": {"まあや", "なるみ", "ひまり","ひじり", "ちさと", "ゆー", "あんな", "まこ", "ともか", "はるか"},
    "ピーチティーとピーチパイ【単独】": { "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ", "ひまり", "ひじり", "ゆー", "あんな","はるか", "そら"},
    "ちゅららんレーサー【単独】": {"しおん", "まい", "ひな", "ひまり", "あんな", "まこ", "はるか", "そら"}, 
    "君ラブ【単独】": { "まい", "ひな", "ひまり","あんな","ともか", "はるか"}, 
    "botばっか【単独】": {"こゆ", "ゆー", "あんな", "ともか"},
    "yes or yes【単独】": {"しおん", "まい", "まあや", "ひまり","ちさと", "ゆー","まこ", "ともか", "そら"},
    "MUSE【単独】": { "しおん", "まい", "まあや", "ひまり", "ひじり","まこ", "ともか"},
    "カルテNO.2222【単独】": {"こゆ", "なるみ","あんな", "はるか"},
    "Accendio【単独】": { "しおん", "まい", "まあや", "ひまり","ちさと","ともか"},
    "queencard【単独】": {"しおん", "まあや", "ちさと", "まこ", "そら"},
    "veryveryvery【単独】": {"まい","こゆ", "ちさと", "ゆー",  "まこ", "ともか", "そら"},
}

# ユニット曲とメンバーの対応表
unit_songs = {
    "ウィンブルドンへ連れて行って【単独】": {"ゆう", "しおん", "ひな"},
    "愛♡スクリ～ム【単独】": {"しおん", "なるみ", "そら"},
    "Kawaii Kaiwai【単独】": {"はる", "ひまり"},
    "シス×ラブ【単独】": {"ゆう", "まこ"},
    "＋もしもしダーリン♡【単独】": {"ひな", "しおん"},
    "鼓動【単独】": {"ひまり", "ちさと"},
    "まさかのconfession【単独】": {"ゆう", "ひな"}
}

song_leaders = {
    # ===== 尼涼祭 =====
    "ラブ♡タップ【尼涼祭】": "そら",
    "Pixel Ribbon【尼涼祭】": "なるみ",
    "マッシュ・ド・アート【尼涼祭】": "ひまり",
    "POP IN 2【尼涼祭】": "ゆー",
    "シンデレラマインド【尼涼祭】": "まい",

    # ===== まちかね =====
    "What Is Love?【まちかね】": "ちさと",
    "ラブソングに襲われる【まちかね】": "そら",
    "バチモリーナ【まちかね】": "はるか",
    "ブルーハワイレモン【まちかね】": "あんな",
    "超特急逃走中【まちかね】": "ひじり",
    "盛れミ・アモーレ【まちかね】": "ともか",
    "かわいいメモリアル【まちかね】": "ひな",
    "都営大江戸線の六本木駅で抱きしめて【まちかね】": "ひな",
    "special spell【まちかね】": "そら",
    "キスミ―パティシエ【まちかね】": "まい",
    "ラブコード【まちかね】": "なるみ",
    "キューにストップできません！【まちかね】": "ひまり",
    "はちゃめちゃわちゃライフ！【まちかね】": "ひまり",
    "feel my rhythm【まちかね】": "しおん",

    # ===== 単独 =====
    "アザトカワイイ【単独】": "ひな",
    "パレオはエメラルド【単独】": "まあや",
    "ひたむきシンデレラ【単独】": "ゆー",
    "レべチかわいい！【単独】": "ひまり",
    "シャウトシャトル【単独】": "そら",
    "バカデカボイスで好きって叫べ【単独】": "はるか",
    "キュンとクラフト【単独】": "ひじり",
    "君とたこやきLove恋め【単独】": "ゆー",
    "ラストノートしか知らない【単独】": "なるみ",
    "ピーチティーとピーチパイ【単独】": "あんな",
    "ちゅららんレーサー【単独】": "しおん",
    "君ラブ【単独】": "あんな",
    "botばっか【単独】": "しおん",
    "yes or yes【単独】": "まい",
    "MUSE【単独】": "まい",
    "カルテNO.2222【単独】": "こゆ",
    "Accendio【単独】": "ちさと",
    "queencard【単独】": "しおん",
    "veryveryvery【単独】": "まこ",
}


# ========================
# 🎨 曲アイコン関数
# ========================
def get_song_icon(song_name):
    if "【尼涼祭】" in song_name:
        return "✨"
    elif "【まちかね】" in song_name:
        return "🍂"
    elif "【単独】" in song_name:
        return "🌸"
    else:
        return "🎵"

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
# 🎛️ ユニット曲表示切り替え
# ========================
st.markdown("---")
show_unit_songs = st.checkbox("ユニット曲の出席率を表示する")
show_kirara_songs = st.checkbox("尼涼祭の曲を表示する")

# ========================
# 📊 出席率ランキング表示
# ========================
if show_unit_songs:
    # ========================
    # 🏆 ユニット曲の出席率ランキング
    # ========================
    st.markdown("## 🏆 ユニット曲の出席率ランキング")
    unit_ranking = []

    for song, members in unit_songs.items():
        attending = members & selected_members
        rate = len(attending) / len(members) if members else 0
        unit_ranking.append((song, len(attending), len(members), rate))

    unit_ranking.sort(key=lambda x: x[3], reverse=True)

    for song, count, total, rate in unit_ranking:
        icon = get_song_icon(song)
        st.write(f"{icon} **{song}**：{count} / {total}人 出席（{rate:.0%}）")

    # ========================
    # 📋 ユニット曲の詳細出席状況
    # ========================
    st.markdown("---")
    st.markdown("## 📋 ユニット曲ごとの出席状況")

    for song, _, _, _ in unit_ranking:
        members = unit_songs[song]
        attending = members & selected_members
        absent = members - selected_members
        icon = get_song_icon(song)

        st.subheader(f"{icon} {song}")
        st.write(f"👥 全体人数: {len(members)}")
        st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
        st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")
        st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")

if show_kirara_songs:
    # ========================
    # 🏆 尼涼祭の曲の出席率ランキング
    # ========================
    st.markdown("---")
    st.markdown("## ✨ 尼涼祭の曲の出席率ランキング")
    kirara_songs = {k: v for k, v in songs.items() if "【尼涼祭】" in k}
    kirara_ranking = []

    for song, members in kirara_songs.items():
        attending = members & selected_members
        rate = len(attending) / len(members) if members else 0
        kirara_ranking.append((song, len(attending), len(members), rate))

    kirara_ranking.sort(key=lambda x: x[3], reverse=True)

    for song, count, total, rate in kirara_ranking:
        icon = get_song_icon(song)
        leader = song_leaders.get(song, "未設定")
        leader_status = "出席" if leader in selected_members else "不在"

        if leader == "未設定":
            st.write(f"{icon} **{song}**：{count} / {total}人 出席（{rate:.0%}）")
        else:
            st.write(f"{icon} **{song}**（曲責: {leader}（{leader_status}））：{count} / {total}人 出席（{rate:.0%}）")

    # ========================
    # 📋 尼涼祭の曲の詳細出席状況
    # ========================
    st.markdown("---")
    st.markdown("## 📋 尼涼祭の曲ごとの出席状況")

    for song, _, _, _ in kirara_ranking:
        members = kirara_songs[song]
        attending = members & selected_members
        absent = members - selected_members
        leader = song_leaders.get(song, "未設定")
        leader_status = "出席" if leader in selected_members else "不在"
        icon = get_song_icon(song)

        if leader == "未設定":
            st.subheader(f"{icon} {song}")
        else:
            st.subheader(f"{icon} {song}（曲責: {leader}（{leader_status}））")

        st.write(f"👥 全体人数: {len(members)}")
        st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
        st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")
        st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")

# ========================
# 📊 通常曲の出席率ランキング
# ========================
st.markdown("---")
st.markdown("## 🏆 通常曲の出席率ランキング（高い順）")
ranking = []

# 尼涼祭の曲を除外
filtered_songs = {k: v for k, v in songs.items() if "【尼涼祭】" not in k}

for song, members in filtered_songs.items():
    attending = members & selected_members
    rate = len(attending) / len(members) if members else 0
    ranking.append((song, len(attending), len(members), rate))

ranking.sort(key=lambda x: x[3], reverse=True)

for song, count, total, rate in ranking:
    icon = get_song_icon(song)
    leader = song_leaders.get(song, "未設定")
    leader_status = "出席" if leader in selected_members else "不在"

    if leader == "未設定":
        st.write(f"{icon} **{song}**：{count} / {total}人 出席（{rate:.0%}）")
    else:
        st.write(f"{icon} **{song}**（曲責: {leader}（{leader_status}））：{count} / {total}人 出席（{rate:.0%}）")

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
    icon = get_song_icon(song)

    if leader == "未設定":
        st.subheader(f"{icon} {song}")
    else:
        st.subheader(f"{icon} {song}（曲責: {leader}（{leader_status}））")

    st.write(f"👥 全体人数: {len(members)}")
    st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
    st.write(f"✅ 出席: {'、'.join(sorted(attending))or 'なし'}")
    st.write(f"❌ 不在: {'、'.join(sorted(absent))or 'なし'}")
