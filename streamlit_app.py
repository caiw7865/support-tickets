import streamlit as st

# 页面配置（紧凑模式）
st.set_page_config(
    page_title="FAIR成熟度",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 全局极小间距 CSS
st.markdown("""
<style>
.block-container {
    padding: 1rem 2rem;
    max-width: 1400px;
    margin: 0 auto;
}
hr { margin: 0.7rem 0 !important; }
h1 { font-size: 2rem !important; margin: 0 !important; }
h2 { font-size: 1.4rem !important; margin: 0.3rem 0 !important; }
h3 { font-size: 1.15rem !important; margin: 0.2rem 0 !important; }
p, li { font-size: 0.95rem !important; margin:0.1rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ====================== 顶部标题 ======================
st.title("FAIR成熟度")

st.markdown("##### 元数据统计信息")
st.markdown("""
- 知识图谱元数据包含标题、标识符在内的17个元数据项
- 数据资源元数据包含标题、下载链接在内的10个元数据项
""")
st.divider()

# ====================== 左右布局（超紧凑） ======================
left_col, right_col = st.columns([1.1, 1], gap="small")

# ========== 左侧：双层环形图（1:1还原，紧凑好看） ==========
with left_col:
    st.markdown("##### FAIR成熟度图谱")
    st.markdown("""
<div style="width: 340px; margin:0 auto; position:relative; height:340px;">
  <div style="position:absolute; width:340px; height:340px; 
background:conic-gradient(#36c270 0deg 90deg, #ff3b30 90deg 180deg, #40b8f0 180deg 270deg, #ffc107 270deg 360deg); 
border-radius:50%; transform:rotate(45deg);">
  </div>
  <div style="position:absolute; width:340px; height:340px; 
background:conic-gradient(
#00a650 0deg 67deg, #eee 67deg 90deg,
#ff3b30 90deg 180deg,
#40b8f0 180deg 270deg,
#ffc107 270deg 360deg
); 
border-radius:50%; transform:rotate(45deg); padding:35px; box-sizing:border-box;">
  </div>
  <div style="position:absolute; width:150px; height:150px; background:#fff; 
border-radius:50%; top:95px; left:95px; 
display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold;">
    FAIR
  </div>

  <!-- 内层大标签 -->
  <div style="position:absolute; top:60px; left:160px; font-weight:bold; color:white; font-size:17px;">F</div>
  <div style="position:absolute; top:160px; left:50px; font-weight:bold; color:white; font-size:17px;">A</div>
  <div style="position:absolute; top:160px; left:270px; font-weight:bold; color:white; font-size:17px;">I</div>
  <div style="position:absolute; top:270px; left:160px; font-weight:bold; color:white; font-size:17px;">R</div>

  <!-- 外层子项 -->
  <div style="position:absolute; top:35px; left:135px; font-weight:bold; font-size:13px;">F1 F2 F3</div>
  <div style="position:absolute; top:135px; left:30px; font-weight:bold; font-size:13px;">A1 A2</div>
  <div style="position:absolute; top:135px; left:260px; font-weight:bold; font-size:13px;">I1 I2 I3</div>
  <div style="position:absolute; top:285px; left:130px; font-weight:bold; font-size:13px;">R1.1 R1.2</div>
</div>
""", unsafe_allow_html=True)

# ========== 右侧：FAIR 说明（极度紧凑） ==========
with right_col:
    st.markdown("##### FAIR指标说明")

    st.markdown("**F**")
    st.caption("F1: 知识图谱元数据提供URI标识符，且通过有效性检验")
    st.caption("F2: 共有27个元数据项")
    st.caption("F3: 数据资源元数据未提供数据标识符")

    st.markdown("**A**")
    st.caption("A1: 元数据包含标题、描述、主题等元数据项，且标识符可关联至元数据记录")
    st.caption("A2: 知识图谱元数据标识符通过有效验证")

    st.markdown("**I**")
    st.caption("I1: 元数据可以RDF形式实现描述")
    st.caption("I2: 元数据项均可映射至遵循FAIR原则的词汇表")
    st.caption("I3: 元数据未提供对其他数据的引用信息")

    st.markdown("**R**")
    st.caption("R1.1: 采用Creative Commons许可体系")
    st.caption("R1.2: 元数据包含作者、时间等来源信息")

# ====================== 底部悬浮按钮 ======================
st.markdown("""
<style>
.fixed-bottom {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    padding: 10px 25px;
    box-shadow: 0 -2px 8px rgba(0,0,0,0.08);
    z-index: 9999;
    display: flex;
    justify-content: flex-end;
    gap: 12px;
}
</style>
<div class="fixed-bottom">
    <button disabled style="background:#0066cc; color:white; border:none; border-radius:6px; padding:8px 22px; font-weight:bold;">
        JSON数据
    </button>
    <button disabled style="background:#00a862; color:white; border:none; border-radius:6px; padding:8px 22px; font-weight:bold;">
        Turtle数据
    </button>
</div>
""", unsafe_allow_html=True)
