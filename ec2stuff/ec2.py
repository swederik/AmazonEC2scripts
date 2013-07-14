import urllib2
from urllib2 import URLError

def grab_metadata():
    amazon_prefix = "http://169.254.169.254/latest/meta-data/"
    metadata_tags = [
        "public-hostname",
        "ami-id",
        "security-groups",
        "ami-launch-index",
        "ami-manifest-path",
        #"block-device-mapping/",
        "hostname",
        "instance-action",
        "instance-id",
        "instance-type",
        #"kernel-id",
        "local-hostname",
        "local-ipv4",
        "mac",
        "network/",
        "placement/",
        "public-ipv4",
        "public-keys",
        "reservation-id",
        "security-groups",
    ]

    block_text = ""

    for metatag in metadata_tags:
        try:
            temp_url = urllib2.urlopen(amazon_prefix + metatag)
        except urllib2.URLError:
            return "Metadata could not be grabbed. Probably not run from an Amazon EC2 server."
        temp_text = temp_url.read()
        block_text += metatag + " : " + temp_text + "\n"

    return block_text
