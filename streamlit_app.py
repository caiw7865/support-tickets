import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# -------------------------- 页面全局配置 --------------------------
st.set_page_config(
    page_title="FAIR成熟度",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 页面上半部分：标题 + 统计信息 --------------------------
st.title("FAIR成熟度")
st.divider()

# 元数据统计信息
st.markdown("### 元数据统计信息")
st.markdown("""
- 知识图谱元数据包含标题、标识符在内的17个元数据项
- 数据资源元数据包含标题、下载链接在内的10个元数据项
""")
st.divider()

# -------------------------- 下半部分：左右分栏 --------------------------
left_col, right_col = st.columns([1, 1], gap="large")

# ========== 左侧：1:1复刻环形图 ==========
with left_col:
    st.subheader("FAIR成熟度环形图")
    
    # 创建画布
    fig, ax = plt.subplots(figsize=(8, 8), dpi=150)
    ax.set_aspect('equal')
    
    # 环形参数
    inner_radius = 0.3
    outer_radius = 0.5
    wedgeprops_inner = {'width': 0.2, 'edgecolor': 'white', 'linewidth': 2}
    wedgeprops_outer = {'width': 0.2, 'edgecolor': 'white', 'linewidth': 1.5}
    
    # 内层大分类（F/A/I/R）
    inner_labels = ['F', 'A', 'I', 'R']
    inner_colors = ['#36c270', '#ff3b30', '#40b8f0', '#ffc107']
    inner_sizes = [25, 25, 25, 25]  # 均分360°
    
    # 绘制内层
    ax.pie(
        inner_sizes,
        radius=inner_radius + 0.2,
        colors=inner_colors,
        labels=inner_labels,
        labeldistance=0.7,
        wedgeprops=wedgeprops_inner,
        startangle=90,
        counterclock=False,
        textprops={'fontsize': 12, 'weight': 'bold'}
    )
    
    # 外层子分类（完全对应你的图）
    outer_labels = [
        'F1', 'F2', 'F3', 'F4',
        'A1', 'A2',
        'I1', 'I2', 'I3',
        'R1.1', 'R1.2'
    ]
    outer_colors = [
        '#00a650', '#00a650', '#00a650', '#f8f9fa',  # F组
        '#e60023', '#e60023',                        # A组
        '#00a8e8', '#00a8e8', '#f8f9fa',              # I组
        '#ffb700', '#ffb700'                          # R组
    ]
    # 每个大分类下的子项占比（对应内层25%的拆分）
    outer_sizes = [
        8.33, 8.33, 8.33, 0.01,  # F (25%拆4份，F4为空白)
        12.5, 12.5,              # A (25%拆2份)
        8.33, 8.33, 8.34,       # I (25%拆3份)
        12.5, 12.5               # R (25%拆2份)
    ]
    
    # 绘制外层
    wedges, texts = ax.pie(
        outer_sizes,
        radius=outer_radius + 0.2,
        colors=outer_colors,
        labels=outer_labels,
        labeldistance=0.9,
        wedgeprops=wedgeprops_outer,
        startangle=90,
        counterclock=False,
        textprops={'fontsize': 11, 'weight': 'bold'}
    )
    
    # 旋转标签，保证可读性
    for i, text in enumerate(texts):
        ang = (wedges[i].theta2 + wedges[i].theta1) / 2
        if ang > 90 and ang < 270:
            text.set_rotation(ang + 180)
        else:
            text.set_rotation(ang)
    
    # 隐藏坐标轴
    ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)

# ========== 右侧：FAIR 各维度说明文本 ==========
with right_col:
    st.subheader("FAIR 各维度说明")
    
    # F 维度
    st.markdown("### **F**")
    st.markdown("""
- **F1**: 知识图谱元数据提供URI标识符，且通过有效性检验
- **F2**: 共有27个元数据项
- **F3**: 数据资源元数据未提供数据标识符
""")
    st.divider()
    
    # A 维度
    st.markdown("### **A**")
    st.markdown("""
- **A1**: 元数据包含标题、描述、主题等元数据项，且标识符可关联至元数据记录
- **A2**: 知识图谱元数据标识符通过有效验证
""")
    st.divider()
    
    # I 维度
    st.markdown("### **I**")
    st.markdown("""
- **I1**: 元数据可以RDF形式实现描述
- **I2**: 元数据项均可映射至遵循FAIR原则的词汇表
- **I3**: 元数据未提供对其他数据的引用信息
""")
    st.divider()
    
    # R 维度
    st.markdown("### **R**")
    st.markdown("""
- **R1.1**: 采用Creative Commons许可体系
- **R1.2**: 元数据包含作者、时间等来源信息
""")

# -------------------------- 底部悬浮按钮（可选，和你之前风格统一） --------------------------
st.markdown("""
<style>
.block-container {
    padding-bottom: 80px;
}
.fixed-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    padding: 15px 30px;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    z-index: 9999;
    display: flex;
    justify-content: flex-end;
    gap: 15px;
}
</style>
<div class="fixed-footer">
    <button style="background:#0066cc;color:white;border:none;border-radius:8px;padding:10px 25px;font-size:1rem;font-weight:bold;">导出报告</button>
    <button style="background:#00a862;color:white;border:none;border-radius:8px;padding:10px 25px;font-size:1rem;font-weight:bold;">查看详情</button>
</div>
""", unsafe_allow_html=True)
