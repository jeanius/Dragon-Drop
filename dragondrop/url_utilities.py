from urlparse import urlparse, parse_qs

def get_youtube_id(url, domain):
	if domain == "youtube.com":
		parsed_url = urlparse(url)
		parsed_qs = parse_qs(parsed_url.query)
		if 'v' in parsed_qs.keys():
			video_id = parsed_qs['v'][0]
			return video_id