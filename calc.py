import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

