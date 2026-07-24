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

# 曲とメンバーの対応表（まちかねの曲・単独の曲など）
songs = {
    # ===== まちかね =====
    "言い訳Maybe【まちかね】": {"そら"},
    "絶対アイドル辞めないで【まちかね】": {"なるみ"},
    "ヘビーローテーション【まちかね】": {"しおん"},
    "Panorama【まちかね】": {"ちさと"},
    "Shining bright【まちかね】": {"まこ"},

    # ===== 単独 =====
    "言い訳Maybe【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "ともか", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり", "まひろ", "みお", "れいこ", "まき"},
    "絶対アイドル辞めないで【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まい", "まあや", "ひじり"},
    "ヘビーローテーション【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり", "まゆか", "まひろ", "みお", "みさき", "ひな", "まき", "るか"},
    "Panorama【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まい", "ひじり", "まひろ", "みお", "ゆりな"},
    "Shining bright【単独】": {"そら", "まこ", "ちさと", "ひまり", "まい", "ひじり"},
    "劇薬中毒【単独】": {"しおん", "なるみ", "ともか", "はるか", "ひじり", "あゆみ", "まゆか", "ひな", "まき", "まゆ", "るか"},
    "きゃわぱっぴんどうー【単独】": {"ちさと", "ひまり", "くるみ", "あゆみ", "まゆか", "まひろ", "さな", "ほのか", "るか"},
    "呪って呪って【単独】": {"しおん", "なるみ", "あんな", "はるか", "まい", "ひじり", "まひろ", "ほのか", "まき"},
    "沼れ！マイラバー【単独】": {"しおん", "なるみ", "あんな", "はるか", "まい", "ゆう", "こゆ", "まあや", "みお", "まゆ"},
    "Same numbers【単独】": {"そら", "まこ", "ひまり", "あんな", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり", "まひろ", "れいこ", "ゆりな"},
    "The 5th【単独】": {"なるみ", "ちさと", "あんな", "ともか", "はるか", "まい", "ゆう", "こゆ", "まあや", "あゆみ", "みお", "ひな", "ほのか", "まき"},
    "きゅんかわ人生【単独】": {"しおん", "ちさと", "ひまり", "あんな", "ともか", "はるか", "まい", "まあや", "ひじり", "まゆか", "まゆ", "ゆりな"},
    "チョコレートメランコリー【単独】": {"そら", "なるみ", "ちさと", "ひまり", "あんな", "ともか", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり", "みお"},
    "LOVEマシーン【単独】": {"そら", "しおん", "まこ", "ひまり", "あんな", "ともか", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり"},
    "アイしちゃってます♡【単独】": {"ちさと", "ひまり", "ともか", "はるか", "みお", "さな", "ほのか", "ゆりな"},
    "LIKEY【単独】": {"そら", "しおん", "まこ", "ちさと", "ひまり", "あんな", "ともか", "はるか", "まい", "まゆか", "みお"},
    "Sweetie【単独】": {"そら", "まこ", "ちさと", "あんな", "ともか", "はるか", "まい", "ゆう", "こゆ", "まあや", "ひじり", "まひろ", "ゆりな"},
    "LOOK AT ME【単独】": {"そら", "まこ", "あんな", "ともか", "はるか", "まい", "ゆう", "みお", "れいこ"},
    "sweettimer【単独】": {"そら", "しおん", "ちさと", "ひまり", "あんな", "ともか", "はるか", "ひじり", "まゆか", "みお"},
    "冬空ラプソディー【単独】": {"なるみ", "まこ", "あんな", "ともか", "はるか", "まい", "ゆう", "ひじ"},
}

# ユニット曲とメンバーの対応表
unit_songs = {
    "二人セゾン【まちかね】": {"ちさと", "ひまり"},
    "パラリラダンス【まちかね】": {"そら", "なるみ"},
    "愛して愛してあと一分【単独】": {"しおん", "あんな"},
    "ロボキス【単独】": {"しおん", "まこ"},
    "Queens【単独】": {"そら", "ちさと"},
}

song_leaders = {
    # ===== まちかね =====
    "言い訳Maybe【まちかね】": "そら",
    "絶対アイドル辞めないで【まちかね】": "なるみ",
    "ヘビーローテーション【まちかね】": "しおん",
    "Panorama【まちかね】": "ちさと",
    "Shining bright【まちかね】": "まこ",

    # ===== 単独 =====
    "言い訳Maybe【単独】": "そら",
    "絶対アイドル辞めないで【単独】": "なるみ",
    "ヘビーローテーション【単独】": "しおん",
    "Panorama【単独】": "ちさと",
    "Shining bright【単独】": "まこ",
    "劇薬中毒【単独】": "あゆみ",
    "きゃわぱっぴんどうー【単独】": "くるみ",
    "呪って呪って【単独】": "ひじり",
    "沼れ！マイラバー【単独】": "こゆ",
    "Same numbers【単独】": "こゆ",
    "The 5th【単独】": "ゆー",
    "きゅんかわ人生【単独】": "しおん",
    "チョコレートメランコリー【単独】": "ともか",
    "LOVEマシーン【単独】": "まあや",
    "アイしちゃってます♡【単独】": "ゆりな",
    "LIKEY【単独】": "まい",
    "Sweetie【単独】": "ゆりな",
    "LOOK AT ME【単独】": "れいこ",
    "sweettimer【単独】": "そら",
    "冬空ラプソディー【単独】": "ゆー",
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
show_tandoku_songs = st.checkbox("単独の曲を表示する")

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

if show_tandoku_songs:
    # ========================
    # 🏆 単独の曲の出席率ランキング
    # ========================
    st.markdown("---")
    st.markdown("## 🌸 単独の曲の出席率ランキング")
    tandoku_songs = {k: v for k, v in songs.items() if "【単独】" in k}
    tandoku_ranking = []

    for song, members in tandoku_songs.items():
        attending = members & selected_members
        rate = len(attending) / len(members) if members else 0
        tandoku_ranking.append((song, len(attending), len(members), rate))

    tandoku_ranking.sort(key=lambda x: x[3], reverse=True)

    for song, count, total, rate in tandoku_ranking:
        icon = get_song_icon(song)
        leader = song_leaders.get(song, "未設定")
        leader_status = "出席" if leader in selected_members else "不在"

        if leader == "未設定":
            st.write(f"{icon} **{song}**：{count} / {total}人 出席（{rate:.0%}）")
        else:
            st.write(f"{icon} **{song}**（曲責: {leader}（{leader_status}））：{count} / {total}人 出席（{rate:.0%}）")

    # ========================
    # 📋 単独の曲の詳細出席状況
    # ========================
    st.markdown("---")
    st.markdown("## 📋 単独の曲ごとの出席状況")

    for song, _, _, _ in tandoku_ranking:
        members = tandoku_songs[song]
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

# 単独の曲を除外
filtered_songs = {k: v for k, v in songs.items() if "【単独】" not in k}

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
