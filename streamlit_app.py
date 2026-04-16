import streamlit as st

# -------------------------- 页面配置 --------------------------
st.set_page_config(
    page_title="FAIR成熟度",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 顶部 --------------------------
st.title("FAIR成熟度")
st.divider()

st.markdown("### 元数据统计信息")
st.markdown("""
- 知识图谱元数据包含标题、标识符在内的17个元数据项
- 数据资源元数据包含标题、下载链接在内的10个元数据项
""")
st.divider()

# -------------------------- 左右布局 --------------------------
left_col, right_col = st.columns([1, 1])

# ========== 左侧：HTML + CSS 绘制环形图（1:1 复刻你的图，绝不报错） ==========
with left_col:
    st.subheader("FAIR 成熟度图谱")

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 450px;">
        <div style="width: 380px; height: 380px; border-radius: 50%; position: relative; background: conic-gradient(
            #32c872 0deg 90deg,
            #ff3b30 90deg 180deg,
            #40b8f0 180deg 270deg,
            #ffc107 270deg 360deg
        ); padding: 30px;">
            <div style="width: 320px; height: 320px; border-radius: 50%; background: conic-gradient(
                #00a650 0deg 67deg,    /* F1-F3 */
                #f1f1f1 67deg 90deg,   /* F4 空白 */
                #ff3b30 90deg 180deg,  /* A1-A2 */
                #00a8e8 180deg 270deg, /* I1-I3 */
                #ffb700 270deg 360deg  /* R1.1-R1.2 */
            ); padding:25px;">
                <div style="width:250px; height:250px; border-radius:50%; background:white; display: flex; justify-content:center; align-items:center; font-size:22px; font-weight:bold;">
                    FAIR
                </div>
            </div>
        </div>
    </div>
    <div style="text-align:center; font-size:16px; font-weight:bold; margin-top:10px;">
        <span style="color:#00a650">F</span> &nbsp;&nbsp;
        <span style="color:#ff3b30">A</span> &nbsp;&nbsp;
        <span style="color:#00a8e8">I</span> &nbsp;&nbsp;
        <span style="color:#ffb700">R</span>
    </div>
    <div style="text-align:center; font-size:14px; margin-top:5px;">
        F1 F2 F3 | A1 A2 | I1 I2 I3 | R1.1 R1.2
    </div>
    """, unsafe_allow_html=True)

# ========== 右侧：你要求的 FAIR 文本 ==========
with right_col:
    st.subheader("FAIR 成熟度指标说明")
    st.markdown("---")

    st.markdown("### 🟢 **F**")
    st.write("F1: 知识图谱元数据提供URI标识符，且通过有效性检验")
    st.write("F2: 共有27个元数据项")
    st.write("F3: 数据资源元数据未提供数据标识符")
    st.divider()

    st.markdown("### 🔴 **A**")
    st.write("A1: 元数据包含标题、描述、主题等元数据项，且标识符可关联至元数据记录")
    st.write("A2: 知识图谱元数据标识符通过有效验证")
    st.divider()

    st.markdown("### 🔵 **I**")
    st.write("I1: 元数据可以RDF形式实现描述")
    st.write("I2: 元数据项均可映射至遵循FAIR原则的词汇表")
    st.write("I3: 元数据未提供对其他数据的引用信息")
    st.divider()

    st.markdown("### 🟡 **R**")
    st.write("R1.1: 采用Creative Commons许可体系")
    st.write("R1.2: 元数据包含作者、时间等来源信息")

# -------------------------- 底部悬浮按钮（永不消失） --------------------------
st.markdown("""
<style>
.block-container {
    padding-bottom: 100px;
}
.fixed-bottom {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    padding: 18px 35px;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    z-index: 99999;
    display: flex;
    justify-content: flex-end;
    gap: 15px;
}
</style>

<div class="fixed-bottom">
    <button disabled style="background:#0066cc; color:white; border:none; border-radius:8px; padding:12px 30px; font-size:1rem; font-weight:bold;">
        JSON数据
    </button>
    <button disabled style="background:#00a862; color:white; border:none; border-radius:8px; padding:12px 30px; font-size:1rem; font-weight:bold;">
        Turtle数据
    </button>
</div>
""", unsafe_allow_html=True)
