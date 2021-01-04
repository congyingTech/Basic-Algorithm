class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split('/')[-1])]
        
if __name__ == "__main__":
    url = ''
    codec = Codec()
    encode_url = codec.encode('https://leetcode.com/problems/design-tinyur')
    print(encode_url)
    print(codec.decode(encode_url))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))