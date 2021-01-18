import rdata


def read_rdata(fname: str):
    parsed = rdata.parser.parse_file(fname)
    return rdata.conversion.convert(parsed)
