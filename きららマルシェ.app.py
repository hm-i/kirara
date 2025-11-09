import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(きららマルシェ・まちかね・単独)")

# 全メンバー（事前入力）
all_members = [
    "ゆう", "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ", "ひまり",
    "ひじり", "ちさと", "ゆー", "あんな", "まこ", "はる", "はるか", "そら", "ともか"
]

# 曲とメンバーの対応表（一般曲）
songs = {
    "ラブ♡タップ【きらら】": {"しおん", "ゆー", "ひじり", "あんな", "そら"},
    "Pixel Ribbon【きらら】": {"ひな", "なるみ", "まい", "あんな", "ひじり", "そら"},
    "マッシュ・ド・アート【きらら】": {"ひまり", "ひじり", "ちさと", "しおん"},
    "Ready!【きらら】": {"まこ", "ひまり", "あんな", "そら", "ひな"},
    "くりてぃかる♡ぷりちー【まちかね】": {"ひまり", "まい", "まこ", "ひじり", "あんな", "そら", "なるみ", "しおん", "ひな"},
    "POP IN 2【きらら】": {"ひじり", "ゆー", "ちさと"},
    "シンデレラマインド【きらら】": {"ひまり", "ちさと", "まい", "なるみ", "そら"},
    "カラコンウインク【単独】": {"ゆう", "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ", "ひまり",
                                         "ひじり", "ちさと", "ゆー", "あんな", "まこ", "はる", "はるか", "そら"},
    "とくべチュ、して【単独】": {"ちさと", "ゆう", "あんな", "そら", "まこ", "しおん", "なるみ", "はるか", "ひじり", "ひな"},
    "超最強【単独】": {"そら", "ひまり", "ひな", "あんな", "しおん", "ちさと"},
    "倍倍fight【単独】": {"そら", "ゆう", "ひまり", "ゆー", "まい", "あんな", "はるか"},
    "フライングゲット【単独】": {"ちさと", "ひじり", "ゆう", "あんな", "そら", "まこ", "しおん", "ゆー", "ともか", "なるみ"},
    "AtoZ【まちかね】": {"まい", "そら", "まあや", "まこ", "しおん", "ゆー", "ひじり"},
    "イェイェ【単独】": {"ゆー", "そら", "しおん", "こゆ", "はるか"},
    "Cherish(My love)【単独】": {"ひじり", "まい", "そら", "まこ", "こゆ"},
    "仲直りシュークリーム【単独】": {"ゆう", "あんな", "はる", "ゆー", "しおん", "まこ", "なるみ", "はるか", "ひな", "ひじり"},
    "ラブトレ【単独】": {"ひまり", "そら", "あんな", "まい", "はる", "ゆー", "ゆう", "なるみ"},
    "ネモネモ【単独】": {"ちさと", "まい", "ひじり", "そら", "まこ"},
    "恋を知った世界【単独】": {"ゆう", "ひな", "しおん", "なるみ", "まこ", "そら", "ちさと"}
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

# 曲ごとのリーダー定義
song_leaders = {
    "ラブ♡タップ【きらら】": "そら",
    "Pixel Ribbon【きらら】": "なるみ",
    "マッシュ・ド・アート【きらら】": "ひまり",
    "Ready!【きらら】": "ひな",
    "くりてぃかる♡ぷりちー【まちかね】": "しおん",
    "POP IN 2【きらら】": "ゆー",
    "シンデレラマインド【きらら】": "まい",
    "ヒロインとオオカミ【単独】": "なるみ",
    "カラコンウインク【まちかね・単独】": "ゆう",
    "とくべチュ、して【まちかね・単独】": "なるみ",
    "超最強【まちかね・単独】": "ひまり",
    "倍倍fight【まちかね・単独】": "そら",
    "フライングゲット【まちかね・単独】": "しおん",
    "Snow halation【まちかね】": "なるみ",
    "アイドルライフエクストラパック【まちかね】": "はるか",
    "AtoZ【まちかね】": "まい",
    "君とtea for two【まちかね】": "ひじり",
    "恋に恋する眠り姫【まちかね】": "あんな",
    "The feels【まちかね】": "しおん",
    "サイレントマジョリティー【まちかね】": "ちさと",
    "金曜日のおはよう【まちかね】": "ともか",
    "イェイェ【単独】": "はるか",
    "Cherish(My love)【単独】": "まい",
    "仲直りシュークリーム【単独】": "ゆー",
    "ラブトレ【単独】": "はる",
    "ネモネモ【単独】": "まこ",
    "恋を知った世界【単独】": ""
}

# ========================
# 🎨 曲アイコン関数
# ========================
def get_song_icon(song_name):
    if "【きらら】" in song_name:
        return "✨"
    elif "【まちかね・単独】" in song_name:
        return "🫧🌸"
    elif "【まちかね】" in song_name:
        return "🫧"
    elif "【単独】" in song_name:
        return "🌸"
    elif "【神戸】" in song_name:
        return "💐"
    else:
        return "🎵"

# ========================
# ✅ 出席メンバーの選択
# ========================
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
st.write(f"選択中のメンバー: {', '.join(sorted(selected_members)) or '（未選択）'}")

# ========================
# 🎛️ ユニット曲表示切り替え
# ========================
st.markdown("---")
show_unit_songs = st.checkbox("ユニット曲の出席率を表示する")
show_kirara_songs = st.checkbox("きららの曲を表示する")

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
    # 🏆 きららの曲の出席率ランキング
    # ========================
    st.markdown("---")
    st.markdown("## ✨ きららの曲の出席率ランキング")
    kirara_songs = {k: v for k, v in songs.items() if "【きらら】" in k}
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
    # 📋 きららの曲の詳細出席状況
    # ========================
    st.markdown("---")
    st.markdown("## 📋 きららの曲ごとの出席状況")

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

# きららの曲を除外
filtered_songs = {k: v for k, v in songs.items() if "【きらら】" not in k}

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
    st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")
    st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")





