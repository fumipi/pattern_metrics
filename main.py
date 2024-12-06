import streamlit as st
import pandas as pd

st.title("ストレートジャケット原型寸法計算")

# ユーザー入力
height = st.number_input("身長(cm)", value=158.0, step=0.1)
bust = st.number_input("バスト(cm)", value=82.0, step=0.1)
waist = st.number_input("ウエスト(cm)", value=64.0, step=0.1)
hip = st.number_input("ヒップ(cm)", value=90.0, step=0.1)

if st.button("計算"):
    # 基本計算（例示。実際の値はユーザが提示した画像の通りに修正してください）
    A_height = height
    A_bust = bust
    A_waist = waist
    A_hip = hip

    A_back_length = height/4 + 1.0
    A_front_length = A_back_length + 1.3 + (bust - 80)*0.1
    A_hip_length = height/8
    A_kama_length = (bust/2) + (bust/4) + 5.0
    A_back_shoulder = (bust/2) + 1.0 - (bust-80)/20
    A_front_shoulder = (bust/2) + (bust-80)/20
    A_back_width = (bust/4) + 1.0 - (bust-80)/20
    A_front_width = (bust/4) + 0.5
    A_nipple_spacing = (bust/4) + 0.5
    A_back_neck = bust/20
    A_front_neck = (bust/20) + 0.3

    # トルソー用ゆるみ分 (例示)
    B_torso_height = 0.0
    B_torso_bust = 9.0
    B_torso_waist = 7.0
    B_torso_hip = 6.0
    B_torso_back_length = 0.8
    B_torso_front_length = 0.9
    B_torso_hip_length = 0.2
    B_torso_kama_length = 1.0
    B_torso_back_shoulder = 1.0
    B_torso_front_shoulder = 0.5
    B_torso_back_width = 1.5
    B_torso_front_width = 0.5
    B_torso_nipple_spacing = 0.75
    B_torso_back_neck = 0.5
    B_torso_front_neck = 0.5

    # トルソー出来上がり寸法 (A+B_torso)
    AB_height = A_height + B_torso_height
    AB_bust = A_bust + B_torso_bust
    AB_waist = A_waist + B_torso_waist
    AB_hip = A_hip + B_torso_hip
    AB_back_length = A_back_length + B_torso_back_length
    AB_front_length = A_front_length + B_torso_front_length
    AB_hip_length = A_hip_length + B_torso_hip_length
    AB_kama_length = A_kama_length + B_torso_kama_length
    AB_back_shoulder = A_back_shoulder + B_torso_back_shoulder
    AB_front_shoulder = A_front_shoulder + B_torso_front_shoulder
    AB_back_width = A_back_width + B_torso_back_width
    AB_front_width = A_front_width + B_torso_front_width
    AB_nipple_spacing = A_nipple_spacing + B_torso_nipple_spacing
    AB_back_neck = A_back_neck + B_torso_back_neck
    AB_front_neck = A_front_neck + B_torso_front_neck

    # ストレートジャケット用ゆるみ分 (例示)
    B_jacket_height = 0.0
    B_jacket_bust = 12.0
    B_jacket_waist = 1.0
    B_jacket_hip = 2.0
    B_jacket_back_length = 1.5
    B_jacket_front_length = 1.0
    B_jacket_hip_length = 0.5
    B_jacket_kama_length = 1.0
    B_jacket_back_shoulder = 0.5
    B_jacket_front_shoulder = 0.5
    B_jacket_back_width = 0.5
    B_jacket_front_width = 0.5
    B_jacket_nipple_spacing = 0.5
    B_jacket_back_neck = 0.5
    B_jacket_front_neck = 0.5

    # ストレートジャケット出来上がり寸法 (A+B_torso+B_jacket)
    ABJ_height = AB_height + B_jacket_height
    ABJ_bust = AB_bust + B_jacket_bust
    ABJ_waist = AB_waist + B_jacket_waist
    ABJ_hip = AB_hip + B_jacket_hip
    ABJ_back_length = AB_back_length + B_jacket_back_length
    ABJ_front_length = AB_front_length + B_jacket_front_length
    ABJ_hip_length = AB_hip_length + B_jacket_hip_length
    ABJ_kama_length = AB_kama_length + B_jacket_kama_length
    ABJ_back_shoulder = AB_back_shoulder + B_jacket_back_shoulder
    ABJ_front_shoulder = AB_front_shoulder + B_jacket_front_shoulder
    ABJ_back_width = AB_back_width + B_jacket_back_width
    ABJ_front_width = AB_front_width + B_jacket_front_width
    ABJ_nipple_spacing = AB_nipple_spacing + B_jacket_nipple_spacing
    ABJ_back_neck = AB_back_neck + B_jacket_back_neck
    ABJ_front_neck = AB_front_neck + B_jacket_front_neck

    # DataFrame作成
    df = pd.DataFrame([
        ["身長", A_height, B_torso_height, AB_height, B_jacket_height, ABJ_height],
        ["バスト", A_bust, B_torso_bust, AB_bust, B_jacket_bust, ABJ_bust],
        ["ウエスト", A_waist, B_torso_waist, AB_waist, B_jacket_waist, ABJ_waist],
        ["ヒップ", A_hip, B_torso_hip, AB_hip, B_jacket_hip, ABJ_hip],
        ["後ろ丈", A_back_length, B_torso_back_length, AB_back_length, B_jacket_back_length, ABJ_back_length],
        ["前丈", A_front_length, B_torso_front_length, AB_front_length, B_jacket_front_length, ABJ_front_length],
        ["ヒップ丈", A_hip_length, B_torso_hip_length, AB_hip_length, B_jacket_hip_length, ABJ_hip_length],
        ["カマ丈", A_kama_length, B_torso_kama_length, AB_kama_length, B_jacket_kama_length, ABJ_kama_length],
        ["後ろ肩丈", A_back_shoulder, B_torso_back_shoulder, AB_back_shoulder, B_jacket_back_shoulder, ABJ_back_shoulder],
        ["前肩丈", A_front_shoulder, B_torso_front_shoulder, AB_front_shoulder, B_jacket_front_shoulder, ABJ_front_shoulder],
        ["後ろ幅", A_back_width, B_torso_back_width, AB_back_width, B_jacket_back_width, ABJ_back_width],
        ["前幅", A_front_width, B_torso_front_width, AB_front_width, B_jacket_front_width, ABJ_front_width],
        ["乳頭間隔", A_nipple_spacing, B_torso_nipple_spacing, AB_nipple_spacing, B_jacket_nipple_spacing, ABJ_nipple_spacing],
        ["後ろ首幅", A_back_neck, B_torso_back_neck, AB_back_neck, B_jacket_back_neck, ABJ_back_neck],
        ["前首幅", A_front_neck, B_torso_front_neck, AB_front_neck, B_jacket_front_neck, ABJ_front_neck],
    ], columns=[
        "部位", 
        "基本身体寸法計算値(A)", 
        "トルソーゆるみ分(B_torso)", 
        "トルソー出来上がり寸法(A+B)", 
        "ストレートジャケットゆるみ分(B_jacket)", 
        "ストレートジャケット出来上がり寸法(A+B+B_jacket)"
    ])

    # 部位列は文字列、その他は数値列になっているはずです。
    # 念のため、最初の列(部位)以外を数値列としてformat適用
    numeric_cols = [col for col in df.columns if col != "部位"]

    st.write("### 計算結果")
    df_styled = df.style.format("{:.1f}", subset=numeric_cols).set_table_styles([
        {
        'selector': 'td',
        'props': [
            ('writing-mode', 'horizontal-tb'),
            ('transform', 'rotate(0deg)'),
            ('white-space', 'nowrap')
            ]
        }
    ])
    st.table(df_styled)
