from gzip import GzipFile
from io import BytesIO
from json import dumps
from zstd import ZstdCompressor
from zstd import ZstdDecompressor


def to_json(obj: object) -> str:
    return dumps(obj, separators=(',', ':'))


def gzip_string(uncompressed: str) -> bytes:
    uncompressed_bytes = uncompressed.encode()
    stream = BytesIO()
    with GzipFile(fileobj=stream, mode='wb') as fobj:
        fobj.write(uncompressed_bytes)  # type: ignore
    stream.seek(0)
    compressed = stream.read()
    return compressed


def gunzip_string(compressed: bytes) -> str:
    stream = BytesIO()
    stream.write(compressed)
    stream.seek(0)
    with GzipFile(fileobj=stream, mode='rb') as fobj:
        uncompressed_bytes = fobj.read()  # type: ignore
    uncompressed = uncompressed_bytes.decode()
    return uncompressed

# Note: zstandard==0.8.1 is in beta and currently does not support streaming input.
# According to their plan, they are planning on including this feature in version 0.9.x
# Once it supports streaming input, we should make changes in compress/decompress.
def zstd_compress(uncompressed: str) -> bytes:
    uncompressed_bytes = uncompressed.encode()
    stream = BytesIO()
    cctx = ZstdCompressor(write_content_size=True)

    with cctx.write_to(stream) as compressor:
        compressor.write(uncompressed_bytes)
        compressor.flush()
    stream.seek(0)
    compressed = stream.read()

    return compressed

def zstd_decompress(compressed: bytes) -> str:
    stream = BytesIO()
    stream.write(compressed)
    stream.seek(0)
    dctx = ZstdDecompressor()

    decompressed_bytes = bytearray()
    for chunk in dctx.read_from(stream):
        decompressed_bytes.extend(chunk)
    decompressed = decompressed_bytes.decode()

    return decompressed
