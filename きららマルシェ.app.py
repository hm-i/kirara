import streamlit as st


# ==================
# 🎵 アプリ本体
# ==================
st.title("♬ダンス練習チェッカー(きららマルシェ・まちかね・単独)")

# 全メンバー（事前入力）
all_members = ["ゆう", "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ",  "ひまり",
               "ひじり", "ちさと", "ゆー", "あんな","まこ","はる","はるか","そら","ともか"]

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
    "カラコンウインク【まちかね・単独】": {"ゆう", "しおん", "まい", "ひな", "こゆ", "まあや", "なるみ",  "ひまり",
               "ひじり", "ちさと", "ゆー", "あんな","まこ","はる","はるか","そら","ともか"},
    "とくべチュ、して【まちかね・単独】": {"ちさと", "ゆう", "あんな", "そら", "まこ", "しおん", "なるみ","はるか","ひじり","ひな"},
    "超最強【まちかね・単独】": {"はる", "ひまり", "ひな", "あんな", "しおん", "ちさと"},
  　"倍倍fight【まちかね・単独】":{"そら","ゆう","ひまり","はる","まい","あんな","はるか"}
　  "フライングゲット【まちかね・単独】":{"ちさと","ひじり","ゆう","あんな","そら","まこ","しおん","ゆー","ともか","なるみ"}
 　 "Snow halation【まちかね】":{"ゆう","ともか","ゆー","まい","あんな","そら","しおん","なるみ","ひじり"}
     "アイドルライフエクストラパック【まちかね】":{"ゆう","ひじり","そら","しおん","なるみ","はるか","ひな"}
     "AtoZ【まちかね】":{"まい","そら","まあや","はる","しおん","ゆー","ひじり"}
     "君とtea for two【まちかね】":{"ひじり","ひまり","こゆ","ともか"}
     "恋に恋する眠り姫【まちかね】":{"なるみ","ひまり","ともか","あんな"}
     "The feels【まちかね】":{"まい","はる","ちさと","ひじり","まこ","しおん","ともか","ひまり"}
     "サイレントマジョリティー【まちかね】":{"ひな","ひじり","ちさと","ゆう","あんな","まこ","ともか","なるみ","ひまり"}
     "金曜日のおはよう【まちかね】":{"ひまり","ひじり","あんな","はる","はるか","こゆ","ともか","ゆー","まあや","まい"}
     "イェイェ【単独】":{"ゆー","そら","しおん","こゆ","はるか"}
     "Cherish(My love)【単独】":{"ひじり","まい","そら","まこ","こゆ"}
     "仲直りシュークリーム【単独】":{"ゆう","あんな","はる","ゆー","しおん","まこ","なるみ","はるか","ひな","ひじり"}
     "ラブトレ【単独】":{"ひまり","そら","あんな","まい","はる","ゆー","ゆう","なるみ"}
     "ネモネモ【単独】":{"ちさと","まい","ひじり","そら","まこ"}
     "２,３年学年曲":{"ゆう","ひな","しおん","なるみ","まこ","そら","ちさと"}
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




