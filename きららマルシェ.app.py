import streamlit as st


# ==================
# 🎵 アプリ本体
# ==================
st.title("♬ダンス練習チェッカー(きららマルシェ・まちかね・単独)")

# 全メンバー（事前入力）
all_members = ["ゆう", "まこ", "ちさと", "ひな", "しおん", "そら", "なるみ",  "ひまり",
               "ひじり", "まい", "ゆー", "あんな","こゆ","はる","はるか","まあや","ともか"]

# 曲とメンバーの対応表
songs = {
    "ラブ♡タップ【きらら】": {"しおん", "ゆー", "ひじり", "あんな", "そら"},
    "Pixel Ribbon【きらら】": {"ひな", "なるみ", "まい", "あんな", "ひじり","そら"},
    "マッシュ・ド・アート【きらら】": {"ひまり", "ひじり", "ちさと", "しおん"},
    "Ready!【きらら】": {"まこ", "ひまり", "あんな", "そら", "ひな"},
    "くりてぃかる♡ぷりちー【きらら】": {"ひまり", "まい", "まこ", "ひじり", "あんな", "そら","なるみ","しおん","ひな"},
    "POP IN 2【きらら】": {"ひじり", "ゆー", "ちさと"},
    "シンデレラマインド【きらら】": {"ひまり", "ちさと", "まい", "なるみ", "そら"},
    "ヒロインとオオカミ【きらら】": {"ひまり", "ちさと", "なるみ", "ゆう", "ひな","そら","まこ","しおん","ひじり","あんな","まい","ゆー"},
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
# 📋 各曲の出席状況（出席率順に並べる）
# ----------------------
st.markdown("---")
st.markdown("## 📋 曲ごとの出席状況（出席率順）")

for song, _, _, _ in ranking:  # 出席率順に並べられた曲名リストを使用
    members = songs[song]
    attending = members & selected_members
    absent = members - selected_members

    st.subheader(f"🎵 {song}")
    st.write(f"👥 全体人数: {len(members)}")
    st.write(f"🙋‍♀️ 出席人数: {len(attending)}")
    st.write(f"✅ 出席: {'、'.join(sorted(attending)) or 'なし'}")
    st.write(f"❌ 不在: {'、'.join(sorted(absent)) or 'なし'}")

