
import feedparser
import streamlit as st

st.set_page_config(
    page_title="Země zprávy",
    page_icon="📰",
    layout="wide",
)

st.title("📰 Země zprávy")
st.caption("České zpravodajství v kontextu.")

SOURCES = {
    "ČT24": "https://ct24.ceskatelevize.cz/rss/hlavni-zpravy",
    "iROZHLAS": "https://www.irozhlas.cz/rss/irozhlas",
    "Seznam Zprávy": "https://www.seznamzpravy.cz/rss",
    "Novinky.cz": "https://www.novinky.cz/rss",
    "Aktuálně.cz": "https://www.aktualne.cz/rss",
    "iDNES.cz": "https://servis.idnes.cz/rss.aspx?c=zpravodaj",
}


articles = []

for source_name, rss_url in SOURCES.items():
    feed = feedparser.parse(rss_url)

    if feed.bozo and not feed.entries:
        st.warning(f"Nepodařilo se načíst {source_name}.")
        continue

    for entry in feed.entries[:20]:
        articles.append({
            "source": source_name,
            "title": entry.get("title", "Bez titulku"),
            "link": entry.get("link", ""),
            "summary": entry.get("summary", ""),
            "published": entry.get("published_parsed"),
        })

articles.sort(
    key=lambda article: article["published"] or (0, 0, 0, 0, 0, 0),
    reverse=True,
)

st.subheader("Nejnovější zprávy")


selected_sources = st.multiselect(
    "Zobrazit média",
    options=list(SOURCES.keys()),
    default=list(SOURCES.keys()),
)

articles = [
    article for article in articles
    if article["source"] in selected_sources
]

for article in articles:

    with st.container(border=True):

        st.markdown(f"### [{article['title']}]({article['link']})")

        st.caption(article["source"])

        if article["published"]:
            import time

            published = time.strftime(
                "%d.%m.%Y %H:%M",
                article["published"],
            )
            st.caption(published)

        if article["summary"]:
            st.write(article["summary"], unsafe_allow_html=False)