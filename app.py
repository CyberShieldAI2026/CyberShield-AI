import streamlit as st
st.set_page_config(
    page_title="CyberShield AI",
         page_icon="🛡️",
         layout="wide"
     )

st.markdown("""
<style>
.stApp {
    background-color: #07111F;
    color: white;
}
h1, h2, h3 {
    color: #38BDF8 !important;
}
.stButton > button {
    background-color: #0EA5E9;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}
.stTextInput input, .stTextArea textarea {
    background-color: #111D2E;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.title("CyberShield AI  | الأمن السيبراني")
st.write("نظام ذكي للكشف عن التهديدات السيبرانية وتحليلها ")
st.markdown("""
<div style="text-align:center; padding:20px; border-radius:18px; border:1px solid #38BDF8; margin-bottom:25px;">
<h3 style="color:#38BDF8;">🛡️ حماية رقمية أذكى</h3>
<p>CyberShield AI — نظام ذكي لدعم الأمن السيبراني</p>
</div>
""", unsafe_allow_html=True)
st.header("تحليل التهديدات ")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🛡️ حالة النظام", "آمن")

with col2:
    st.metric("🔍 الفحوصات", "جاهز")

with col3:
    st.metric("⚠️ مستوى الخطورة", "متوسط")
user_input = st.text_input("ادخل البيانات المراد تحليلها:")
if st.button("بدء تحليل التهديد"):
     if user_input:
         st.success("تم تحليل البيانات بنجاح")
         st.write("النتيجة: لا توجد تهديدات واضحة")
else:
    st.warning("يرجى إدخال البيانات أولا")
st.header("معلومات الأمن السيبراني")

st.write("-التصيد الاحتيالي : رسائل أو مواقع مزيفة تهدف لسرقة المعلومات.")
st.write("-البرمجيات الخبيثة : برامج قد تضر الجهاز أو تسرق البيانات.")
st.write("-كلمات المرور القوية تساعد على حماية الحسابات .")
threat_type = st.text_input("اكتب نوع التهديد:")

if st .button("عرض المعلومات"):
    if threat_type:
        st.info("تم اختيار نوع التهديد : " + threat_type)
    else:
        st.warning("يرجى كتابة نوع التهديد أولا")
st.header("نصائح للحماية")

st.write("-استخدم كلمات مرور قوية.")
st.write("-لا تفتح الروابط المشبوهة.")
st.write("- حدّث البرامج باستمرار.")
st.write("-لا تشارك معلوماتك الشخصية مع الآخرين.")
st.success(" ابق آمنا واحم معلوماتك الرقمية!")
st.divider()
st.subheader("فحص التهديدات")
user_input = st.text_area("ادخل النص او الرابط المراد فحصه:")
if st.button("فحص التهديد"):
    st.success("تم استلام البيانات للفحص")
st.write("التهديد يحتاج الى تحليل")
st.info("CyberShield AI يساعدك على التعرف التهديدات السيبرانية.")
st.caption("نظام ذكي لدعم الامن السيبراني وتحليل التهديدات ")
st.info("مرحبا بك في CyberShield AI")

st.markdown("---")
st.subheader("نظام CyberShield AI")

st.info("نظام ذكي لدعم الامن السيبراني وتحليل التهديدات الرقمية .")

st.write("اختر نوع التهديد الذي تريد تحليله من القائمة اعلاه, ثم ادخل البيانات المطلوبة .")

st.success("النظام جاهز لتحليل التهديدات")

st.markdown("---")
st.subheader("نتيجة تحليل التهديد")

st.write("نوع التهديد: جاهز للتحليل")
st.write("مستوى الخطورة: متوسط")
st.write("التوصية : تأكد من مصدر البيانات وتجنب الروابطوالملفات المشبوهة.")

st.success("تم الانتهاء من التحليل")
st.divider()

st.subheader("حالة النظام")
st.success("نظام جاهز لتحليل التهديدات ")

st.divider()

st.subheader("إرشادات الأمن السيبراني")
st.info("لا تفتح الروابط المشبوهة")
st.info("استخدم كلمات مرور قوية")
st.info("لا تشارك بياناتك الشخصية")
st.info("حدّث برامج الحماية باستمرار")

st.divider()

st.subheader("عن CyberShield AI")
st.write("نظام ذكي يهدف إلى دعم الوعي بالأمن السيبراني والمساعدة في التعرف على التهديدات الرقمية.")
st.markdown("""
<style>
div[data-testid="stAlert"] {
    border-radius: 15px;
    border: 1px solid #38BDF8;
}
.stButton > button:hover {
    border: 2px solid #38BDF8;
    color: #38BDF8;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
 }
 
 h1 {
     text-align: center;
     font-size: 45px !important;
     font-weight: 800 !important;
     letter-spacing: 1px;
}
  
  h2, h3 {
      border-bottom: 1px solid #1E90FF;
      padding-bottom: 8px;
}
  div[data-testid="stTextInput"],
  div[data-testid="stTextArea"] {
      border-radius: 12px;
}
  
  .stButton > button {
      width: 100%;
      font-weight: bold;
      transition: 0.3s;
 }
   
   .stButton > button:hover {
       transform: scale(1.02)
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
div[data-testid="stAlert"] {
    background: linear-gradient(135deg, #0B1F36, #102E4A);
    border: 1px solid #38BDF8;
    box-shadow: 0 0 15px rgba(56,189,248,0.15);
}

.stTextInput, .stTextArea {
    background-color: #0B1728;
    border-radius: 15px;
}

.stButton > button {
    background: linear-gradient(90deg, #0284C7, #2563EB);
    border-radius: 12px;
    border: 1px solid #38BDF8;
    font-size: 17px;
    font-weight: bold;
    padding: 12px;
    box-shadow: 0 0 12px rgba(14,165,233,0.25);
}

.stButton > button:hover {
    box-shadow: 0 0 22px rgba(56,189,248,0.55);
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* بطاقات الأقسام */
div[data-testid="stVerticalBlock"] {
    gap: 0.8rem;
}

/* العناوين */
h2, h3 {
    color: #38BDF8 !important;
    font-weight: 800 !important;
}

/* تحسين مربعات الإدخال */
.stTextInput input, .stTextArea textarea {
    border: 1px solid #2563EB !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

/* الأزرار */
.stButton > button {
    background: linear-gradient(90deg, #0284C7, #2563EB) !important;
    border: 1px solid #38BDF8 !important;
    border-radius: 12px !important;
    color: white !important;
    font-weight: bold !important;
    transition: 0.3s !important;
}

/* تأثير عند المرور */
.stButton > button:hover {
    box-shadow: 0 0 20px #38BDF8 !important;
    transform: translateY(-2px);
}

/* التنبيهات والنتائج */
div[data-testid="stAlert"] {
    border-radius: 14px !important;
    border: 1px solid #38BDF8 !important;
}

</style>
""", unsafe_allow_html=True)
