import streamlit as st
from google import genai  # 新しいライブラリのインポート方法
from PIL import Image

# --- 設定 ---
# ※APIキーは最新のライブラリ形式に合わせて設定
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

# --- ページ設定と天子のキャラクター設定はそのまま ---
st.set_page_config(page_title="Theater of Fashion", page_icon="🎭")

# （中略：以前のCSSなどはそのまま使ってOKよ）

# --- 解析・提案ボタンの処理部分 ---
if st.button("天子にプロデュースを依頼する"):
    if uploaded_file is not None:
        with st.spinner("天子があなたの魅力を劇的に構成中..."):
            image = Image.open(uploaded_file)
            
            prompt = f"あなたは早咲天子です。予算{budget}円で、画像の人物の体型・肌を分析し、最高のコーデを提案して。"
            
            # 新しいSDKの呼び出し方
            response = client.models.generate_content(
                model="gemini-2.0-flash", # 最新モデル
                contents=[prompt, image]
            )
            
            st.markdown("---")
            st.write("### ✨ 天子のディレクション・シート")
            st.write(response.text)