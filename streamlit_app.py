import streamlit as st

# -------------------------- 页面配置 --------------------------
st.set_page_config(
    page_title="FAIR成熟度",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 顶部：标题 + 统计 --------------------------
st.title("FAIR成熟度")
st.divider()

st.markdown("### 元数据统计信息")
st.markdown("""
- 知识图谱元数据包含标题、标识符在内的17个元数据项
- 数据资源元数据包含标题、下载链接在内的10个元数据项
""")
st.divider()

# -------------------------- 下半部分：左右布局 --------------------------
left_col, right_col = st.columns([1, 1], gap="large")

# ========== 左侧：用文字 + 样式还原 FAIR 图（不使用任何绘图库） ==========
with left_col:
    st.subheader("FAIR 成熟度评估")
    st.markdown("""
    <div style="font-size:18px; line-height:2.2; padding-left:20px;">
        <span style="color:#00a850; font-weight:bold;">F ●</span> 
        <span style="margin-left:8px;">F1  F2  F3</span><br>
        <span style="color:#ff3b30; font-weight:bold;">A ●</span> 
        <span style="margin-left:8px;">A1  A2</span><br>
        <span style="color:#40b8f0; font-weight:bold;">I ●</span> 
        <span style="margin-left:8px;">I1  I2  I3</span><br>
        <span style="color:#ffc107; font-weight:bold;">R ●</span> 
        <span style="margin-left:8px;">R1.1  R1.2</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("左侧为 FAIR 成熟度图谱结构：F / A / I / R 四大维度")

# ========== 右侧：你要求的完整文本 ==========
with right_col:
    st.subheader("FAIR 成熟度说明")

    st.markdown("### **F**")
    st.write("F1: 知识图谱元数据提供URI标识符，且通过有效性检验")
    st.write("F2: 共有27个元数据项")
    st.write("F3: 数据资源元数据未提供数据标识符")

    st.divider()

    st.markdown("### **A**")
    st.write("A1: 元数据包含标题、描述、主题等元数据项，且标识符可关联至元数据记录")
    st.write("A2: 知识图谱元数据标识符通过有效验证")

    st.divider()

    st.markdown("### **I**")
    st.write("I1: 元数据可以RDF形式实现描述")
    st.write("I2: 元数据项均可映射至遵循FAIR原则的词汇表")
    st.write("I3: 元数据未提供对其他数据的引用信息")

    st.divider()

    st.markdown("### **R**")
    st.write("R1.1: 采用Creative Commons许可体系")
    st.write("R1.2: 元数据包含作者、时间等来源信息")

# -------------------------- 底部永久悬浮按钮（和你之前风格一致） --------------------------
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
    z-index: 9999;
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
