import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Community Help Hub", page_icon="🤝", layout="wide")

if "posts" not in st.session_state:
    st.session_state.posts = [
        {"title":"Found: blue school backpack","category":"Lost & Found","location":"Community library","details":"A blue backpack was found near the library entrance. Please describe it to confirm ownership.","contact":"Contact the library reception","created":"Sample post"},
        {"title":"Free maths study group","category":"Study Support","location":"Community centre","details":"A friendly study session for learners who want to practise maths together.","contact":"Ask the community centre desk","created":"Sample post"},
        {"title":"Saturday recycling collection","category":"Recycling","location":"Main community hall","details":"Bring clean paper, cardboard and plastic bottles for the community recycling drive.","contact":"Community volunteers","created":"Sample post"},
        {"title":"Community clean-up notice","category":"Community Notices","location":"Park entrance","details":"Volunteers are welcome to help tidy the park. Bring water and wear comfortable clothes.","contact":"Community notice board","created":"Sample post"},
    ]

st.markdown("""
<style>
.block-container {max-width:1180px;padding-top:1.8rem}
.hero {padding:2rem;border-radius:22px;background:linear-gradient(120deg,#102a43,#145b66,#1d817d);color:white;margin-bottom:1.2rem}
.hero h1 {color:white;font-size:2.5rem}
.hero p {color:#e4fbf7;font-size:1.1rem}
.pill {display:inline-block;padding:.3rem .7rem;border-radius:999px;background:#d8f5ee;color:#145b55;font-weight:600;font-size:.85rem}
.post {border:1px solid #d9e5e8;border-radius:16px;padding:1rem 1.1rem;margin:.6rem 0;background:white}
.post h3 {color:#102a43;margin:.4rem 0}
.muted {color:#536777;font-size:.9rem}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<span class="pill">NEIGHBOURS HELPING NEIGHBOURS</span>
<h1>🤝 Community Help Hub</h1>
<p>Share local notices, find lost items, learn together, and support a cleaner community.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Explore the Hub")
    page = st.radio("Choose a section", ["Browse posts", "Create a post", "About the project"])
    st.divider()
    st.caption("Learning prototype. Please do not share private or sensitive information.")

if page == "Browse posts":
    st.subheader("Community board")
    st.write("Search notices and find community support.")
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        query = st.text_input("Search posts", placeholder="Try backpack, maths or recycling")
    with c2:
        category = st.selectbox("Category", ["All categories", "Lost & Found", "Study Support", "Recycling", "Community Notices"])
    with c3:
        sort_by = st.selectbox("Sort by", ["Newest first", "Title A–Z"])
    posts = list(st.session_state.posts)
    if category != "All categories":
        posts = [p for p in posts if p["category"] == category]
    if query.strip():
        q = query.strip().lower()
        posts = [p for p in posts if q in " ".join(str(v) for v in p.values()).lower()]
    if sort_by == "Title A–Z":
        posts.sort(key=lambda p: p["title"].lower())
    else:
        posts.reverse()
    m1, m2, m3 = st.columns(3)
    m1.metric("Posts shown", len(posts))
    m2.metric("Categories", 4)
    m3.metric("Project stage", "Prototype")
    if not posts:
        st.info("No matching posts. Try another search or create a notice.")
    for i, post in enumerate(posts):
        st.markdown(f"""
        <div class="post">
        <span class="pill">{post['category']}</span>
        <h3>{post['title']}</h3>
        <div class="muted">📍 {post['location']} · {post['created']}</div>
        <p>{post['details']}</p>
        <p><b>Next step:</b> {post['contact']}</p>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Manage demo post"):
            st.caption("Deleting removes it from this session only.")
            if st.button("Delete this post", key=f"delete_{i}_{post['title']}"):
                st.session_state.posts.remove(post)
                st.rerun()

elif page == "Create a post":
    st.subheader("Share something helpful")
    st.write("Create a notice. Keep it respectful and avoid private details.")
    with st.form("create_post", clear_on_submit=True):
        title = st.text_input("Post title", max_chars=90)
        category = st.selectbox("Category", ["Lost & Found", "Study Support", "Recycling", "Community Notices"])
        location = st.text_input("General location", max_chars=80)
        details = st.text_area("Details", max_chars=500)
        contact = st.text_input("Safe next step", max_chars=120, placeholder="e.g. Ask at the reception desk")
        submitted = st.form_submit_button("Publish post", type="primary", use_container_width=True)
    if submitted:
        if not title.strip() or not location.strip() or not details.strip():
            st.error("Please complete the title, general location and details.")
        else:
            st.session_state.posts.append({
                "title": title.strip(), "category": category, "location": location.strip(),
                "details": details.strip(), "contact": contact.strip() or "Ask a trusted community representative",
                "created": datetime.now().strftime("%d %b %Y, %H:%M")
            })
            st.success("Your post was added to this session's community board.")
            st.info("Prototype note: posts are not shared with other visitors and may not persist after the session ends.")

else:
    st.subheader("About Community Help Hub")
    st.write("Community Help Hub is a community-support app concept that helps people share useful information and find local support.")
    st.markdown("#### The problem")
    st.write("Helpful local information can be scattered across chats, noticeboards and word of mouth.")
    st.markdown("#### The solution")
    st.write("A searchable community board for lost-and-found notices, study support, recycling and community announcements.")
    st.markdown("#### Intended users")
    st.write("Learners, families, community volunteers, local organisations and community centres.")
    st.markdown("#### Future improvements")
    st.write("A shared database, secure accounts, moderation, reporting tools and verified community partners.")
    st.warning("This is a demonstration prototype. Posts are held in the current session, not a shared database. Do not enter phone numbers, home addresses, passwords or other sensitive information.")

st.divider()
st.caption("Community Help Hub · Student project prototype · Built with Python and Streamlit")
