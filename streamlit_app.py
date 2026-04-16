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

# ========== 左侧：1:1 复刻双层 FAIR 环形图（带全部标签 + 清晰分区） ==========
with left_col:
    st.subheader("FAIR 成熟度图谱")

    st.markdown("""
<style>
.fair-chart {
    position: relative;
    width: 400px;
    height: 400px;
    margin: 0 auto;
}
.inner-circle {
    position: absolute;
    width: 160px;
    height: 160px;
    background: white;
    border-radius: 50%;
    top: 120px;
    left: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
    z-index: 10;
}
.slice {
    position: absolute;
    width: 400px;
    height: 400px;
    clip-path: polygon(50% 50%, 50% 0%, 100% 0%, 100% 100%, 50% 100%);
    border-radius: 50%;
}
</style>

<div class="fair-chart">
  <div class="inner-circle">FAIR</div>

  <!-- 内层：F A I R 四大分区 -->
  <div style="position:absolute; width:400px; height:400px; background:conic-gradient(#36c270 0% 25%, #ff3b30 25% 50%, #40b8f0 50% 75%, #ffc107 75% 100%); border-radius:50%; transform:rotate(45deg);"></div>

  <!-- 外层：子项 F1 F2 F3 / A1 A2 / I1 I2 I3 / R1.1 R1.2 -->
  <div style="position:absolute; width:400px; height:400px; background:conic-gradient(
    #00a650 0deg 67deg,
    #eee 67deg 90deg,
    #ff3b30 90deg 180deg,
    #00a8e8 180deg 270deg,
    #ffb700 270deg 360deg
  ); border-radius:50%; transform:rotate(45deg); padding:40px; box-sizing:border-box;"></div>

  <!-- 内层文字 F A I R -->
  <div style="position:absolute; top:70px; left:185px; font-size:18px; font-weight:bold; color:white;">F</div>
  <div style="position:absolute; top:185px; left:70px; font-size:18px; font-weight:bold; color:white;">A</div>
  <div style="position:absolute; top:185px; left:310px; font-size:18px; font-weight:bold; color:white;">I</div>
  <div style="position:absolute; top:310px; left:185px; font-size:18px; font-weight:bold; color:white;">R</div>

  <!-- 外层文字标签 -->
  <div style="position:absolute; top:45px; left:165px; font-size:14px; font-weight:bold;">F1 F2 F3</div>
  <div style="position:absolute; top:160px; left:45px; font-size:14px; font-weight:bold;">A1 A2</div>
  <div style="position:absolute; top:160px; left:325px; font-size:14px; font-weight:bold;">I1 I2 I3</div>
  <div style="position:absolute; top:335px; left:160px; font-size:14px; font-weight:bold;">R1.1 R1.2</div>
</div>
""", unsafe_allow_html=True)

# ========== 右侧：FAIR 说明 ==========
with right_col:
    st.subheader("FAIR 成熟度指标说明")
    st.divider()

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

# -------------------------- 底部永久悬浮按钮 --------------------------
st.markdown("""
<style>
.block-container { padding-bottom: 100px; }
.fixed-bottom {
    position: fixed; bottom: 0; left: 0; width: 100%;
    background: white; padding: 18px 35px;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    z-index: 99999; display: flex; justify-content: flex-end; gap:15px;
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
