from langchain.document_loaders import WebBaseLoader

urls = [
    "https://www.apple.com/newsroom/",
    "https://www.samsung.com/us/news/",
    "https://blog.google/inside-google/company-announcements/",
    "https://news.microsoft.com/",
    "https://www.sony.com/en/SonyInfo/News/",
    "https://press.aboutamazon.com/news-releases/",
    "https://about.fb.com/news/",
    "https://newsroom.intel.com/",
    "https://blogs.nvidia.com/news/",
    "https://www.oracle.com/news/",
    "https://newsroom.ibm.com/",
    "https://newsroom.cisco.com/",
    "https://newsroom.hp.com/",
    "https://newsroom.dell.com/",
    "https://newsroom.lenovo.com/",
    "https://newsroom.huawei.com/",
    "https://www.tesla.com/blog",
    "https://www.salesforce.com/company/news-press/",
    "https://www.adobe.com/newsroom.html",
    "https://newsroom.paypal-corp.com/",
    "https://newsroom.ebayinc.com/",
    "https://newsroom.uber.com/",
    "https://news.lyft.com/",
    "https://press.airbnb.com/",
    "https://newsroom.spotify.com/",
    "https://investor.snap.com/news-releases/news-release-details",
    "https://www.linkedin.com/pulse/news/",
    "https://newsroom.tiktok.com/en-us",
    "https://press.pinterest.com/en",
    "https://investors.netflix.com/news-events/press-releases/default.aspx",
    "https://ir.twitter.com/news/default.aspx",
    "https://newsroom.snapchat.com/",
    "https://newsroom.zoho.com/",
    "https://press.zoom.us/",
    "https://newsroom.shopify.com/",
    "https://investors.dropbox.com/news/default.aspx",
    "https://newsroom.paloaltonetworks.com/",
    "https://www.atlassian.com/company/news",
    "https://newsroom.okta.com/",
]

loader = WebBaseLoader(urls)
documents = loader.load()

# Save documents to a file
import pickle
with open('documents.pkl', 'wb') as f:
    pickle.dump(documents, f)
