import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(夏祭り2026)")

# 全メンバー（事前入力）
all_members = [
    "そら","まあや","りえる","しおん", "ひじり","みお","なるみ",
    "ともか", "みさき", "まこ","あやみ","くるみ","ちさと","あゆみ",
    "まひろ","ひまり","まゆか","ほのか","あんな","れいこ","まゆ",
    "はるか","ひな","あやか","ゆう","ゆりな","さな","こゆき","るか", "まき","まい"
]

# 曲とメンバーの対応表（まちかねの曲・単独の曲など）

songs = {
    # ===== まちかね =====
    "言い訳Maybe【まちかね】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まい", "ゆう", "こゆき", "まあや", "ひじり", "まひろ", "みお", "れいこ"},
    "絶対アイドル辞めないで【まちかね】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まあや", "ひじり"},
    "ヘビーローテーション【まちかね】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "まい", "ゆう", "こゆき", "まあや", "ひじり", "まひろ", "みお", "みさき", "ひな", "るか", "あやみ"},
    "Panorama【まちかね】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな","まい", "ひじり", "まひろ", "みお", "ゆりな"},
    "Shining bright【まちかね】": {"そら", "まこ", "ちさと", "ひまり","あんな", "ゆう", "ひじり"},
    "♡♡♡わんだーらんど【まちかね】": {"しおん", "くるみ", "ほのか", "まゆ"},
    "今、恋をしている【まちかね】": {"なるみ", "ひまり", "あんな", "はるか", "まい", "ゆう", "こゆき", "まあや", "ひじり", "みお", "まゆ", "あやか"},
    "君セン！【まちかね】": {"ゆう", "まゆか", "さな", "みさき", "ほのか", "まき", "るか", "りえる", "あやか"},
    "ゆめみるプリマドンナ【まちかね】": {"あんな", "はるか", "まあや", "あゆみ", "さな", "まき", "ゆりな", "あやか"},
    "キュートなキューたい【まちかね】": {"しおん", "ちさと", "ひまり", "ゆう", "あゆみ", "さな", "ゆりな", "あやか"},
    "I♡シズム【まちかね】": {"そら", "しおん", "ひまり", "まあや","あんな", "くるみ", "ほのか"},
    "AI SEE CHAT【まちかね】": {"ちさと", "まゆか", "みお", "ひな"},
    "BRAVE GROOVE【まちかね】": {"そら", "しおん", "あんな", "まあや", "ひじり", "まひろ", "くるみ", "ゆりな", "あやみ"},
    "CHEER UP【まちかね】": {"まこ", "ちさと", "しおん", "あゆみ",  "まひろ", "くるみ", "みお", "れいこ", "るか"},
    "初恋のこたえ。【まちかね】": {"なるみ", "まこ", "ちさと", "あんな", "はるか", "まい", "れいこ", "ほのか", "まゆ"},
    "のびしろグリッター【まちかね】": {"そら", "しおん", "なるみ", "あんな","はるか", "まい","ひじり"},
    "BANG BANG【まちかね】": {"そら", "ちさと", "ひまり", "まい", "まひろ", "ゆりな"},
    "チュープリ【まちかね】": {"しおん", "はるか", "ゆう", "こゆき", "まあや", "りえる"},
    "世界でいちばんアイドル【まちかね】": {"なるみ", "あんな", "はるか", "ゆう", "こゆき", "まひろ"},

    # ===== 尼涼祭 =====
    "きにしないっ！【尼涼祭】": {"まあや", "はるか", "こゆき", "ゆう", "まこ", "まい", "ひじり", "ひまり", "そら"},
    "サマーリボン【尼涼祭】": {"ゆう", "はるか", "こゆき", "まい", "あんな", "まこ", "ひまり"},
    "夏恋ジレンマ【尼涼祭】": {"あんな", "まあや", "まこ", "ひじり"},
    "生まれたトキから白歴史【尼涼祭】": {"あんな", "くるみ", "まい", "はるか", "ひまり"},
    "ゼリーの海で背泳ぎ眩しいや【尼涼祭】": {"まこ", "まあや", "こゆき", "ひじり", "そら"},
    "Kiss&Bite Me!【尼涼祭】": {"あんな", "くるみ", "しおん", "ゆう", "そら", "ひじり", "ひまり"},
    "いちご完全犯罪【尼涼祭】": {"くるみ", "しおん", "こゆき", "そら"},

    # ===== 単独 =====
    "言い訳Maybe【単独】": {"しおん","ひまり","まこ", "ひじり","みお","なるみ",
    "ともか", "そら","くるみ","ちさと","あゆみ",
    "まひろ","まあや","まゆか","ほのか","あんな","れいこ","まゆ",
    "はるか","ひな","あやか","ゆう","ゆりな","さな","こゆき","るか", "まき","まい"},
    "絶対アイドル辞めないで【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな", "はるか", "まあや", "ひじり"},
    "ヘビーローテーション【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり", "あんな","ともか", "はるか", "まい", "ゆう", "こゆき", "まあや", "ひじり",
                       "あやか","まゆ", "まひろ", "みお", "ひな", "るか"},
    "Panorama【単独】": {"そら", "しおん", "なるみ", "まこ", "ちさと", "ひまり","あんな", "まい", "ひじり", "まひろ", "みお", "ゆりな"},
    "Shining bright【単独】": {"そら", "まこ", "ちさと", "ひまり", "あんな","ゆう", "ひじり"},
    "劇薬中毒【単独】": {"しおん", "なるみ", "ともか", "あゆみ", "まい","まゆか", "ひな", "まき", "まゆ", "るか"},
    "きゃわぽっぴんどうー【単独】": {"ちさと", "あゆみ","まゆか","まひろ", "くるみ", "さな", "ほのか", "るか","あやか"},
    "呪って呪って【単独】": {"しおん", "なるみ", "ちさと","ともか", "はるか","まい", "ひじり", "まひろ", "ほのか", "まき"},
    "沼れ！マイラバー【単独】": {"しおん", "なるみ", "ともか", "はるか", "まい", "ゆう", "こゆき", "くるみ", "まゆ"},
    "Same numbers【単独】": {"そら", "まこ","ひまり", "あんな","ともか", "はるか", "まい", "ゆう", "こゆき", "まあや", "ひじり", "まゆか","あやか","れいこ", "まひろ", "ゆりな"},
    "The 5th【単独】": {"なるみ", "ちさと", "あんな", "はるか", "まゆか", "ゆう", "まあや", "みお", "さな", "ひな", "まき"},
    "きゅんかわ人生【単独】": {"しおん", "なるみ", "ひまり", "あんな", "ともか","はるか", "まい", "こゆき", "まあや", "まゆ", "るか","あやか"},
    "チョコレートメランコリー【単独】": {"そら", "なるみ","ひまり", "ともか", "あんな", "はるか", "まい", "ゆう", "まあや", "ひじり", "くるみ"},
    "LOVEマシーン【単独】": {"そら", "しおん", "まこ","ひまり", "あんな",  "ともか", "はるか", "まい", "ゆう", "こゆき", "まあや","ひじり", "あゆみ", 
                     "あやか", "くるみ", "れいこ", "まき"},
    "アイしちゃってます♡【単独】": {"ちさと", "ひまり", "はるか", "れいこ", "さな", "ほのか", "ゆりな"},
    "LIKEY【単独】": {"そら", "しおん", "まこ", "ちさと", "ひまり", "ともか", "くるみ", "まい", "あゆみ"},
    "Sweetie/ME:I【単独】": {"そら", "まこ", "ひまり", "ともか","はるか", "まい", "まあや", "ひじり", "まひろ", "ゆりな"},
    "LOOK AT ME【単独】": {"そら", "まこ", "ともか", "まい", "ゆう","こゆき","まあや", "くるみ", "れいこ"},
    "sweettimer【単独】": {"そら", "しおん", "なるみ", "ともか", "あんな", "はるか", "ひじり", "あやか", "みお"},
    "冬空ラプソディー【単独】": {"なるみ", "まこ", "あんな", "はるか", "まい", "ゆう", "ひじり"},
}

# ユニット曲とメンバーの対応表
unit_songs = {
    "二人セゾン【まちかね】": {"ちさと", "ひまり"},
    "パラリラダンス【まちかね】": {"そら", "なるみ"},
    "愛して愛してあと一分【単独】": {"しおん", "ともか"},
    "ロボキス【単独】": {"しおん", "まこ"},
    "Queens【単独】": {"そら", "ひまり"}
}

song_leaders = {
    # ===== まちかね =====
    "言い訳Maybe【まちかね】": "そら",
    "絶対アイドル辞めないで【まちかね】": "なるみ",
    "ヘビーローテーション【まちかね】": "しおん",
    "Panorama【まちかね】": "ちさと",
    "Shining bright【まちかね】": "まこ",
    "♡♡♡わんだーらんど【まちかね】": "ほのか",
    "今、恋をしている【まちかね】": "あんな",
    "君セン！【まちかね】": "さな",
    "ゆめみるプリマドンナ【まちかね】": "あやか",
    "キュートなキューたい【まちかね】": "あやか",
    "I♡シズム【まちかね】": "ひまり",
    "AI SEE CHAT【まちかね】": "まゆか",
    "BRAVE GROOVE【まちかね】": "くるみ",
    "CHEER UP【まちかね】": "まこ",
    "初恋のこたえ。【まちかね】": "なるみ",
    "のびしろグリッター【まちかね】": "はるか",
    "BANG BANG【まちかね】": "ひまり",
    "チュープリ【まちかね】": "しおん",
    "世界でいちばんアイドル【まちかね】": "なるみ",

    # ===== 尼涼祭 =====
    "きにしないっ！【尼涼祭】": "そら",
    "サマーリボン【尼涼祭】": "あんな",
    "夏恋ジレンマ【尼涼祭】": "ひじり",
    "生まれたトキから白歴史【尼涼祭】": "まい",
    "ゼリーの海で背泳ぎ眩しいや【尼涼祭】": "まこ",
    "Kiss&Bite Me!【尼涼祭】": "くるみ",
    "いちご完全犯罪【尼涼祭】": "しおん",

    # ===== 単独 =====
    "劇薬中毒【単独】": "あゆみ",
    "きゃわぱっぴんどうー【単独】": "くるみ",
    "呪って呪って【単独】": "ひじり",
    "沼れ！マイラバー【単独】": "こゆ",
    "Same numbers【単独】": "こゆ",
    "The 5th【単独】": "ゆう",
    "きゅんかわ人生【単独】": "しおん",
    "チョコレートメランコリー【単独】": "ともか",
    "LOVEマシーン【単独】": "まあや",
    "アイしちゃってます♡【単独】": "ゆりな",
    "LIKEY【単独】": "まい",
    "Sweetie【単独】": "ゆりな",
    "LOOK AT ME【単独】": "れいこ",
    "sweettimer【単独】": "そら",
    "冬空ラプソディー【単独】": "ゆう",
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
show_amaryosai_songs = st.checkbox("尼涼祭の曲を表示する")

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

if show_amaryosai_songs:
    # ========================
    # 🏆 尼涼祭の曲の出席率ランキング
    # ========================
    st.markdown("---")
    st.markdown("## 🍂 尼涼祭の曲の出席率ランキング")
    amaryosai_songs = {k: v for k, v in songs.items() if "【尼涼祭】" in k}
    amaryosai_ranking = []

    for song, members in amaryosai_songs.items():
        attending = members & selected_members
        rate = len(attending) / len(members) if members else 0
        amaryosai_ranking.append((song, len(attending), len(members), rate))

    amaryosai_ranking.sort(key=lambda x: x[3], reverse=True)

    for song, count, total, rate in amaryosai_ranking:
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

    for song, _, _, _ in amaryosai_ranking:
        members = amaryosai_songs[song]
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
