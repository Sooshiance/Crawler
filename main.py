from core.crawler import fetch_data


if __name__=="__main__":
    data = fetch_data("https://stackoverflow.com/questions/70951453/open-a-bundle-file-with-mac")
    print(data)
