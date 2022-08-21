from m3u_parser import M3uParser
url = "https://raw.githubusercontent.com/ibratabian17/AltosTV/m3u8channel/index.m3u8"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
parser = M3uParser(timeout=2, useragent=useragent)
parser.parse_m3u(url)
print(len(parser.get_list()))
parser.to_file('AltosJSON.json')
