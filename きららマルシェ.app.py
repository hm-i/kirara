import streamlit as st

# =====================
# 🎵 アプリ本体
# =====================

st.title("♬ダンス練習チェッカー(スイパラ・サーオリ・いちょう祭)")

# 全メンバー（事前入力）
all_members = [
    "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ", "ひまり",
    "ひじり", "ちさと", "ゆー", "あんな", "まこ", "はる", "はるか", "そら", "ともか"
]

# 曲とメンバーの対応表（一般曲）
songs = {
    "ラブ♡タップ【スイパラ】": {"しおん", "ゆー", "ひじり", "あんな", "そら"},
    "Pixel Ribbon【スイパラ】": {"ひな", "なるみ", "まい", "あんな", "ひじり", "そら"},
    "マッシュ・ド・アート【スイパラ】": {"ひまり", "ひじり", "ちさと", "しおん"},
    "POP IN 2【スイパラ】": {"ひじり", "ゆー", "ちさと"},
    "シンデレラマインド【スイパラ】": {"ひまり", "ちさと", "まい", "なるみ", "そら"},
    "What Is Love?【サーオリ】": {"しおん", "まい", "まあや", "なるみ", "ひまり",
                                         "ちさと", "ゆー", "まこ", "ともか"},
    "ラブソングに襲われる【サーオリ】": {"ちさと", "ともか", "あんな", "そら", "まこ", "しおん", "なるみ", "まあや", "ひじり", "ひな"},
    "バチモリーナ【サーオリ】": {"はるか", "ひじり", "ひな", "あんな", "しおん", "ちさと","なるみ","まあや","ともか"},
    "ブルーハワイレモン【サーオリ】": {"そら", "こゆ", "ひまり", "ゆー", "まこ", "あんな", "はるか","ひじり","ともか","なるみ","まあや","ひな"},
    "超特急逃走中【サーオリ】": {"ちさと", "ひじり", "まい", "あんな", "そら", "ひな", "こゆ", "ゆー", "ともか", "なるみ"},
    "盛れミ・アモーレ【サーオリ】": {"ともか", "そら", "ゆー", "まこ", "しおん", "あんな", "ひまり"},
    "かわいいメモリアル【サーオリ】": {"ゆー", "ひな", "なるみ", "こゆ", "ひじり","ちさと"},
    "都営大江戸線の六本木駅で抱きしめて【サーオリ】": {"ともか", "なるみ", "まあや", "ひな"},
    "special spell【サーオリ】": {"はるか", "そら", "しおん", "ちさと"},
    "キスミ―パティシエ【サーオリ】": {"ひまり", "そら", "あんな", "まい", "はるか", "ちさと", "ひな"},
    "ラブコード【サーオリ】": {"まあや", "はるか", "ひじり", "そら", "あんな","ともか","なるみ"},
    "キューにストップできません！【サーオリ】": {"ゆー", "はるか", "まい", "ひまり", "あんな", "そら", "ちさと","ひじり"},
    "はちゃめちゃわちゃライフ！【サーオリ】": {"ゆー","まい", "なるみ", "ひまり","ちさと", "あんな", "はるか", },
    "feel my rhythm【サーオリ】": {"しおん", "まあや","ひまり", "まこ",  "ともか"},
    "アザトカワイイ【いちょう】": {"しおん", "ひな", "こゆ", "まあや", "なるみ","ひじり", "ちさと", "ゆー", "あんな", "まこ",  "ともか", "そら"},
    "パレオはエメラルド【いちょう】": {"ひな", "まあや", "なるみ", "ゆー",  "まこ", "ともか", "そら"},
    "ひたむきシンデレラ【いちょう】": { "まい","なるみ", "ひまり","ちさと", "ゆー", "あんな", "はるか", "ともか"},
    "レべチかわいい！【いちょう】": {"しおん", "まい", "ひまり","ひじり", "ゆー", "あんな", "そら"},
    "シャウトシャトル【いちょう】": {"しおん","まあや", "なるみ", "あんな","ひじり", "はるか", "そら"},
    "バカデカボイスで好きって叫べ【いちょう】": { "しおん", "ひな",  "なるみ",  "ひじり", "あんな", "はるか", "そら"},
    "キュンとクラフト【いちょう】": {"まい", "まあや", "なるみ", "ひじり", "ちさと", "ともか", "あんな", "はるか", "そら"},
    "君とたこやきLove恋め【いちょう】": { "しおん", "ひまり","ゆー", "ともか", "はるか", "そら","ひな"}, 
    "ラストノートしか知らない【いちょう】": {"まあや", "なるみ", "ひまり","ひじり", "ちさと", "ゆー", "あんな", "まこ", "ともか", "はるか"},
    "ピーチティーとピーチパイ【いちょう】": { "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ", "ひまり", "ひじり", "ゆー", "あんな","はるか", "そら"},
    "ちゅららんレーサー【いちょう】": {"しおん", "まい", "ひな", "ひまり", "あんな", "まこ", "はるか", "そら"}, 
    "君ラブ【いちょう】": { "まい", "ひな", "ひまり","あんな","ともか", "はるか"}, 
    "botばっか【いちょう】": {"こゆ", "ゆー", "あんな", "ともか"},
    "yes or yes【いちょう】": {"しおん", "まい", "まあや", "ひまり","ちさと", "ゆー","まこ", "ともか", "そら"},
    "MUSE【いちょう】": { "しおん", "まい", "まあや", "ひまり", "ひじり","まこ", "ともか"},
    "カルテNO.2222【いちょう】": {"こゆ", "なるみ","あんな", "はるか"},
    "Accendio【いちょう】": { "しおん", "まい", "まあや", "ひまり","ちさと","ともか"},
    "queencard【いちょう】": {"しおん", "まあや", "ちさと", "まこ", "そら"},
    "veryveryvery【いちょう】": {"まい","こゆ", "ちさと", "ゆー",  "まこ", "ともか", "そら"},






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
    # ===== スイパラ =====
    "ラブ♡タップ【スイパラ】": "そら",
    "Pixel Ribbon【スイパラ】": "なるみ",
    "マッシュ・ド・アート【スイパラ】": "ひまり",
    "POP IN 2【スイパラ】": "ゆー",
    "シンデレラマインド【スイパラ】": "まい",

    # ===== サーオリ =====
    "What Is Love?【サーオリ】": "ちさと",
    "ラブソングに襲われる【サーオリ】": "そら",
    "バチモリーナ【サーオリ】": "はるか",
    "ブルーハワイレモン【サーオリ】": "あんな",
    "超特急逃走中【サーオリ】": "ひじり",
    "盛れミ・アモーレ【サーオリ】": "ともか",
    "かわいいメモリアル【サーオリ】": "ひな",
    "都営大江戸線の六本木駅で抱きしめて【サーオリ】": "ひな",
    "special spell【サーオリ】": "そら",
    "キスミ―パティシエ【サーオリ】": "まい",
    "ラブコード【サーオリ】": "なるみ",
    "キューにストップできません！【サーオリ】": "ひまり",
    "はちゃめちゃわちゃライフ！【サーオリ】": "ひまり",
    "feel my rhythm【サーオリ】": "しおん",

    # ===== いちょう =====
    "アザトカワイイ【いちょう】": "ひな",
    "パレオはエメラルド【いちょう】": "まあや",
    "ひたむきシンデレラ【いちょう】": "ゆー",
    "レべチかわいい！【いちょう】": "ひまり",
    "シャウトシャトル【いちょう】": "そら",
    "バカデカボイスで好きって叫べ【いちょう】": "はるか",
    "キュンとクラフト【いちょう】": "ひじり",
    "君とたこやきLove恋め【いちょう】": "ゆー",
    "ラストノートしか知らない【いちょう】": "なるみ",
    "ピーチティーとピーチパイ【いちょう】": "あんな",
    "ちゅららんレーサー【いちょう】": "しおん",
    "君ラブ【いちょう】": "あんな",
    "botばっか【いちょう】": "しおん",
    "yes or yes【いちょう】": "まい",
    "MUSE【いちょう】": "まい",
    "カルテNO.2222【いちょう】": "こゆ",
    "Accendio【いちょう】": "ちさと",
    "queencard【いちょう】": "しおん",
    "veryveryvery【いちょう】": "まこ",
}


# ========================
# 🎨 曲アイコン関数
# ========================
def get_song_icon(song_name):
    if "【スイパラ】" in song_name:
        return "✨"
    elif "【サーオリ】" in song_name:
        return "🫧🌸"
    elif "【いちょう】" in song_name:
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
show_kirara_songs = st.checkbox("スイパラの曲を表示する")

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
    st.markdown("## ✨ の曲のスイパラの出席率ランキング")
    kirara_songs = {k: v for k, v in songs.items() if "【スイパラ】" in k}
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
    st.markdown("## 📋 スイパラの曲ごとの出席状況")

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
filtered_songs = {k: v for k, v in songs.items() if "【スイパラ】" not in k}

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







